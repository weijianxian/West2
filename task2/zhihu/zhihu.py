# 爬取知乎热榜问题

import os
from json import dump, dumps, load, loads
from time import sleep

from selenium.webdriver import Edge, EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class Answer:
    id: str = ""
    content: WebElement = None
    raw_content: str = ""

    def __init__(self, answer_id: str, content: WebElement):
        self.id = answer_id
        self.content = content
        self.raw_content = content.get_attribute("outerHTML")

        print(self.raw_content)

    def __str__(self):
        return f"{self.id}"

    def parse_content(self):
        # TODO: 解析回答内容
        pass


class Question:
    title = ""
    url = ""
    id = ""

    answer_list: list[Answer] = []

    def __init__(self, title: str, question_url: str):
        self.title: str = title
        self.url: str = question_url
        self.id: str = question_url.split("/")[-1]

    # 重写hash和eq方法，用于问题去重
    def __hash__(self):
        return hash((self.title, self.url))

    def __eq__(self, other):
        if isinstance(other, Question):
            return self.title == other.title and self.url == other.url
        return False

    # 重写str方法，用于打印问题
    def __str__(self):
        return f"{self.title},{self.id},{self.url}"


class Zhihu:
    is_login = False

    def __init__(self, driver: Edge = Edge()):
        self.driver = driver

    def login(self, cookies: list = None):
        """
        登录知乎
        :param cookies: 传入cookies登录
        :return: None
        """

        print("正在登录")

        self.driver.get("http://www.zhihu.com/signin")
        sleep(5)

        # 如果传入cookies则直接登录
        if cookies:
            print("通过传入的cookies登录")
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()
            self.is_login = True

        # 未传入则检测本地cookie文件
        elif os.path.exists("cookies"):
            print("通过本地cookies登录")
            cookies = load(open("cookies"))
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()
            self.is_login = True

        # 未检测到cookie文件则手动登录
        else:
            print(f"{'='*20}\n请登录\n{'='*20}")
            while self.driver.current_url != "https://www.zhihu.com/":
                sleep(1)
            # 保存cookies
            dump(
                [
                    {"name": cookie["name"], "value": cookie["value"]}
                    for cookie in self.driver.get_cookies()
                ],
                open("cookies", "w"),
            )

            print("保存cookies成功")
            self.driver.refresh()
            self.is_login = True

    def get_hot(self) -> list[Question]:
        """
        获取知乎热榜问题
        :return: 热榜问题列表
        """
        self.driver.get("https://www.zhihu.com/hot")
        sleep(5)
        questions = self.driver.find_elements(By.CLASS_NAME, "HotItem")

        hot_question_list: list[Question] = []
        for question in questions:
            content = question.find_element(By.CLASS_NAME, "HotItem-content")
            title = content.find_element(By.TAG_NAME, "a").get_attribute("title")
            url = content.find_element(By.TAG_NAME, "a").get_attribute("href")

            hot_question_list.append(Question(title, url))

        return hot_question_list

    def get_topic_top_question(self, url: str, scroll_times: int = 5) -> list[Question]:
        """
        获取知乎话题热榜问题
        :param url: 话题url
        :param scroll_times: 滚动次数
        :return: 问题列表
        """

        self.driver.get(url)

        # 滚动
        for _ in range(scroll_times):
            sleep(2)
            self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )

        sleep(5)
        questions_list = self.driver.find_elements(By.CLASS_NAME, "TopicFeedItem")
        topic_top_question_set: set[Question] = set()

        for question in questions_list:
            content = question.find_element(By.CLASS_NAME, "ContentItem-title")

            try:
                meata_data = content.find_elements(By.TAG_NAME, "meta")
                url = meata_data[0].get_attribute("content")
                title = meata_data[1].get_attribute("content")
                # 问题去重
                topic_top_question_set.add(Question(title, url))

            except:
                continue

        return list(topic_top_question_set)

    def get_answer(self, question: Question, scroll_times: int = 5) -> list[Answer]:
        """
        获取问题的回答
        :param question: 问题
        :param scroll_times: 滚动次数
        :return: 回答列表
        """
        print(f"正在获取问题：{question}")
        driver = self.driver
        driver.get(question.url)

        # 滚动
        for _ in range(scroll_times):
            sleep(2)
            print("正在滚动答案页面")
            self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )

        answer_list: list[WebElement] = driver.find_elements(
            By.CLASS_NAME, "AnswerItem"
        )

        # 获取回答
        for answer_webelement in answer_list:
            # 获取回答元数据
            asnwer_meta_data = loads(answer_webelement.get_attribute("data-zop"))
            answer_id = asnwer_meta_data["itemId"]

            question.answer_list.append(
                Answer(
                    answer_id,
                    answer_webelement.find_element(By.CLASS_NAME, "RichText"),
                )
            )


def main():

    # 创建Edge浏览器 & 初始化知乎客户端
    options = EdgeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    client = Zhihu(driver=Edge(options=options))

    client.driver.execute_cdp_cmd(
        "Page.addScriptToEvaluateOnNewDocument",
        {
            "source": """
                Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
                })
            """
        },
    )
    client.login()

    test_question = Question("test", "https://www.zhihu.com/question/26742539")

    client.get_answer(test_question)

    input("回车退出")


if __name__ == "__main__":
    main()
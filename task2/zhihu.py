# 爬取知乎热榜问题

import os
from json import dump, load
from time import sleep

from selenium.webdriver import Edge
from selenium.webdriver.common.by import By


class Answer:
    def __init__(
        self,
        url: str,
        content: str,
    ):
        self.url = url
        self.content = content


class Question:
    title = ""
    question_url = ""
    answer_list: list[Answer] = []

    def __init__(self, title: str, question_url: str):
        self.title: str = title
        self.question_url: str = question_url

    def __hash__(self):
        return hash((self.title, self.question_url))

    def __eq__(self, other):
        if isinstance(other, Question):
            return self.title == other.title and self.question_url == other.question_url
        return False

    def __str__(self):
        return f"{self.title},{self.question_url}"


class Zhihu:
    is_login = False

    def __init__(self, driver: Edge):
        self.driver = driver

    def login(self, cookies: list = None):
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
            return

        # 未传入则检测本地cookie文件
        if os.path.exists("cookies"):
            print("通过本地cookies登录")
            cookies = load(open("cookies"))
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()
            self.is_login = True
            return

        # 未检测到cookie文件则手动登录
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
        self.driver.refresh()
        self.is_login = True
        return True

    def get_hot(self) -> list[Question]:
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

    def get_topic_top_question(self, url) -> list[Question]:
        self.driver.get("https://www.zhihu.com/topic/19554298/top-answers")

        # 滚动到底部
        for _ in range(5):
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


def main():
    driver = Edge()

    zhihu = Zhihu(driver)
    zhihu.login()

    # 获取热榜问题
    hot_question_list = zhihu.get_topic_top_question(
        url="https://www.zhihu.com/topic/19554298/top-answers"
    )
    for question in hot_question_list:
        print(question)
    # 获取热榜问题
    # hot_question_list = zhihu.get_hot()
    # for question in hot_question_list:
    #     print(question)


if __name__ == "__main__":
    main()

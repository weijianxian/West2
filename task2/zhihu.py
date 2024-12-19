# 爬取知乎热榜问题

import os
from json import dump, load
from time import sleep

from selenium.webdriver import Edge
from selenium.webdriver.common.by import By


class Question:
    def __init__(self, title, question_url):
        self.title = title
        self.question_url = question_url

    def __str__(self):
        return f"{self.title},{self.question_url}"


class Zhihu:

    def __init__(
        self,
        driver: Edge,
        cookies: list = None,
    ):
        self.driver = driver
        # 添加cookies

        driver.get("https://www.zhihu.com/")
        if cookies:
            for item in cookies:
                self.driver.add_cookie(item)
            self.driver.refresh()

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


def main():
    driver = Edge()

    # 如果没有cookies文件则登录
    if not os.path.exists("cookies"):
        while driver.current_url != "https://www.zhihu.com/":
            print("请登录")
            sleep(1)
        dump(
            [
                {"name": cookie["name"], "value": cookie["value"]}
                for cookie in driver.get_cookies()
            ],
            open("cookies", "w"),
        )
        print(f"{'='*20}\n登录成功\n{'='*20}")

    # 初始化知乎
    zhihu = Zhihu(driver, load(open("cookies")))

    # 获取热榜问题
    hot_question_list = zhihu.get_hot()
    for question in hot_question_list:
        print(question)


if __name__ == "__main__":
    main()

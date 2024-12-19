import httpx
from bs4 import BeautifulSoup as bs
from bs4.element import Tag
from tqdm import tqdm


# 页面类
class Pages:
    def __init__(self, link):
        self.link = link
        self.notifys = []

        response = httpx.get(self.link)
        soup: bs = bs(response.text, "html.parser")
        items: list[Tag] = soup.find_all("ul", class_="list-gl")[0].find_all("li")
        for i in items:
            time = i.find("span").text.strip()
            title = i.find("a").text.strip()
            link = "https://jwch.fzu.edu.cn/" + i.find_all("a")[0]["href"]
            organze = i.text.strip().replace(time, "").replace(title, "").strip()
            self.notifys.append(Notify(time, organze, title, link))


# 通知类
class Notify:
    def __init__(self, time, organze, title, link):
        self.time = time
        self.organze = organze
        self.title = title
        self.link = link
        self.file: File = None

    @property
    def to_csv(self):
        if self.file:
            return f"{self.time},{self.organze},{self.title},{self.link},{self.file.to_csv()}"
        else:
            return f"{self.time},{self.organze},{self.title},{self.link}"

    # def get(self):
    #     response = httpx.get(self.link)
    #     soup = bs(response.text, "html.parser")
    #     try:
    #         file_tag = (
    #             soup.find("div", class_="xl_main")
    #             .find("ul", style="list-style-type:none;")
    #             .find("li")
    #         )
    #         self.file = File(
    #             name=file_tag.find("a").text,
    #             download_link="https://jwch.fzu.edu.cn/" + file_tag.find("a")["href"],
    #             times=file_tag.find("span").text,
    #         )
    #     except:
    #         self.file = None
    #     return self.csv


# 文件类
class File:
    def __init__(self, name, download_link, times):
        self.name = name
        self.link = download_link
        self.times = times

    def __str__(self):
        return f"{self.name} {self.link}"

    def to_csv(self):
        return f"{self.name},{self.link}"


def main():
    base_url = "https://jwch.fzu.edu.cn/jxtz"
    page_list = [Pages(f"{base_url}.htm")] + [
        Pages(f"{base_url}/{i}.htm") for i in range(1, 195)
    ][::-1]

    # 获取所有通知的详细信息并写入文件
    with open("FZU_Info.csv", "w", encoding="UTF-8") as f:
        f.write("时间,组织,标题,链接\n")
        for page in tqdm(page_list, desc="获取页面"):
            for notify in page.notifys:
                f.write(notify.csv + "\n")


if __name__ == "__main__":
    main()

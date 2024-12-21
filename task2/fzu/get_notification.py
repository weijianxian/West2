import asyncio
import time

import httpx
from bs4 import BeautifulSoup as bs
from bs4.element import Tag
from tqdm import tqdm
from tqdm.asyncio import tqdm as atqdm


# 页面类
class Pages:
    def __init__(self, page_index: str):
        self.page_index = page_index

        if page_index == "0":
            self.link = "https://jwch.fzu.edu.cn/jxtz.htm"
        else:
            self.link = "https://jwch.fzu.edu.cn/jxtz/" + page_index + ".htm"
        self.notifys: list[Notify] = []

    async def get_notifys(self):
        async with httpx.AsyncClient() as client:
            response = await client.get(self.link)
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
    def __init__(
        self,
        time: str,
        organze: str,
        title: str,
        link: str,
    ):
        self.time = time
        self.organze = organze
        self.title = title
        self.link = link
        self.files: list["File"] = []

    @property
    def csv(self):
        if self.files:
            return f"{self.time},{self.organze},{self.title},{self.link},{sum([file.times for file in self.files])}"
        else:
            return f"{self.time},{self.organze},{self.title},{self.link},0"

    async def get_file(self):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(self.link)
                soup: bs = bs(response.text, "html.parser")
                file_tags: list[Tag] = soup.select(
                    "body > div.page > div.w-main > div.wapper > form > div.wapper >div.ny_box >div.xl_main"
                )[0].find_all("li")

                for file_tag in file_tags:
                    file_name = file_tag.find("a").text.strip().replace("附件：", "")

                    file_link = "https://jwch.fzu.edu.cn" + file_tag.find("a")["href"]
                    # 获取下载次数
                    resp = await client.get(
                        f"https://jwch.fzu.edu.cn/system/resource/code/news/click/clicktimes.jsp",
                        params={
                            "wbnewsid": file_link.split("wbfileid=")[1],
                            "owner": file_link.split("owner=")[1].split("&")[0],
                            "type": "wbnewsfile",
                            "randomid": "nattach",
                        },
                    )
                    download_times = resp.json()["wbshowtimes"]

                    self.files.append(File(file_name, file_link, download_times))
        except Exception as e:
            pass


# 文件类
class File:
    def __init__(
        self,
        name=None,
        download_link=None,
        download_times=0,
    ):
        self.name = name
        self.link = download_link
        self.times = download_times

    @property
    def csv(self):
        return f"{self.name},{self.times}"


async def main():
    page_list = [Pages(str(i)) for i in range(0, 195)]

    await atqdm.gather(
        *[page.get_notifys() for page in page_list],
        desc="获取通知",
        position=0,
    )

    notify_list = [notify for page in page_list for notify in page.notifys]
    get_files_tasks = [notify.get_file() for notify in notify_list]

    # 分块执行任务
    chunk_size = 200
    all_chunks = len(notify_list) // chunk_size + 1
    for i in tqdm(range(all_chunks), desc="获取文件", position=0, leave=False):
        start = i * chunk_size
        end = (i + 1) * chunk_size
        await atqdm.gather(
            *get_files_tasks[start:end],
            desc=f"第{i+1:<2}块",
            position=1,
        )

        time.sleep(1)

    with open("notification.csv", "w", encoding="utf-8") as f:
        for notify in notify_list:
            f.write(notify.csv + "\n")


if __name__ == "__main__":
    asyncio.run(main())

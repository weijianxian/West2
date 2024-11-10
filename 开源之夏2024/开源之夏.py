import asyncio
import os
import re

import aiofiles
import httpx


def clean_projectname(filename: str) -> str:
    """
    清理文件名，去除不允许的字符
    """
    return re.sub(r'[\/:*?"<>|,]', "_", filename)


async def get_PDF_file(key: str, file_name: str) -> None:
    """
    :param key: str 项目id
    """
    async with httpx.AsyncClient() as client:
        PDF_data = await client.post(
            url="https://summer-ospp.ac.cn/api/publicApplication",
            json={"proId": key},
        )
    os.makedirs("./PDF", exist_ok=True)
    file_name = clean_projectname(file_name)
    async with aiofiles.open(f"./PDF/{file_name}.pdf", "wb") as f:
        await f.write(PDF_data.content)


async def get_endApplication_file(program_id: str, file_name: str) -> None:
    """
    :param program_id: str 项目id
    """
    async with httpx.AsyncClient() as client:
        endApplication_url = (
            await client.post(
                url="https://summer-ospp.ac.cn/api/getProDetail",
                json={
                    "programId": program_id,
                    "type": "org",
                },
            )
        ).json()["endApplicationUrl"]

        endApplication_data = await client.get(endApplication_url)
    os.makedirs("./endApplication", exist_ok=True)
    file_name = clean_projectname(file_name)
    async with aiofiles.open(f"./endApplication/{file_name}.zip", "wb") as f:
        await f.write(endApplication_data.content)


async def get_page_data(page: int) -> list:
    """
    :param page: int 页数，每页50条数据
    """
    async with httpx.AsyncClient() as client:
        response = await client.post(
            url="https://summer-ospp.ac.cn/api/getAnnouncement",
            headers={
                "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                "content-type": "application/json",
            },
            json={
                "programName": "",
                "pageNum": page,
                "pageSize": "50",
                "name": "",
                "orgName": "",
            },
        )
    return response.json()["rows"]


async def main():
    async with aiofiles.open("开源之夏.csv", "w", encoding="utf-8") as f:
        await f.write(
            "作者名字,项目名字,导师名字,申请报告path,结项文件path,仓库地址(可能存在多个)\n"
        )
        for page in range(1, 11):
            print(f"正在爬取第{page}页数据")
            page_data = await get_page_data(page)
            tasks = []
            for item in page_data:
                author_name = item["name"]  # 作者名字
                program_name = item["programName"]  # 项目名字
                leader_name = item["realName"]  # 导师名字
                repo_url_list = item["repo"]  # 仓库地址

                # 下载申请书
                tasks.append(get_PDF_file(item["orgProgramId"], program_name))
                # 下载结题报告
                tasks.append(
                    get_endApplication_file(item["orgProgramId"], program_name)
                )
                await f.write(
                    f"{author_name},{clean_projectname(program_name)},{leader_name},./PDF/{clean_projectname(program_name)}.pdf,./endApplication/{clean_projectname(program_name)}.zip,{','.join(repo_url_list)},\n"
                )

            await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())

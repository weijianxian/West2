import os
import re

import aiofiles
import httpx


async def get_PDF_file(key: str, file_path: str) -> None:
    """
    :param key: str 项目id
    """
    async with httpx.AsyncClient() as client:
        PDF_data = await client.post(
            url="https://summer-ospp.ac.cn/api/publicApplication",
            json={"proId": key},
        )

    async with aiofiles.open(f"{file_path}.pdf", "wb") as f:
        await f.write(PDF_data.content)


async def get_endApplication_file(endApplication_url: str, file_path: str) -> None:
    """
    :param endApplication_url: str 结题报告URL
    """

    async with httpx.AsyncClient() as client:
        endApplication_data = await client.get(endApplication_url)

    async with aiofiles.open(f"{file_path}", "wb") as f:
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


async def get_program_detail(program_id: str) -> dict:
    """
    :param program_id: str 项目id
    """
    async with httpx.AsyncClient() as client:
        response = await client.post(
            url="https://summer-ospp.ac.cn/api/getProDetail",
            json={
                "programId": program_id,
                "type": "org",
            },
        )
    return response.json()

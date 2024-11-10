import asyncio

from tqdm.asyncio import tqdm

from sql_saver import ProgramDetail, session
from utils import *

os.makedirs("./PDF", exist_ok=True)
os.makedirs("./endApplication", exist_ok=True)


async def main():
    for page in range(1, 11):
        print(f"正在爬取第 {page} 页数据")
        page_data = await get_page_data(page)
        tasks = []
        for item in page_data:
            ProgramId = item["orgProgramId"]

            program = ProgramDetail(
                info=item, detail=await get_program_detail(ProgramId)
            )
            # 添加到数据库
            session.add(program)

            # 添加下载任务到列表
            tasks.append(get_PDF_file(program.program_id, program.PDF_path))
            tasks.append(
                get_endApplication_file(
                    program.end_application_url, program.end_application_path
                )
            )

        session.commit()
        # 并发下载
        await tqdm.gather(*tasks, desc=f"下载第 {page} 页文件")


if __name__ == "__main__":
    asyncio.run(main())

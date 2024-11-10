import re

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def clean_filename(filename: str) -> str:
    """
    清理文件名，去除不允许的字符
    """
    return re.sub(r'[\/:*?"<>|]', "_", filename)


Base = declarative_base()


class ProgramDetail(Base):
    __tablename__ = "开源之夏2024"
    # 表结构
    id = Column(Integer, primary_key=True)
    # 项目id
    program_id = Column(String, nullable=False)
    # 作者名 中选学生名字
    author_name = Column(String, nullable=False)
    # 导师名字
    leader_name = Column(String, nullable=False)
    # 项目名
    program_name = Column(String, nullable=False)
    # 项目代码
    program_code = Column(String, nullable=False)
    # 仓库地址
    repo_url = Column(String, nullable=False)
    # 结题报告地址
    end_application_url = Column(String, nullable=False)
    # 技术标签
    tech_tag = Column(String, nullable=False)
    # 编程语言标签
    programmingLanguageTag = Column(String, nullable=False)
    # 导师邮箱
    email = Column(String, nullable=False)
    # git用户名
    gitUserName = Column(String, nullable=True)
    # 项目名清理后
    program_name_clean = Column(String, nullable=False)
    # PDF路径
    PDF_path = Column(String, nullable=False)
    # 结题报告路径
    end_application_path = Column(String, nullable=False)

    def __init__(self, info, detail):
        self.program_id = info["orgProgramId"]
        self.author_name = info["name"]
        self.leader_name = info["realName"]
        self.program_name = info["programName"]
        self.program_name_clean = clean_filename(self.program_name)
        self.program_code = detail["programCode"]
        self.repo_url = ",".join(detail["repo"])
        self.end_application_url = detail["endApplicationUrl"]
        self.tech_tag = ",".join(["-".join(i) for i in eval(detail["techTag"])])
        self.email = detail["email"]
        self.gitUserName = detail.get("gitUserName")
        self.programmingLanguageTag = ",".join(eval(detail["programmingLanguageTag"]))

        self.PDF_path = f"./PDF/{self.program_code}-{self.program_name_clean}.pdf"
        self.end_application_path = (
            f"./endApplication/{self.program_code}-{self.program_name_clean}.zip"
        )


# 创建数据库引擎
engine = create_engine("sqlite:///开源之夏2024.db")
Base.metadata.create_all(engine)

# 创建会话
Session = sessionmaker(bind=engine)
session = Session()

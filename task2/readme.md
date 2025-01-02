# 项目简介

本项目是一个基于 Python 的爬虫和数据处理项目，主要包括两个部分：

1. **福大通知爬虫**：从福州大学教务处网站抓取通知信息，并将结果保存到 `notification.csv` 文件中，并对数据进行分析。
2. **知乎爬虫**：从知乎抓取问题及其回答，并处理反爬虫机制。
3. **开源之夏 2024**：从指定网站抓取开源项目的详细信息，并将这些信息保存到数据库中，同时下载相关的 PDF 文件和结束申请文件。

项目使用了 `httpx`、`BeautifulSoup`、`tqdm`、`selenium` 等库来实现对网页数据的抓取和处理。

# 文件结构

```
project
└─task2
   ├─fzu            # 福大教务处
   │  ├─get_notification.py #获取通知
   │  └─analyse.ipynb # 分析
   ├─zhihu          # 知乎
   │  └─zhihu.py
   └─开源之夏2024      # 开源之夏爬虫
      ├─main.py       # 主程序文件
      ├─sql_saver.py  # 数据库保存模块
      ├─utils.py      # 工具函数模块
      ├─PDF           # 存储下载的PDF文件
      ├─requirements.txt # 依赖
      └─endApplication # 存储下载的结束申请文件

```

# 1. 福大通知爬虫

## 1. get_notification.py

- **功能**：从指定的网页抓取通知信息，并将结果保存到 `notification.csv` 文件中。
- **主要模块**：
  - `Pages` 类：用于处理每个页面的通知信息。
  - `Notify` 类：用于处理每条通知的详细信息。
  - `File` 类：用于处理通知中的文件信息。
  - `main` 函数：主函数，负责控制整个爬取流程。

## 2. analyse.ipynb

- **功能**：分析数据
- **主要模块**：
  - 使用 jupyter notebook 的形式完成代码以及分析报告
  - 统计“通知人”都有哪些，各占比例多少？
  - 分析附件下载次数与通知人是否关系，若有，有什么联系？
  - 统计每天的通知数，分析哪段时间通知比较密集？
  - others

# 2. 知乎

- **功能**：从知乎抓取问题及其回答，并处理反爬虫机制。
- **主要模块**：
  - `ZhihuClient` 类：用于处理知乎的登录和数据抓取。
  - `get_answer` 方法：用于获取指定问题的回答，并处理反爬虫机制。
  - `scroll_page` 方法：用于模拟页面滚动，加载更多内容。
  - `main` 函数：主函数，负责控制整个爬取流程。

# 3. 开源之夏

- **主要功能**：爬取开源之夏 2024 结项文件和项目报告，使用 sql lite 存储数据

## 主要模块

### main.py

- **功能**：主程序文件，负责控制整个爬取流程，包括获取页面数据、解析数据、保存数据到数据库以及下载相关文件。

### sql_saver.py

- **功能**：数据库保存模块，定义了数据模型和数据库会话。
- **ProgramDetail**：定义了项目详细信息的数据模型。
- **session**：对象：数据库会话，用于执行数据库操作。

### utils.py

- **功能**：工具函数模块，包含了获取页面数据、获取项目详细信息、下载文件等功能的实现。
- **get_page_data(page)**：获取指定页面的数据。
- **get_program_detail(ProgramId)**：获取指定项目的详细信息。
- **get_PDF_file(program_id, PDF_path)**：下载指定项目的 PDF 文件。
- **get_endApplication_file(end_application_url, end_application_path)**：下载指定项目的结束申请文件。

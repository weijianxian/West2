## [Assignment #1 of Spring 2024.](http://cs231n.github.io/) 本地翻译版 

### 如何运行? 
1. 安装依赖 `pip install -r requirements.txt`
2. 下载 
[数据集](http://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz) 和 
[imagenet_val_25.npz](http://cs231n.stanford.edu/imagenet_val_25.npz) 并 
解压到 ./cs2310/datasets/
    <details>
    <summary>解压后的文件夹格式为：</summary>
    
    ```bash
    ├─datasets
    │  │  get_datasets.sh # 用于Linux系统下载解压文件的脚本
    │  │  imagenet_val_25.npz
    │  │
    │  └─cifar-10-batches-py # 数据集
    │          batches.meta
    │          data_batch_1
    │          data_batch_2
    │          data_batch_3
    │          data_batch_4
    │          data_batch_5
    │          readme.html
    │          test_batch
    ```
    </details>

### 
### made by weijx
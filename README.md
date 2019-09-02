# 浮生梦家族信息OCR系统
Abstract: The automated OCR system for [ninjia never die 3](http://www.pandadastudio.com/).

该系统旨在简化数据统计流程。以输入图片序列的形式，自动将信息结构化（统计成.csv文件，便于Microsoft excel等其他可视化工具打开）。

### 依赖项Prerequisites

1. Download and install [Anaconda 3](https://www.anaconda.com/distribution/) according to your platform.
2. Install AipOcr, a python binding for Baidu AI platform.(pip install baidu-aip, [tutorial](https://www.jianshu.com/p/e10dc43c38d0))

## 特性

- 以图片为输入，自动识别信息
- 和家族metadata对应，进行模糊搜索。能将最新信息同步到历史数据库。
- 自动生成每周周报（TODO）

## 已实现功能

- 深渊排名信息自动识别，并和metadata进行模糊匹配

## 程序入口

### 深渊信息自动生成

1. 将你的目录切换至当前库，文件的输入在`data\8_30`
2. 修改`fushengmeng_ocr\cfg\basic_config.py`中的百度APP_ID, SECRET_KEY等参数（获得方法请上[百度云AI控制台](https://console.bce.baidu.com/ai/#/ai/ocr/overview/index)，文字识别项查询，和我认识的可以直接问我要）。
3. 打开控制台，运行`python 8_30.py`.
4. OCR结果在`data\8_30\result`，表格结果在`8_30.csv`

## Todo

1. 家族团队副本统计
2. 库整体框架注释
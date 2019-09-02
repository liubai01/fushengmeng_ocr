"""
The configuration file， including the parameters and flags of OCR system.

WARNING: 请注意不要泄露我的APP_ID。百度OCR超过每天额度是要扣我的钱的，虽然不多，
但是请不要过度调用我的代码。维护代码库请避免OCR的overhead.
"""
import os

root_path = os.path.realpath(__file__)
root_path = os.path.split(root_path)[0]
root_path = os.path.split(root_path)[0]
root_path = os.path.split(root_path)[0]

data_path = os.path.join(root_path, "data")
metadata_path = os.path.join(data_path, "metadata", "metadata.csv")


class basic_cfg:
    # 百度OCR相关设置（调用百度API进行模板识别）
    APP_ID = 'INPUT_YOUR_APP_ID'
    API_KEY = 'INPUT_YOUR_APP_KEY'
    SECRET_KEY = 'INPUT_YOUR_SECRET_KEY'

    SHENYUAN_TEMPLATESIGN = '5e325de161f970154c1d11c26147712b'

    # 一些数据的基本路径
    METADATA_PATH = metadata_path
    DATA_PATH = data_path
    assert os.path.exists(METADATA_PATH)
    assert os.path.exists(DATA_PATH)

    ocr_plot_result = True
    DEBUG = True

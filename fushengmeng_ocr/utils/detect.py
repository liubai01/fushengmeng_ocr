import matplotlib
matplotlib.use('TkAgg')
matplotlib.rcParams['font.family'] = 'SimHei'

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import os

from aip import AipOcr
from ..cfg.basic_config import basic_cfg

APP_ID = basic_cfg.APP_ID
API_KEY = basic_cfg.API_KEY
SECRET_KEY = basic_cfg.SECRET_KEY

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def ocr_shenyuan(fname, plot_im=False):
    """
    深渊图片的OCR检测
    :param fname: the path for input image
    :return: a list of size 9x3: ['名称', '伤害', '挑战次数']
    """
    image = get_file_content(fname)

    results = client.custom(image, options={'templateSign': basic_cfg.SHENYUAN_TEMPLATESIGN})
    data = results['data']['ret']

    if basic_cfg.DEBUG:
        print(data)

    if plot_im:
        plt.cla()
        plt.figure(figsize=(30, 20))
        currentAxis=plt.gca()
        image_PIL = Image.open(fname)
        plt.imshow(image_PIL)

        for i in data:
            try:
                word = i['word']
                height, left, top, width = i['location']['height'], i['location']['left'], i['location']['top'], i['location']['width']

                rect = patches.Rectangle(
                    (left, top), width, height, linewidth=1, edgecolor='r', facecolor='none'
                )
                currentAxis.add_patch(rect)

                plt.text(left, top + 0.5, word)
            except Exception as e:
                print(e, i)

        to_path = os.path.splitext(fname)[0] + "_result.jpg"
        dir, filename = os.path.split(to_path)
        dir = os.path.join(dir, "result")
        if not os.path.exists(dir):
            os.mkdir(dir)

        plt.savefig(os.path.join(dir, filename))

    structured_data = [[None for _ in range(3)] for _ in range(9)]

    for i in data:
        word_name = i['word_name']
        word = i['word']
        _, seq, v = word_name.split('#')

        seq = int(seq)
        if v == '挑战次数':
            try:
                structured_data[seq - 1][2] = int(word)
            except Exception as e:
                structured_data[seq - 1][2] = None
        elif v == '名称':
            try:
                if len(word) > 3 and word[-3:] == '副族长':
                    structured_data[seq - 1][0] = word[:-3]
                elif len(word) > 2 and word[-2:] in ['族员', '族长', '新人', '豪杰', '长老', '精英']:
                    structured_data[seq - 1][0] = word[:-2]
                else:
                    structured_data[seq - 1][0] = word
            except Exception as e:
                    structured_data[seq - 1][0] = None
        elif v == '伤害':
            try:
                structured_data[seq - 1][1] = int(word)
            except Exception as e:
                structured_data[seq - 1][1] = None

    return structured_data

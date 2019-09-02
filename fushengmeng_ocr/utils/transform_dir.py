"""
This script detect all the image under the datafile. And serailize the result into
the .pkl(picklized) file.
"""

import os
from .detect import ocr_shenyuan
from ..cfg.basic_config import basic_cfg
import pickle

def save_obj(path, obj):
    with open(path, "wb")as f:
        ret = pickle.dump(obj, f)
    return ret

def transform_dir(dir_path):
    files = os.listdir(dir_path)

    for fname in files:
        # Remark: only process the image with postfix '.png'
        if fname.endswith(".png"):
            try:
                png_path = os.path.join(dir_path, fname)
                pkl_name = fname[:-4] + ".pkl"
                pkl_path = os.path.join(dir_path, pkl_name)

                if os.path.exists(pkl_path):
                    print("OCR detect system: {} exists".format(fname))
                    continue

                info = ocr_shenyuan(png_path, plot_im=basic_cfg.ocr_plot_result)
                save_obj(pkl_path, info)

                print("OCR detect system: {} success".format(fname))
            except Exception as e:
                print(e)
                print("OCR detect system: {} failed".format(fname))

if __name__ == "__main__":
    filepath = os.path.join('data', '8_30')
    transform_dir(filepath)

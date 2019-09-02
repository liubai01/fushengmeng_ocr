import os
import pickle
import pandas as pd
from .LCS import find_fit_name
from ..cfg.basic_config import basic_cfg

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt

def load_obj(path):
    with open(path, "rb")as f:
        ret = pickle.load(f)
    return ret

class Metadata_entry:

    def __init__(self, name, uid, rank):
        self.has_checked = False

        self.name = name
        self.uid = uid
        self.rank = rank

def aggr_info(dir_path):
    files = os.listdir(dir_path)

    data = []

    # Load in the metadata
    metadata = pd.read_csv(basic_cfg.METADATA_PATH)
    meta_names = []
    meta_dict = {}
    meta_entries = []

    # generate metadata entries
    for idx, row in metadata.iterrows():
        e = Metadata_entry(row['名字'], row['uid'], row['忍阶'])

        name_possible = [row['名字']]
        if str(row['别名']) != 'nan':
            name_possible += row['别名'].split('，')
        meta_names += name_possible

        for n in name_possible:
            meta_dict[n] = e
        meta_entries.append(e)

    # Load the chached OCR information
    for fname in files:
        if fname.endswith(".pkl"):
            pkl_path = os.path.join(dir_path, fname)
            info = load_obj(pkl_path)
            data += info

    # if fit, join the table
    for idx, i in enumerate(data):
        fit_name = find_fit_name(i[0], meta_names)
        if fit_name:
            e = meta_dict[fit_name]

            data[idx] += [meta_dict[fit_name].uid, meta_dict[fit_name].rank]
            meta_dict[fit_name].has_checked = True
            data[idx][0] = meta_dict[fit_name].name
        else:
            data[idx] += [None for _ in range(2)]

    for k, v in meta_dict.items():
        uid, rank, flag = v.uid, v.rank, v.has_checked
        if not flag:
            data.append([k, 0, 0, uid, rank])

    df = pd.DataFrame(data, columns=['名字', '伤害', '挑战次数', 'uid', '忍阶'], index=None)

    return df


if __name__ == "__main__":
    filepath = os.path.join('data', '8_30')
    df = aggr_info(filepath)
    df['平均伤害'] = df['伤害'] / df['挑战次数']

    df.to_csv('8_30.csv')
    print(df)

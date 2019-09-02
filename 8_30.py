from fushengmeng_ocr.utils.transform_dir import transform_dir
from fushengmeng_ocr.utils.aggrete_info import aggr_info
import os

if __name__ == "__main__":
    filepath = os.path.join('data', '8_30')
    transform_dir(filepath)

    df = aggr_info(filepath)
    df['平均伤害'] = df['伤害'] / df['挑战次数']

    df.to_csv('8_30.csv')
    print(df)

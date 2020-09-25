import numpy as np
import pandas as pd
import xml.etree.ElementTree as ET
from sqlalchemy import create_engine


def main():
    root = ET.parse('/Users/felix/Desktop/rep.xml').getroot()

    df_cols = ['id', 'name', 'time']
    df = pd.DataFrame(columns=df_cols)

    count = 1
    for i in root[5]:
        try:
            df = df.append(
                pd.Series([count, i[3][0][2].text, i[1].text], index=df_cols),
                ignore_index=True)
        except:
            pass
        count = count + 1

    print(df.head())

    engine = create_engine('sqlite://')
    df.to_sql('test', con=engine, if_exists="replace")

    engine.execute('select * from test')


if __name__ == '__main__':
    main()

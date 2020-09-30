import numpy as np
import pandas as pd
import xml.etree.ElementTree as ET
from sqlalchemy import create_engine


def main():
    root = ET.parse('/Users/felix/Desktop/rep.xml').getroot()

    df_cols = ['fdid', 'name', 'time']
    df = pd.DataFrame(columns=df_cols)

    for i in root[5]:
        try:
            if i[3][0][2].tag == '{http://www.hikvision.com/ver20/XMLSchema}name':
                df = df.append(
                    pd.Series([i[3][0][0].text, i[3][0][2].text, i[1].text], index=df_cols),
                    ignore_index=True)
        except:
            df = df.append(
                pd.Series(['-', '-', '-'], index=df_cols),
                ignore_index=True
            )

    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(df)

    # engine = create_engine('sqlite://')
    # df.to_sql('test', con=engine, if_exists="replace")

    # engine.execute('select * from test')


if __name__ == '__main__':
    main()

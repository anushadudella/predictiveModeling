# observations / data
import Constants
import pandas as pd
from pathlib import Path

def loadFiles():

    directory = Constants.INPUT_LOC
    files = list(Path(directory).glob('*'))

    df = pd.DataFrame()
    lsDataframes = []

    try:
        if (len(files) < 1):
            raise Exception()
        else:
            for file in files:
                df_temp = pd.read_csv(file)
                lsDataframes.append(df_temp)
            df = pd.concat(lsDataframes)
            print(df.size)

            return df
    except:
        print(" No COVID case files found ")
        sys.exit()
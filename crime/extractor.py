# Importing required libraries
import os
import pandas as pd
from dotenv import load_dotenv

# Recovering dotenv variables
load_dotenv()

# Defining files path
CRIME_FILES_PATH = os.getenv('CRIME_FILES_PATH')

def extract() -> pd.DataFrame:
    df = pd.DataFrame()
    try:
        dir = CRIME_FILES_PATH
        for file in os.listdir(dir):
            absolute_path = os.path.join(dir, file)
            if not file.endswith('.csv'):
                print(f"{file} isn't a csv file")
            elif not os.path.isfile(absolute_path):
                print(f"{absolute_path} isn't a file")
            else:
                curr_df = pd.read_csv(absolute_path)
                if df.empty:
                    df = curr_df
                else:
                    df = pd.concat([df, curr_df])
        return df
    except Exception as error:
        print(error)

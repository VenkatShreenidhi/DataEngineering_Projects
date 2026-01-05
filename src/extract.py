import os 
import pandas as pd 

RAW_DATA_PATH = "Data/RAW/spotify_data.csv"

def extract(file_path: str = RAW_DATA_PATH) -> pd.DataFrame:
    """
    Docstring for extract_csv
    
    :param file_path: Description
    :type file_path: str
    :return: Description
    :rtype: DataFrame

    Extracting raw spotify data from CSV 
    No cleaning or tranformations occurs here 
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path} ")
    
    df = pd.read_csv(file_path)

    print("Extraction successful")
    print(f" rows: {df.shape[0]}")
    print(f" colums: {df.shape[1]}")

    return df 


if __name__ == "__main__":
    df_raw = extract(RAW_DATA_PATH)


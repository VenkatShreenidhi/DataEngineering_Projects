import pandas as pd 
from sqlalchemy import create_engine
import os 
from urllib.parse import quote_plus

PROCESSED_PATH = "Data/processed/spotify_cleaned.csv"

DB_USER = "root"
DB_PASSWORD = quote_plus("365@Partygirl")
DB_HOST = "localhost"
DB_PORT = "3306"
DB_NAME = "spotify_analytics"

TABLE_NAME = "spotify_tracks"

def load_to_mysql():
    try:
        if not os.path.exists(PROCESSED_PATH):
            raise FileNotFoundError("Processed data not found; RUN transform again ")
        
        print("Loading data to MYSQL:")


        df = pd.read_csv(PROCESSED_PATH)

        engine = create_engine(
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

        df.to_sql(
        name=TABLE_NAME,
        con=engine,
        if_exists="replace",   # later you can change to 'append'
        index=False,
        chunksize=1000
    )
        
        print(f" Loaded to SQL {len(df)} records into '{TABLE_NAME}' table")

    except FileNotFoundError as e:
        print("ERROR:", e)
        return 

if __name__ == "__main__":
    load_to_mysql()
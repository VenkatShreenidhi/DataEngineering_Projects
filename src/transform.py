"""
Docstring for transform
To convert the raw dataframe from extraction to a clean, analytics-ready dataset
output would be processed csv file 
"""
from src.extract import extract
import os 
import pandas as pd



PROCESSED_DATA_PATH = "Data/processed/spotify_cleaned.csv"

def transform(df:pd.DataFrame)-> pd.DataFrame:

    #standardise column names 
    df.columns = (df.columns.str.strip().str.lower().str.replace(" ","_"))

    #Drop duplicates 
    df= df.drop_duplicates()

   


    #Handle missing critical fields 
    # if either artist name or track_name is missing drop the row 
    df = df.dropna(subset=["track_name", "artist_name"])
    #handling missing value
    # Missing value for album_name 
    if "album_name" in df.columns:
        df["album_name"] = df["album_name"].fillna("Single / Unknown")
    # Date format needs to be similar 

    if "release_date" in df.columns:
        df["release_date"] = pd.to_datetime(df["release_date"],errors="coerce")
    

    # Convert duration from ms to minutes
    if "duration_ms" in df.columns:
        df["duration_minutes"] = (df["duration_ms"] / 60000).round(2)


    #Popularity bucket -> converting numerical to categorical values for better analysis 

    if "popularity" in df.columns:
        df["popularity"] = pd.to_numeric(df["popularity"], errors="coerce")

        df["popularity_bucket"] = pd.cut(
            df["popularity"], bins=[-1,30,60,100],labels= ["trash","mid","Bop"]

        )

    #extract release year from release_date

    if "release_date" in df.columns:
        df["release_year"] = df["release_date"].dt.year

    
    #anamoly filter 

    if "popularity" in df.columns:
        df = df[(df["popularity"] >= 0) & (df["popularity"] <= 100)]

    if "duration_minutes" in df.columns:
        df = df[df["duration_minutes"] > 0]
    

    return df 


def main():
    df_raw =extract()
    df_cleaned = transform(df_raw)

    os.makedirs("Data/processed", exist_ok=True)
    df_cleaned.to_csv(PROCESSED_DATA_PATH, index=False)

    print("Transformation complete!")
    print(f" Rows after tranformation: {df_cleaned.shape[0]}")


if __name__ == "__main__":
    main()

    





from fastapi import Depends, APIRouter, HTTPException
from typing import List, Optional ## to be used for type hinting
import pandas as pd ## to manipulate the csv


router = APIRouter() ## instance of APIRouter so we can define routes ahead

# Load the CSV file into a DataFrame
df = pd.read_csv('scraped_info.csv')

@router.get("/search/", response_model=List[dict])
async def search_csv(
    name: str
):
    if name is None:
        raise HTTPException(status_code=400, detail="At least one search parameter must be provided")

    # Filter the DataFrame based on the search parameters
    filtered_df = df
    if name:
        filtered_df = filtered_df[filtered_df['name'].str.contains(name, case=False, na=False)]

    # Convert the filtered DataFrame to a list of dictionaries
    results = filtered_df.to_dict(orient='records')

    if not results:
        raise HTTPException(status_code=404, detail="No results found")

    return results

@router.get("/get_cik/", response_model=dict)
async def get_cik(name: str):

    filtered_df = df[df['name'].str.contains(name, case=False, na=False, regex=False)]
    
    if filtered_df.empty:
        raise HTTPException(status_code=404, detail="No company found with that name")
    
    cik_code = filtered_df.iloc[0]['cik']

    return {"name": name, "cik": cik_code}


@router.get("/get_company_info/", response_model=dict) ### get method, return in dictionary form
async def get_company_info(cik: str): ## asynchronous with input in str format

    # Filter the DataFrame by the provided CIK
    filtered_df = df[df['cik'] == cik]
    
    if filtered_df.empty:
        raise HTTPException(status_code=404, detail="No company found with that CIK code")
    
    # Convert the information to a dictionary
    company_info = filtered_df.iloc[0].to_dict() ## return all company information
    
    return company_info
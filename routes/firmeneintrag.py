from fastapi import Depends, APIRouter, HTTPException
from typing import List, Optional
import pandas as pd
router = APIRouter()

# Load the CSV file into a DataFrame
df = pd.read_csv('data.csv')


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

from pydantic import BaseModel


class ProductsInfo(BaseModel):
    userId: str
    role: str
    department: str
    query: str
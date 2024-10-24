from pydantic import BaseModel, EmailStr
from typing import Optional, List


class YML(BaseModel):
    topic: str
    policies: List[str]


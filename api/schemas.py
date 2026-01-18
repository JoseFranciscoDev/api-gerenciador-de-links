from pydantic import BaseModel
from typing import Optional

class LinkCreate(BaseModel):
    url_original: str

    produto: Optional[str] = None
    utm_source: Optional[str] = None
    utm_medium: Optional[str] = None
    tag: Optional[str] = None

 
class LinkResponse(BaseModel):
    slug: str
    short_url: str
    url_final: str
    


from pydantic import BaseModel
from typing import Optional

class LinkCreateSchema(BaseModel):
    url_original: str
    
    campaign: Optional[str] = None
    utm_source: Optional[str] = None
    utm_medium: Optional[str] = None


 
class LinkResponse(BaseModel):
    url_original: str
    url_final: str
    


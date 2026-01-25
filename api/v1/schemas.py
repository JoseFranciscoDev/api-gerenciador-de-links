from pydantic import BaseModel, field_validator
from typing import Optional


class LinkToTrankSchema(BaseModel):
    url_original: str

    campaign: Optional[str] = None
    utm_source: Optional[str] = None
    utm_medium: Optional[str] = None


class LinkResponse(BaseModel):
    url_original: str
    url_final: str


class LinkSaveSchema(BaseModel):
    title: str
    url_original: str
    url_final: str

    @field_validator("title", "url_final", "url_original")
    @classmethod
    def validator_not_whitespace(cls, value):
        if not value.strip():
            raise ValueError("Value cannot be void")
        return value

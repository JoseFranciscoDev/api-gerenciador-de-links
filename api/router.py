from fastapi import APIRouter
from api.database import get_db
from api.schemas import LinkCreateSchema, LinkResponse
from api.url_builders import build_tracked_url
from urllib.parse import urlparse
router = APIRouter(prefix='/links', tags=['links'])

@router.post('/trankear/', response_model=LinkResponse)
def to_trank_link(data: LinkCreateSchema):
    url_original = data.url_original

    params = {
        "campaign": data.campaign,
        "utm_source": data.utm_source,
        "utm_medium": data.utm_medium,
    }

    params = {k: v for k, v in params.items() if v is not None}

    link_tranked = build_tracked_url(url_original, params)
    return {"url_original": url_original, "url_final": link_tranked}    
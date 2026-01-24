from fastapi import APIRouter, Depends, status
from api.database import get_db, Session
from api.v1.schemas import LinkToTrankSchema, LinkResponse, LinkSaveSchema
from api.v1.url_builders import build_tracked_url
from api.models import Link

router = APIRouter(prefix="/v1", tags=["links - v1"])


@router.post(
    "/trankear/",
    response_model=LinkResponse,
)
def to_trank_link(
    data: LinkToTrankSchema,
):
    url_original = data.url_original

    params = {
        "campaign": data.campaign,
        "utm_source": data.utm_source,
        "utm_medium": data.utm_medium,
    }

    params = {k: v for k, v in params.items() if v is not None}

    link_tranked = build_tracked_url(url_original, params)
    return LinkResponse(url_original=url_original, url_final=link_tranked)


@router.post("/sort/")
def sortear_link():
    pass


@router.post("/links", summary="save link", status_code=status.HTTP_201_CREATED)
def save_link(
    data: LinkSaveSchema,
    session: Session = Depends(get_db),
):
    try:
        new_link = Link(
            title=data.title, url_final=data.url_final, url_original=data.url_original
        )
        session.add(new_link)
        session.commit()
    except Exception as error:
        print(error)


@router.get("/links")
def get_all_links(session: Session = Depends(get_db)):
    links = session.query(Link).all()
    return links

from api.database import Base
from sqlalchemy import String, Integer, Boolean, DateTime, func
from sqlalchemy.orm import mapped_column, Mapped
from datetime import datetime

class Link(Base):
    __tablename__ = 'links'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    url_final: Mapped[str] = mapped_column(String, nullable=False)
    url_original: Mapped[str] = mapped_column(String)
    produto: Mapped[str] = mapped_column(String)
    utm_source: Mapped[str] = mapped_column(String)
    utm_medium: Mapped[str] = mapped_column(String)
    tag_sck: Mapped[str] = mapped_column(String)
    create_at: Mapped[datetime] = mapped_column(DateTime, default=func.now()) # CURRENT TIMESTAMP
    deleted:Mapped[bool] = mapped_column(Boolean, default=False)


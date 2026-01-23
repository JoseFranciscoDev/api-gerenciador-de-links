from api.database import Base
from sqlalchemy import String, Integer, Boolean, DateTime, func
from sqlalchemy.orm import mapped_column, Mapped
from datetime import datetime

class Link(Base):
    __tablename__ = 'links'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    url_final: Mapped[str] = mapped_column(String, nullable=False)
    url_original: Mapped[str] = mapped_column(String)
    campaign: Mapped[str] = mapped_column(String(30))
    utm_source: Mapped[str] = mapped_column(String(30))
    utm_medium: Mapped[str] = mapped_column(String(30))
    create_at: Mapped[datetime] = mapped_column(DateTime, default=func.now()) # CURRENT TIMESTAMP
    deleted:Mapped[bool] = mapped_column(Boolean, default=False)


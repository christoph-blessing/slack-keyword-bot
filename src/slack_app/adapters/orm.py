from sqlalchemy import Boolean, Column, Integer, String, Table
from sqlalchemy.orm import registry

from ..domain.model import Keyword

mapper_registry = registry()
metadata = mapper_registry.metadata

keyword = Table(
    "keyword",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("channel_name", String(255)),
    Column("subscriber", String(255)),
    Column("word", String(255)),
    Column("active", Boolean),
)


def start_mappers() -> None:
    mapper_registry.map_imperatively(Keyword, keyword)

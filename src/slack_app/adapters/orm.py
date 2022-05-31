from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import registry, relationship

from ..domain.model import Channel, Subscription

mapper_registry = registry()
metadata = mapper_registry.metadata

channel = Table("channel", metadata, Column("channel_name", String(255), primary_key=True))

subscription = Table(
    "subscription",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("channel_name", ForeignKey("channel.channel_name")),
    Column("subscriber", String(255)),
    Column("word", String(255)),
    Column("unsubscribed", Boolean),
)


def start_mappers() -> None:
    mapper_registry.map_imperatively(Subscription, subscription)
    mapper_registry.map_imperatively(
        Channel, channel, properties={"subscriptions": relationship(Subscription, collection_class=set)}
    )

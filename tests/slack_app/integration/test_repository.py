from sqlalchemy.orm import Session

from slack_app.adapters.repository import SQLAlchemyRepository
from slack_app.domain.model import Channel

from ..conftest import KeywordCreator


def test_can_add_keyword(session: Session, create_keyword: KeywordCreator) -> None:
    repo = SQLAlchemyRepository(session)
    repo.add(create_keyword(channel="general", subscriber="bob", word="hello"))
    session.commit()
    rows = list(session.execute("SELECT channel, subscriber, word FROM keyword"))
    assert rows == [("general", "bob", "hello")]


def test_can_get_keyword(session: Session, create_keyword: KeywordCreator) -> None:
    session.execute("INSERT INTO keyword (channel, subscriber, word) VALUES ('general', 'bob', 'hello')")
    repo = SQLAlchemyRepository(session)
    keywords = repo.get(channel=Channel("general"))
    assert keywords == [create_keyword(channel="general", subscriber="bob", word="hello")]
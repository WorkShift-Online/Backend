from db import Visits
from pony import orm
from datetime import datetime


@orm.db_session
def test_pos_create_new_visit():
    v = Visits(
        ipv4='001.112.211.100',
        ua='Некоторая информация о браузере пользователя',
        channel='WEB',
        started_at=datetime.utcnow()
    )


@orm.db_session
def test_pos_getting_visit_by_id():
    v = Visits['04acc87d-f3cb-4f58-aaa3-e2a688cca0fb']
    assert v.ipv4 == '001.112.211.100'

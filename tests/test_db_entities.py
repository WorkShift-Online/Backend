from db import Visits, orm, datetime


@orm.db_session
def test_pos_create_new_visit():
    v = Visits(
        ipv4='001.112.211.100',
        ua='Некоторая информация о браузере пользователя',
        channel='WEB',
        started_at=datetime.utcnow(),
        auth=False
    )


@orm.db_session
def test_pos_getting_visit_by_id():
    v = Visits['4317b110-b1b0-4e4f-b88c-cb42f8301e49']
    assert v.ipv4 == '001.112.211.100'

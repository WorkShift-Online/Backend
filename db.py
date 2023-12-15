from json import load
from pony import orm
from uuid import UUID
from datetime import datetime

secret = load(
    open(
        file=r'C:\Users\mx\Desktop\WorkShift Backend\.secret.json',
        encoding='utf-8'
    )
)

settings = dict(
    provider='postgres',
    user=secret['dbUser'],
    password=secret['dbPassword'],
    host=secret['dbHost'],
    database=secret['dbDatabase']
)

db = orm.Database(**settings)


class Visits(db.Entity):
    id = orm.PrimaryKey(UUID, auto=True)
    created_at = orm.Required(datetime, default=lambda: datetime.utcnow())
    updated_at = orm.Optional(datetime)
    deleted_at = orm.Optional(datetime)
    ipv4 = orm.Required(str, 15)
    ua = orm.Required(orm.LongStr)
    channel = orm.Required(str, 15)
    started_at = orm.Required(datetime)
    ended_at = orm.Optional(datetime)
    auth = orm.Required(bool, default=False)
    user_id = orm.Optional(UUID)
    raw_phone = orm.Optional(str, 18)


db.generate_mapping(create_tables=True)

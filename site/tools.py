from datetime import datetime
import pytz

def get_date() -> datetime:
    return datetime.now(tz=pytz.timezone('Europe/Moscow'))

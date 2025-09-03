from datetime import datetime


def add(moment: datetime.date) -> datetime.date:
    G = 1_000_000_000

    ts = datetime.timestamp(moment)
    return datetime.fromtimestamp(ts + G)

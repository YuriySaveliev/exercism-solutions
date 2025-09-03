from datetime import datetime, timedelta


def add(moment: datetime.date) -> datetime.date:
    GIGASECOND = 10 ** 9
    
    return moment + timedelta(seconds=GIGASECOND)

from datetime import datetime, timezone


# для удобства тестирования
def current_datetime():
    return datetime.now(timezone.utc)


def start_timestamp(period: str) -> int:
    if period == "all":
        return 0

    # now = current_timestamp()
    if period == "month":
        dt = current_datetime()
        dt = dt.replace(month=dt.month - 1)
        return dt.timestamp()
    if period == "year":
        dt = current_datetime()
        dt = dt.replace(year=dt.year - 1)
        return dt.timestamp()

    return 0

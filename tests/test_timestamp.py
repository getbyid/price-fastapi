from datetime import datetime
from app import utils


def mock_datetime():
    return datetime.fromisoformat("2021-10-10T00:00:00")


def test_month_period(monkeypatch):
    monkeypatch.setattr(utils, "current_datetime", mock_datetime)
    ts = utils.start_timestamp("month")
    dt = datetime.fromtimestamp(ts)
    assert dt.isoformat() == "2021-09-10T00:00:00"


def test_year_period(monkeypatch):
    monkeypatch.setattr(utils, "current_datetime", mock_datetime)
    ts = utils.start_timestamp("year")
    dt = datetime.fromtimestamp(ts)
    assert dt.isoformat() == "2020-10-10T00:00:00"


def test_all_period():
    ts = utils.start_timestamp("all")
    assert ts == 0


def test_empty_period():
    ts = utils.start_timestamp("")
    assert ts == 0

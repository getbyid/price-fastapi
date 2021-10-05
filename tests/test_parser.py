import pytest
from app.parsers.schema_org import SchemaOrgParser
from app.parsers.dns_shop import DnsShopParser


@pytest.mark.sample_html("wb--GTX1660.txt")
def test_schema_org_parser(load_html):
    parser = SchemaOrgParser()
    parser.html = load_html
    result = parser.parse_html()
    assert result == {
        "price": 51690,
        "currency": "RUB",
        "availability": 1,
    }


@pytest.mark.sample_html("dns_shop--GTX1660.txt")
def test_dns_shop_parser(load_html):
    parser = DnsShopParser()
    parser.html = load_html
    result = parser.parse_html()
    assert result == {
        "price": 42999,
        "code": "1347836",
        "guid": "38d7d1eb-43d7-11e9-a206-00155d03332b",
    }

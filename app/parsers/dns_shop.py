import json
from app.parsers.base_parser import BaseParser


class DnsShopParser(BaseParser):
    allowed_url = "https://www.dns-shop.ru/product/"

    cut_from = "window['MainSwWrapper'].sendProductMessage("
    cut_to = "));</script>"

    def parse_html(self):
        start = self.html.find(self.cut_from)
        if start < 0:
            raise Exception("start position not found")

        start += len(self.cut_from)

        end = self.html.find(self.cut_to, start)
        if end < start:
            raise Exception("end position not found")

        str = self.html[start:end]
        # print(str)

        data = json.loads(str)
        # print(data)

        return {
            "price": int(data["price"]),
            "code": data["code"],
            "guid": data["guid"],
        }

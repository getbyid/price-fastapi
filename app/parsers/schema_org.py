from lxml import etree
from app.parsers.base_parser import BaseParser


class SchemaOrgParser(BaseParser):
    sel_product = 'div[itemtype="http://schema.org/Product"]'
    sel_offer = 'div[itemtype="http://schema.org/Offer"]'
    sel_price = 'meta[itemprop="price"]'
    sel_currency = 'meta[itemprop="priceCurrency"]'
    sel_availability = 'link[itemprop="availability"]'

    href_instock = "http://schema.org/InStock"

    def parse_html(self):
        parser = etree.HTMLParser()
        document = etree.fromstring(self.html, parser)

        product_el = document.cssselect(self.sel_product)[0]
        offer_el = product_el.cssselect(self.sel_offer)[0]

        price = offer_el.cssselect(self.sel_price)[0].get("content")
        currency = offer_el.cssselect(self.sel_currency)[0].get("content")
        href = offer_el.cssselect(self.sel_availability)[0].get("href")

        return {
            "price": int(float(price)),
            "currency": currency,
            "availability": 1 if href == self.href_instock else 0,
        }

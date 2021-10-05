import asyncio
import time
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Offer, History
from app.parsers.schema_org import SchemaOrgParser
from app.parsers.dns_shop import DnsShopParser


class Updater:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def update_all(self):
        result = await self.session.execute(select(Offer))
        offers = result.scalars().all()
        print(f"Offers: {offers}")

        updated = await asyncio.gather(
            *[self._update_offer(offer.id, offer.url) for offer in offers]
        )

        return {
            "total": len(offers),
            "updated": sum(updated),
        }

    async def _update_offer(self, id, url: str) -> int:
        print(f"Offer {id}: {url}")

        parser = self._select_parser(url)
        try:
            data = await parser.parse(url)
        except Exception as e:
            print(f"Offer {id}: {e}")
            parser.dump_html(id)
            return 0

        record = History(
            offer_id=id,
            datetime=int(time.time()),
            availability=data.get("availability", 1),
            price=data.get("price", 0),
            price_currency=data.get("currency", "RUB"),
        )
        self.session.add(record)
        return 1

    def _select_parser(self, url: str):
        if DnsShopParser.accepts_url(url):
            return DnsShopParser()
        else:
            return SchemaOrgParser()

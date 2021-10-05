import httpx
from pathlib import Path
from time import strftime


class BaseParser:
    allowed_url = ""
    html = ""

    # https://techblog.willshouse.com/2012/01/03/most-common-user-agents/
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "Dnt": "1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    }

    async def parse(self, url: str):
        if not self.accepts_url(url):
            raise Exception("not allowed URL")

        await self.download_page(url)
        return self.parse_html()

    @classmethod
    def accepts_url(cls, url: str):
        return len(cls.allowed_url) == 0 or url.startswith(cls.allowed_url)

    async def download_page(self, url: str):
        async with httpx.AsyncClient(headers=self.headers) as client:
            resp = await client.get(url)
            print(resp)
            self.html = resp.text

    def parse_html(self):
        raise NotImplementedError()

    def dump_html(self, id):
        ts = strftime("%Y-%m-%d-%H-%M-%S")
        p = Path(__file__).parent.parent.parent.joinpath("dumps", f"{id}_{ts}.txt")
        p.write_text(self.html)

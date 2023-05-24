import asyncio
import tornado

import json
from dataclasses import dataclass, asdict

from datetime import datetime


class TimeHandler(tornado.web.RequestHandler):
    async def get(self):
        hour = datetime.now().hour
        if 0 <= hour < 12:
            time = "morning"
        elif 12 <= hour < 18:
            time = "afternoon"
        else:
            time = "evening"
        self.write(json.dumps(asdict(Time(time))))


@dataclass
class Time():
    timeOfDay: str



async def main():
    app = tornado.web.Application([
        (r"/time", TimeHandler)
    ])
    app.listen(8443)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
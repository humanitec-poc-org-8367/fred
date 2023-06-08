import asyncio
import logging
import tornado

import json
from dataclasses import dataclass, asdict

from datetime import datetime

logging.basicConfig(level=logging.INFO)

consumers = set(());

class TimeHandler(tornado.web.RequestHandler):
    async def get(self):
        logging.info('called static endpoint')
        time = "epoch"
        self.write(json.dumps(asdict(Time(time))))

class ResourceTimeHandler(tornado.web.RequestHandler):
    async def get(self, resourceId):
        logging.info('called dynamic endpoint with resId:' + resourceId)
        hour = datetime.now().hour
        if 0 <= hour < 12:
            time = "morning"
        elif 12 <= hour < 18:
            time = "afternoon"
        else:
            time = "evening"
        self.write(json.dumps(asdict(Time(time))))

class ConsumerHandler(tornado.web.RequestHandler):
    
    async def put(self, resourceId):
        logging.info('called add consumer: ' + resourceId)
        consumers.add(resourceId)
        logging.info(consumers);

        self.set_status(204);  

    async def delete(self, resourceId):
        logging.info('called delete consumer: ' + resourceId)
        consumers.discard(resourceId)
        logging.info(consumers);
        self.set_status(204)


class ConsumersHandler(tornado.web.RequestHandler):
    async def get(self):
        logging.info('called GET consumers')
        logging.info(consumers)
        self.write(json.dumps(list(consumers)));  

@dataclass
class Time():
    timeOfDay: str


async def main():
    app = tornado.web.Application([
        (r"/static/time", TimeHandler),
        (r"/(.*)/time", ResourceTimeHandler),
        (r"/consumers", ConsumersHandler),
        (r"/consumers/(.*)", ConsumerHandler),


    ])
    app.listen(8443)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
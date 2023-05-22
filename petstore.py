import asyncio
import tornado


class MainHandler(tornado.web.RequestHandler):
    async def get(self):
        self.write("Hello, World")


async def main():
    app = tornado.web.Application([
        (r"/", MainHandler)
    ])
    app.listen(8443)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
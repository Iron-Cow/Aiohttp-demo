import aiohttp
import argparse


from demo import create_app

import asyncio

try:
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
    print("Library uvloop is not available (Probably due to Windows")


parser = argparse.ArgumentParser(description='Demo Project')
parser.add_argument('--host', help="Host to lister", default="0.0.0.0")
parser.add_argument('--port', help="Port to accept connection", default=5000)
parser.add_argument('--reload', action='store_true', help="Autoreload code on change")

args = parser.parse_args()

app = create_app()

if args.reload:
    print('Start code with reload')
    import aioreloader
    aioreloader.start()


if __name__ == '__main__':
    aiohttp.web.run_app(app, host=args.host, port=args.port)

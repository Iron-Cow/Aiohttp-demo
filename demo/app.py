import aiohttp_jinja2
import jinja2
from aiohttp import web
import asyncpgsa
from .routes import setup_routes


def create_app(config: dict) -> web.Application:
    app = web.Application()
    app['config'] = config
    setup_routes(app)
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.PackageLoader('demo', 'templates')
     )
    app.on_startup.append(on_start)
    app.on_cleanup.append(on_shutdown)
    return app


async def on_start(app):
    config = app['config']
    app['db'] = await asyncpgsa.create_pool(dsn=config['database_uri'])

async def on_shutdown(app):
    await app['db'].close()

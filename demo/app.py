import aiohttp_jinja2
import jinja2
from aiohttp import web
from .routes import setup_routes


def create_app() -> web.Application:
    app = web.Application()
    setup_routes(app)
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.PackageLoader('demo', 'templates')
     )
    return app
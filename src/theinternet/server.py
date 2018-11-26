import asyncio
import os
import sys
import idna
from collections import defaultdict
from uuid import uuid4

from atum import GET, POST

from quart import Quart, websocket, session, abort, request
from .templates import home

if getattr(sys, 'frozen', False):
    # running as a frozen binary
    app = Quart(__name__,
                static_folder=None,
                )


    @app.route('/static/<path:filename>')
    async def static(filename):
        from .frozen_static import get_static_file
        try:
            return get_static_file(filename)
        except FileNotFoundError:
            raise abort(404)

else:
    # running from source
    app = Quart(__name__,
                static_folder=os.path.join(
                    os.path.dirname(os.path.abspath(__file__)),
                    'static'),
                static_url_path='/static',
                )

app.secret_key = os.getenv('SECRET_KEY', uuid4().hex)
counter = defaultdict()


@app.route('/')
async def hello():
    try:
        hostname = request.headers['X-Forwarded-Host']
    except KeyError:
        try:
            hostname = request.headers['Host']
            if hostname.startswith('127.') or hostname == 'localhost':
                hostname = 'local-user.theinternet.lol'
        except KeyError:
            hostname = 'unknown.theinternet.lol'

    name = hostname.split('.')[0].replace('-', ' ')
    try:
        name = idna.decode(name)
    except:
        pass
    return home.render(name=name.title())

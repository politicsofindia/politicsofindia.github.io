from aiohttp import web
import aiohttp_jinja2
import jinja2
import asyncio
from db import init_db, add_user
import os

routes = web.RouteTableDef()

@routes.get('/')
async def signup_form(request):
    return aiohttp_jinja2.render_template('signup.html', request, {})

@routes.post('/')
async def signup(request):
    data = await request.post()
    email = data['email']
    password = data['password']
    await add_user(email, password)
    return web.Response(text="Sign up successful")

async def init_app():
    app = web.Application()
    app.add_routes(routes)
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('.'))
    await init_db()
    return app

app = asyncio.get_event_loop().run_until_complete(init_app())

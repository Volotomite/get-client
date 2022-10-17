import os
import json

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root(request: Request):
    host = request.client.host
    port = request.client.port

    name = str(host)
    full_path = './data/' + name
    if not os.path.exists(full_path):
        with open(full_path, 'w') as f:
            f.write(str(port))

    return templates.TemplateResponse("index.html", {"request":request, "host": host, "port": port})


@app.post("/fetch/")
async def fetch(request: Request):
    data = await request.json()
    host = data['ip']
    name = str(host)
    full_path = './data/' + name
    with open(full_path, "a") as f:
         f.write(json.dumps(data))
         f.write('\n\n\n\n\n')

    return None

def log_entry():
    pass

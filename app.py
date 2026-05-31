from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request


from workflows.coding_workflow import run_agentic_workflow

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)

async def home(request:Request):
    return templates.TemplateResponse(
        "index.html",
        {"request" : request}

    )

@app.post("/chat")
async def chat(query : dict):

    user_message = query["message"]

    response = run_agentic_workflow(user_message)

    return {"response" : response}
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/medinote/ap")
async def process_input(request: Request):
    body = await request.body()
    text = body.decode("utf-8").strip()
    if text.startswith("HOOP ["):
        return {"ap_entries": ["1. Sample diagnostic output from HOOP [] input."]}
    return JSONResponse(status_code=400, content={"error": "Input must start with HOOP ["})

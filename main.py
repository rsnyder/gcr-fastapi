from fastapi import FastAPI

app = FastAPI()
from starlette.responses import RedirectResponse

@app.get('/')
async def root():
  return RedirectResponse(url='/docs')

@app.get('/some-endpoint')
async def some_endpoint(url: str):
    return {'endpoint': 'some-endpoint'}
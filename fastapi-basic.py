import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

class Details(BaseModel):
    f_name: str
    l_name: str
    phone_number: int


app = FastAPI()


@app.get('/')
def index():
    return {'message': "This is the home page of this API. Go to /apiv1/<name> or /apiv2/?name=<string>"}


@app.get('/apiv1/{name}')
def api1(name: str):
    return {'message': f'Hello! @{name}'}


@app.get('/apiv2/')
def api2(name: str):
    return {'message': f'Hello! @{name}'}

@app.post('/apiv3/')
def api3(data: Details):
    return {'message': data}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=4000, debug=True)

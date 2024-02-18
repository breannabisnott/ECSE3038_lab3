from fastapi import FastAPI, Request, Response, status
import uuid

app = FastAPI()

tanks = []

@app.get("/tank")
def get_tank():
    return tanks

@app.get("/tank/{id}")
def get_tank_id():
    tank_index = 0
    for i in range(len(tanks)):
        if tanks[i]["id"] == id:
            tank_index = i

    return(tanks[tank_index])

@app.post("/tank")
async def post_tank(request: Request, response: Response):   
    tank = await request.json()

    new_uuid = uuid.uuid4()

    tank = {"id": str(new_uuid), **tank}

    tanks.append(tank)
    response.status_code = status.HTTP_201_CREATED

    return(tank)

@app.patch("/tank/{id}")
async def patch_tank(id: int, request:Request):
    patched_tank = await request.json()

    for i, tank in enumerate(tanks):
        if tank["id"] == id:
            tanks[i] = {**tank, **patched_tank}
            return tank[i]
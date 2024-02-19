from fastapi import FastAPI, Request, Response, status, HTTPException
import uuid

app = FastAPI()

tanks = []

@app.get("/tank")
def get_tank():
    return tanks

@app.get("/tank/{id}")
def get_tank_id(id: str):
    for i in range(len(tanks)):
        if tanks[i]["id"] == id:
            return(tanks[i])
    
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/tank")
async def post_tank(request: Request, response: Response):   
    tank = await request.json()

    new_uuid = uuid.uuid4()

    id = str(new_uuid)
    tank = {"id": id, **tank}

    tanks.append(tank)
    response.status_code = status.HTTP_201_CREATED

    return(tank)

@app.patch("/tank/{id}")
async def patch_tank(id: str, request:Request, response: Response):
    patched_tank = await request.json()

    for x in list(patched_tank.keys()):
        if x == "id":
            raise HTTPException(status_code=400, detail="Unable to edit ID")

    for i, tank in enumerate(tanks):
        if tank["id"] == id:
            tanks[i] = {**tank, **patched_tank}
            response.status_code = status.HTTP_200_OK
            return tanks[i]
        
    raise HTTPException(status_code=404, detail="Item not found")
        
@app.delete("/tank/{id}")
def delete_tank(id: str, response: Response):

    for i in range(len(tanks)):
        if tanks[i]["id"] == id:
            del tanks[i]
            response.status_code = status.HTTP_204_NO_CONTENT
            return()
    
    raise HTTPException(status_code=404, detail="Item not found")    
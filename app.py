from fastapi import FastAPI, Request

app = FastAPI()

tanks = [
    {
        "id": 1,
        "location": "Engineering department",
        "lat": "18.0051862",
        "long": "-76.7505108",
    },

    {
        "id": 2,
        "location": "Engineering department",
        "lat": "18.0051862",
        "long": "-76.7505108",
    }
]

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
async def post_tank(request: Request):   
    tank = await request.json()

    tank = {"id": len(tanks) + 1, **tank}

    tanks.append(tank)

    return(tank)
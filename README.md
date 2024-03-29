# Breanna Bisnott ECSE3038 Lab 3 Submission

### Two Truths & a Lie
- I've flown a plane
- My 5K PB is 28:22
- I love ackee

The purpose of this code is for a lab assignment on building POST request handlers with FastAPI :D

## `get_tank()`
This route returns a list of 0 or more objects. If a POST request was successfully made to the /tank route previously, the GET route should return an array of the POSTed tank object.

## `get_tank_id()`
This route returns a single JSON object of tank that is associated with the id passed as input in the route. If the API is unable to locate the object that has the id specified, the API  responds with an appropriate response message and status code.

## `post_tank()`
This route accepts a JSON object structured as depicted below. On success, the web application responds with the same JSON object that was posted with the addition of an `id` attribute. This `id` is to be generated by the API. 

The route also returns a status code that indicates that an object was **successfully created**.

## `patch_tank()`
The server allows a client to alter the parts of one of the tanks after it has been POSTed. The server allows the requester to make a JSON body with any combination of the three attributes and update them as necessary (The client is NOT allowed to edit the `id` attribute). 

The route also returns a status code that indicates that an object was **successfully altered**.

If the API is unable to locate the object that has the id specified, the API responds with an appropriate response message and status code.

## `delete_tank()`
The web application allows the client to delete any previously POSTed object. The web application does not send back any message to the client once the objects have been deleted. There is, however, a suitable status code that indicates **success** and that an **empty response is sent**.

If the API is unable to locate the object that has the id specified, the API responds with an appropriate response message and status code.

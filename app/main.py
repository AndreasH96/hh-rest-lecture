from fastapi import FastAPI,HTTPException, Response, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from dotenv import load_dotenv
import os

class UserSchema(BaseModel):
    name:str
    age :int
    company:str

load_dotenv()
port = int(os.getenv('PORT')) if  os.getenv('PORT') else 8000
db = {}
application = FastAPI()
application.mount("/static", StaticFiles(directory="static"), name="static")

origins = ["*"]

@application.on_event("startup")
async def startup():
    application.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )



templates = Jinja2Templates(directory="static")


@application.get("/",response_class=HTMLResponse)
def homePath(request:Request):
    return templates.TemplateResponse("index.html",{"request":request,"users":db})


@application.get("/users")
def getUserIds():
    return list(db.keys())

@application.get("/users/{uid}")
def getUser(uid:str):
    if(not uid.lower() in db.keys()):
        raise HTTPException(status_code=404, detail="Item not found")
    
    user = db.get(uid.lower())
    return user

@application.post("/users",status_code=201)
def addUser(user: UserSchema):
    
    #Since we validated the body, we know that user.name is a string at all times
    db[user.name.lower()] = user

    return "Success"


@application.put("/users",status_code=200)
def updateUser(user: UserSchema,response:Response):
    uid = user.name
    if (not uid.lower() in db.keys()):
        response.status_code=201

    # We can perform same operation as in the POST request
    addUser(user)
    return "Success"

@application.delete("/users/{uid}")
def deleteUser(uid:str):
    if(not uid.lower() in db.keys()):
        return "User not found",404
    db.pop(uid.lower())
    return "Success", 200

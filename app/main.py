from fastapi import FastAPI,HTTPException, Response
from pydantic import BaseModel
from dotenv import load_dotenv
import os


class UserSchema(BaseModel):
    name:str
    age :int
    company:str

load_dotenv()
port = os.getenv('PORT') if  os.getenv('PORT') else 5000
db = {}
application = FastAPI()


@application.get("/")
def getUserIds():
    return list(db.keys())

@application.get("/{uid}")
def getUser(uid:str):
    if(not uid.lower() in db.keys()):
        raise HTTPException(status_code=404, detail="Item not found")
    
    user = db.get(uid.lower())
    return user

@application.post("/",status_code=201)
def addUser(user: UserSchema):
    #Since we validated the body, we know that user.name is a string at all times
    db[user.name.lower()] = user

    return "Success"


@application.put("/{uid}",status_code=200)
def updateUser(uid:str,user: UserSchema,response:Response):

    if (not uid.lower() in db.keys()):
        response.status_code=201

    # We can perform same operation as in the POST request
    addUser(user)
    return "Success"

@application.delete("/{uid}")
def deleteUser(uid:str):
    if(not uid.lower() in db.keys()):
        return "User not found",404
    db.pop(uid.lower())
    return "Success", 200

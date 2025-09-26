from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mysql import connector
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_headers = ["*"],
    allow_methods = ["*"]
)


@app.get("/m1")
def response1():
    return("HELLO BRO")
@app.get("/")
def response11():
    return("WELCOME BUDDY")
@app.get("/about")
def response111():
    return("THE LEADING TECH COMAPANY WEBPRIME.TOP")
@app.get("/contact")
def response1111():
    return("support@webprime.top")
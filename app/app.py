from fastapi import FastAPI

app=FastAPI()

@app.get("/helloworld")
def helowrold():
    return{"message":"hellowrold"}




from fastapi import fastapi

app=fastapi()

@app.get("/helloworld")
def helowrold():
    return{"message":"hellowrold"}




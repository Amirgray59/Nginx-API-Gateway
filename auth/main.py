from fastapi import FastAPI 


app = FastAPI() 


@app.get("/")
def root() : 
    return {"service" : "auth"}

@app.get("/health")
def health() : 
    return {"status" : "ok"}



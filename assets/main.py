from fastapi import FastAPI


app =FastAPI() 

@app.get("/")
def root():
    return {"service": "notes"}

@app.get("/health")
def health():
    return {"status": "ok"}

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Maintenance API is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}
from fastapi import FastAPI

app = FastAPI(title="API Resilience Fork")

@app.get("/health")
def health():
    return {"status": "ok"}

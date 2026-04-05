from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="PCE API - Full Mode")

class InputData(BaseModel):
    value: float

def pce_layer(value):
    if value < 0.2:
        return "VALID"
    elif value < 0.5:
        return "SUSPEND"
    elif value < 0.8:
        return "CRITICAL"
    else:
        return "REJECT"

def ois_layer(value):
    return {
        "dG": round(value, 3),
        "trajectory": "stable" if value < 0.5 else "divergent"
    }

def sel_layer(value):
    return {
        "compression": round(1 - value, 3),
        "entropy_level": "LOW" if value < 0.3 else "MEDIUM" if value < 0.7 else "HIGH"
    }

@app.get("/")
def root():
    return {"message": "PCE API Running (Full Mode)"}

@app.post("/validate")
def validate(data: InputData):
    value = data.value

    status = pce_layer(value)
    ois = ois_layer(value)
    sel = sel_layer(value)

    return {
        "status": status,
        "stability": status,
        "identity": ois,
        "entropy": sel
    }
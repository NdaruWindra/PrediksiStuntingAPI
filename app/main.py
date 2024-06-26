from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.model.model import predict_stunting

app = FastAPI()

class PredictionRequest(BaseModel):
    umur: int
    jenis_kelamin: str
    tinggi_badan: float

@app.get('/')
def index():
    return {"message": "Welcome to the stunting prediction API!"}

@app.post('/predict')
async def predict(data: PredictionRequest):
    umur = data.umur
    jenis_kelamin = 1 if data.jenis_kelamin.lower() == 'laki-laki' else 0
    tinggi_badan = data.tinggi_badan

    prediction_result = predict_stunting(umur, jenis_kelamin, tinggi_badan)
    if 'error' in prediction_result:
        raise HTTPException(status_code=400, detail=prediction_result['error'])

    return prediction_result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=80)

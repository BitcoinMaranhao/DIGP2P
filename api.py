from fastapi import FastAPI
from pydantic import BaseModel

from main import var_valor

app = FastAPI()


@app.get("/V1/API/calc_btc", 
          tags=["BTC"],
          summary="Valor satoshis",
          description="Retorna dados de sats com base em um falor fiat")
async def calcular_btc(value:float):
    resultado = await var_valor(value)
    if resultado:
        return resultado
    return {"error": "Erro ao calcular resposta BTC"}
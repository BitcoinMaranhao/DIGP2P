from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict

from main import var_valor,var_valor_usdt

app = FastAPI()
# Definindo o modelo para o corpo da requisição
class ValueRequest(BaseModel):
    amountInCents: float

@app.post("/V1/API/calc_btc", 
          tags=["BTC"],
          summary="Valor satoshis",
          description="Retorna dados de sats com base em um falor fiat")
async def calcular_btc(value: ValueRequest):
    # Acessando o valor do JSON enviado
    resultado = await var_valor(value.amountInCents)
    
    if resultado:
        return resultado
    
    return {"error": "Erro ao calcular resposta BTC"}

@app.post("/V1/API/calc_usdt", 
          tags=["USDT"],
          summary="Valor USDT",
          description="Retorna dados de usdt com base em um falor fiat")
async def calcular_usdt(value: ValueRequest):
    # Acessando o valor do JSON enviado
    resultado = await var_valor_usdt(value.amountInCents)
    
    if resultado:
        return resultado
    
    return {"error": "Erro ao calcular resposta BTC"}
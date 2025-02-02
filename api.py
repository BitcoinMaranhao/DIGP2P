from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict

from main import buy_usdt, buy_btc, sell_btc, sell_usdt

app = FastAPI()
# Definindo o modelo para o corpo da requisição
class ValueRequest(BaseModel):
    amountInCents: float

@app.get("/V1/API/calc_btc", 
          tags=["BTC"],
          summary="Valor satoshis",
          description="Retorna dados de sats com base em um falor fiat")
async def calcular_btc(value: ValueRequest):
    # Acessando o valor do JSON enviado
    resultado = await buy_btc(value.amountInCents)
    
    if resultado:
        return resultado
    
    return {"error": "Erro ao calcular resposta BTC"}

@app.get("/V1/API/calc_usdt", 
          tags=["USDT"],
          summary="Valor USDT",
          description="Retorna dados de usdt com base em um falor fiat")
async def calcular_usdt(value: ValueRequest):
    # Acessando o valor do JSON enviado
    resultado = await buy_usdt(value.amountInCents)
    
    if resultado:
        return resultado
    
    return {"error": "Erro ao calcular resposta BTC"}


@app.get("/V1/API/calc_sell_btc", 
          tags=["BTC"],
          summary="Valor satoshis",
          description="Retorna dados de sats com base em um falor fiat")
async def calcular_btc(value: ValueRequest):
    # Acessando o valor do JSON enviado
    resultado = await sell_btc(value.amountInCents)
    
    if resultado:
        return resultado
    
    return {"error": "Erro ao calcular resposta BTC"}

@app.get("/V1/API/calc_sell_usdt", 
          tags=["USDT"],
          summary="Valor USDT",
          description="Retorna dados de usdt com base em um falor fiat")
async def calcular_usdt(value: ValueRequest):
    # Acessando o valor do JSON enviado
    resultado = await sell_usdt(value.amountInCents)
    
    if resultado:
        return resultado
    
    return {"error": "Erro ao calcular resposta BTC"}
from fastapi import FastAPI
from pydantic import BaseModel

from main import buy_usdt, buy_btc, sell_btc, sell_usdt, buy_btc_digpix

app = FastAPI()

class ValueRequest(BaseModel):
    amount: float  # Valor em reais, aceita centavos (ex.: 100.50 para R$ 100,50)

@app.post("/V1/API/calc_btc",
          tags=["BTC"],
          summary="Valor em BTC",
          description="Retorna dados de BTC com base em um valor fiat")
async def calcular_btc(value: ValueRequest):
    resultado = await buy_btc(value.amount)  # Valor em reais
    if resultado:
        return resultado
    return {"error": "Erro ao calcular resposta BTC"}

@app.post("/V1/API/calc_usdt",
          tags=["USDT"],
          summary="Valor em USDT",
          description="Retorna dados de USDT com base em um valor fiat")
async def calcular_usdt(value: ValueRequest):
    resultado = await buy_usdt(value.amount)  # Valor em reais
    if resultado:
        return resultado
    return {"error": "Erro ao calcular resposta USDT"}

@app.post("/V1/API/calc_sell_btc",
          tags=["BTC"],
          summary="Valor venda BTC",
          description="Retorna dados de venda de BTC com base em um valor fiat")
async def calcular_sell_btc(value: ValueRequest):
    resultado = await sell_btc(value.amount)  # Valor em reais
    if resultado:
        return resultado
    return {"error": "Erro ao calcular resposta BTC"}

@app.post("/V1/API/calc_sell_usdt",
          tags=["USDT"],
          summary="Valor venda USDT",
          description="Retorna dados de venda de USDT com base em um valor fiat")
async def calcular_sell_usdt(value: ValueRequest):
    resultado = await sell_usdt(value.amount)  # Valor em reais
    if resultado:
        return resultado
    return {"error": "Erro ao calcular resposta USDT"}

@app.post("/V1/API/calc_sats",
          tags=["BTC"],
          summary="Valor em satoshis",
          description="Converte um valor em BRL para satoshis com base na cotação do BTC")
async def calcular_sats(value: ValueRequest):
    resultado = await buy_btc(value.amount)  # Valor em reais
    if "quantidade" in resultado:
        sats = int(resultado["quantidade"] * 100_000_000)  # Converte BTC para satoshis
        return {"satoshis": sats}
    return {"error": "Erro ao calcular satoshis"}

@app.post("/V1/API/calc_sats_digpix",
          tags=["BTC"],
          summary="Valor em satoshis com taxa Digpix",
          description="Converte um valor em BRL para satoshis com taxa fixa de 4%")
async def calcular_sats_digpix(value: ValueRequest):
    resultado = await buy_btc_digpix(value.amount)  # Valor em reais
    if "quantidade" in resultado:
        sats = int(resultado["quantidade"] * 100_000_000)  # Converte BTC para satoshis
        return {"satoshis": sats}
    return {"error": "Erro ao calcular satoshis"}
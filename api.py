from fastapi import FastAPI
from pydantic import BaseModel

from main import buy_usdt, buy_btc, sell_btc, sell_usdt

app = FastAPI()

# Definindo o modelo para o corpo da requisição
class ValueRequest(BaseModel):
    amountInCents: float

@app.post("/V1/API/calc_btc",
          tags=["BTC"],
          summary="Valor satoshis",
          description="Retorna dados de BTC com base em um valor fiat")
async def calcular_btc(value: ValueRequest):
    # Acessando o valor do JSON enviado
    resultado = await buy_btc(value.amountInCents / 100)  # Converte centavos para BRL

    if resultado:
        return resultado

    return {"error": "Erro ao calcular resposta BTC"}

@app.post("/V1/API/calc_usdt",
          tags=["USDT"],
          summary="Valor USDT",
          description="Retorna dados de USDT com base em um valor fiat")
async def calcular_usdt(value: ValueRequest):
    # Acessando o valor do JSON enviado
    resultado = await buy_usdt(value.amountInCents / 100)  # Converte centavos para BRL

    if resultado:
        return resultado

    return {"error": "Erro ao calcular resposta USDT"}  # Correção na mensagem

@app.post("/V1/API/calc_sell_btc",
          tags=["BTC"],
          summary="Valor venda BTC",
          description="Retorna dados de venda de BTC com base em um valor fiat")
async def calcular_sell_btc(value: ValueRequest):
    # Acessando o valor do JSON enviado
    resultado = await sell_btc(value.amountInCents / 100)  # Converte centavos para BRL

    if resultado:
        return resultado

    return {"error": "Erro ao calcular resposta BTC"}

@app.post("/V1/API/calc_sell_usdt",
          tags=["USDT"],
          summary="Valor venda USDT",
          description="Retorna dados de venda de USDT com base em um valor fiat")
async def calcular_sell_usdt(value: ValueRequest):
    # Acessando o valor do JSON enviado
    resultado = await sell_usdt(value.amountInCents / 100)  # Converte centavos para BRL

    if resultado:
        return resultado

    return {"error": "Erro ao calcular resposta USDT"}  # Correção na mensagem

@app.post("/V1/API/calc_sats",
          tags=["BTC"],
          summary="Valor em satoshis",
          description="Converte um valor em BRL para satoshis com base na cotação do BTC")
async def calcular_sats(value: ValueRequest):
    # Acessando o valor do JSON enviado
    resultado = await buy_btc(value.amountInCents / 100)  # Converte centavos para BRL

    if "quantidade" in resultado:
        sats = int(resultado["quantidade"] * 100_000_000)  # Converte BTC para satoshis
        return {"satoshis": sats}

    return {"error": "Erro ao calcular satoshis"}
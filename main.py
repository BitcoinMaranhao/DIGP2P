import httpx

depix_tax = 0.99
async def buy_crypto(valor_compra, porcentagem, par):
    url = f"https://www.binance.com/api/v3/ticker/price?symbol={par}"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    if response.status_code == 200:
        cotacao = float(response.json()["price"])
        taxa_pix = depix_tax
        fee_service_brl = (valor_compra * porcentagem) / 100
        total_comprado = valor_compra - fee_service_brl - taxa_pix
        quantidade = total_comprado / cotacao
        
        return {"quantidade": round(quantidade, 8)}  # Ajustando para 8 casas decimais
    else:
        return {"error": f"Erro ao acessar API Binance: {response.status_code}"}
    
async def var_valor(valor, par):
    if valor <= 9999.99:
        taxa = 7
    elif 10000 <= valor < 20000:
        taxa = 6
    else:
        taxa = 5
    
    return await buy_crypto(valor, taxa, par)

async def sell_crypto(valor_compra, porcentagem, par):
    url = f"https://www.binance.com/api/v3/ticker/price?symbol={par}"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    if response.status_code == 200:
        cotacao = float(response.json()["price"])
        taxa_pix = depix_tax
        fee_service_brl = (valor_compra * porcentagem) / 100
        total_comprado = valor_compra + fee_service_brl + taxa_pix
        quantidade = total_comprado / cotacao
        
        return {"quantidade": round(quantidade, 8)}  # Ajustando para 8 casas decimais
    else:
        return {"error": f"Erro ao acessar API Binance: {response.status_code}"}

 
async def var_sell_valor(valor, par):
    taxa = 5    
    return await sell_crypto(valor, taxa, par)

async def buy_btc(valor):
    var_valor(valor,'BTCBRL')
    
async def buy_usdt(valor):
    var_valor(valor,'USDTBRL')
    
async def sell_btc(valor):
    var_sell_valor(valor,'BTCBRL')
    
async def sell_usdt(valor):
    var_sell_valor(valor,'USDTBRL')
# Exemplo de chamada:
# await var_valor(5000, "BTCBRL")
# await var_valor(15000, "USDTBRL")

# import asyncio

# if __name__ == "__main__":
#     resultado = asyncio.run(var_sell_valor(100000, "BTCBRL"))
#     print(resultado)
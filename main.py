import httpx

depix_tax = 0.99  # Taxa fixa do Pix

async def get_binance_price(par: str) -> float:
    """Obtém a cotação atual do par de moedas na Binance."""
    url = f"https://www.binance.com/api/v3/ticker/price?symbol={par}"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    if response.status_code == 200:
        return float(response.json()["price"])
    else:
        raise Exception(f"Erro ao acessar API Binance: {response.status_code}")

async def trade_crypto(valor: float, par: str, is_buy: bool) -> dict:
    """Realiza compra ou venda de criptomoeda com base na cotação da Binance."""
    try:
        cotacao = await get_binance_price(par)
        taxa = get_trade_tax(valor)
        fee_service_brl = (valor * taxa) / 100

        if is_buy:
            total = valor - fee_service_brl - depix_tax
        else:
            total = valor + fee_service_brl + depix_tax

        quantidade = total / cotacao
        return {"quantidade": round(quantidade, 8)}

    except Exception as e:
        return {"error": str(e)}

def get_trade_tax(valor: float) -> int:
    """Determina a taxa de negociação com base no valor."""
    if valor <= 9999.99:
        return 6
    elif 10000 <= valor < 20000:
        return 5
    return 4

# Funções específicas para compra e venda de BTC e USDT
async def buy_btc(valor: float): return await trade_crypto(valor, 'BTCBRL', is_buy=True)
async def buy_usdt(valor: float): return await trade_crypto(valor, 'USDTBRL', is_buy=True)
async def sell_btc(valor: float): return await trade_crypto(valor, 'BTCBRL', is_buy=False)
async def sell_usdt(valor: float): return await trade_crypto(valor, 'USDTBRL', is_buy=False)

# Exemplo de uso:
# import asyncio
# asyncio.run(buy_btc(5000))

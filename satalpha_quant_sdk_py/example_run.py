import asyncio
from satalpha_quant_sdk_py.core import AggTradeWebSocketClient

def message_handler(msg: str):
    print("收到消息:", msg)

async def main():
    # 测试本地地址
    ws_url = "ws://localhost:9999/ws/public"
    client = AggTradeWebSocketClient(ws_url)
    client.set_params(["PERP_BTC/USDT:USDT", "PERP_ETH/USDT:USDT"])
    client.on_message(message_handler)

    # 异步运行连接，注意此示例会阻塞
    await asyncio.to_thread(client.run)

if __name__ == "__main__":
    asyncio.run(main())

import pytest
import asyncio
from satalpha_quant_sdk_py.core import PublicWebSocketClient

def message_handler(msg: str):
    print("收到消息:", msg)

async def main():
    # 测试本地地址
    ws_url = "wss://quant-ws-test.satsalpha.com/public"
    client = PublicWebSocketClient(ws_url)
    client.set_topic("aggTrade")
    client.set_params(["PERP_BTC/USDT:USDT", "PERP_ETH/USDT:USDT"])
    client.on_message(message_handler)

    # 异步运行连接，注意此示例会阻塞
    await asyncio.to_thread(client.run)

@pytest.mark.asyncio
async def test_ws_subscribe_runs():
    # 异步运行连接，注意此示例会阻塞
    await main()

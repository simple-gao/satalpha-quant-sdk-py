import asyncio
import json
import websockets

class PublicWebSocketClient:
    def __init__(self, url: str):
        self.url = url
        self.params = []
        self.topic = None
        self.ws = None
        self.on_message_callback = None
        self._stop = False

    def set_params(self, params: list[str]):
        self.params = params

    def set_topic(self, topic: str):
        self.topic = topic

    def on_message(self, callback):
        """注册收到消息回调"""
        self.on_message_callback = callback

    async def _connect(self):
        while not self._stop:
            try:
                print("尝试连接 WebSocket...")
                async with websockets.connect(self.url) as ws:
                    self.ws = ws
                    print("WebSocket 连接成功")
                    await self._send_subscribe()

                    while True:
                        msg = await ws.recv()
                        if self.on_message_callback:
                            self.on_message_callback(msg)

            except (websockets.exceptions.ConnectionClosedError,
                    websockets.exceptions.ConnectionClosedOK,
                    ConnectionResetError) as e:
                print(f"连接断开，原因: {e}，5秒后重连...")
                await asyncio.sleep(5)
            except Exception as e:
                print(f"未知错误: {e}，10秒后重连...")
                await asyncio.sleep(10)

    async def _send_subscribe(self):
        if not self.params:
            print("订阅参数为空，无法订阅")
            return
        sub_msg = {
            "op": "subscribe",
            "topic": self.topic,
            "params": self.params
        }
        await self.ws.send(json.dumps(sub_msg))
        print(f"发送订阅消息: {sub_msg}")

    async def _send_unsubscribe(self):
        if not self.params:
            print("警告：取消订阅参数为空，无法取消订阅")
            return
        unsub_msg = {
            "op": "unsubscribe",
            "topic": self.topic,
            "params": self.params
        }
        if self.ws is not None:
            await self.ws.send(json.dumps(unsub_msg))
            print(f"发送取消订阅消息: {unsub_msg}")

    async def _close(self):
        self._stop = True
        if self.ws is not None:
            await self._send_unsubscribe()
            await self.ws.close()
            print("WebSocket 已关闭")

    def run(self):
        asyncio.run(self._connect())

    async def stop(self):
        await self._close()

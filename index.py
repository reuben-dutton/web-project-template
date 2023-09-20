import asyncio

from src.tasks_example import make_request
from src.worker.broker import broker


async def main():
    await broker.startup()

    task = await make_request.kiq("https://httpbin.org/get")
    result = await task.wait_result()
    task = await make_request.kiq("https://httpbin.org/get")
    result = await task.wait_result()
    task = await make_request.kiq("https://httpbin.org/get")
    result = await task.wait_result()

    print(result.return_value.json())

    await broker.shutdown()


if __name__ == "__main__":
    asyncio.run(main())

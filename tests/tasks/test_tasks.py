import pytest
import respx
from taskiq import Context

from src.tasks_example import make_request
from tests import utils


@respx.mock
@pytest.mark.anyio
async def test_make_request_unlimited(monkeypatch, unlimited_client):
    server_response = utils.construct_delayed_response(0)

    respx.get("https://httpbin.org/get").mock(side_effect=server_response)

    def get_client(context: Context):
        return unlimited_client

    monkeypatch.setattr("src.worker.dependencies.get_client", get_client)

    tasks = []

    for _ in range(10):
        tasks.append(await make_request.kiq("https://httpbin.org/get"))

    for task in tasks:
        result = await task.wait_result()

    assert result.return_value.status_code == 200

import pytest

from src.web.client import PoliteClient, ClientSettings


@pytest.fixture
def anyio_backend():
    return 'asyncio'


@pytest.fixture
async def unlimited_client():
    clientSettings: ClientSettings = ClientSettings(None, None)
    client = PoliteClient(clientSettings)
    yield client
    await client.aclose()


@pytest.fixture
async def retry_client():
    clientSettings: ClientSettings = ClientSettings(None, None)
    clientSettings.set_max_retries(2)
    client = PoliteClient(clientSettings)
    yield client
    await client.aclose()


@pytest.fixture(params=[1, 2, 3, 5, 7], ids=lambda rate: f"global_rate={rate}")
async def global_limited_client(request):
    clientSettings: ClientSettings = ClientSettings(request.param, None)
    client = PoliteClient(clientSettings)
    yield client
    await client.aclose()


@pytest.fixture(params=[1, 2, 3], ids=lambda rate: f"domain_rate={rate}")
async def domain_limited_client(request):
    clientSettings: ClientSettings = ClientSettings(None, request.param)
    clientSettings.set_domain_concurrency(1)
    client = PoliteClient(clientSettings)
    yield client
    await client.aclose()

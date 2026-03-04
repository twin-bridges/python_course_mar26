import pytest
import os
from dotenv import load_dotenv
from cpapi import APIClient, APIClientArgs


@pytest.fixture(scope="session")
def web_api_session():

    api_server = "chkpnt-pod99.lasthop.io"
    api_version = "2"

    load_dotenv()
    username = "admin"
    password = os.environ["CHKP_ADMIN"]

    client_args = APIClientArgs(
        server=api_server, api_version=api_version, unsafe=True, context="web_api"
    )

    with APIClient(client_args) as api_client:
        api_client.login(username, password)

        # Object that is passed to the tests
        yield api_client

import os
import pytest
from mgmt_cli_session import mgmt_cli_auth
from dotenv import load_dotenv


def test_mgmt_cli_auth(ssh_conn):

    load_dotenv()
    admin_pass = os.environ["CHKP_ADMIN"]

    # Intentionally fail
    with pytest.raises(KeyError):
        mgmt_cli_auth(ssh_conn, username="admin", password="invalid")

    session_id = mgmt_cli_auth(ssh_conn, username="admin", password=admin_pass)
    assert len(session_id) == 43

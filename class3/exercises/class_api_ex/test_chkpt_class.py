import os
from rich import print
from dotenv import load_dotenv
from chkpt_api_ex import ChkptAPI
import ipdb  # noqa


def gaia_test():
    host = "chkpnt-pod99.lasthop.io"

    # This looks for a .env file and loads it
    load_dotenv()
    user = "admin"
    admin_pass = os.environ["CHKP_ADMIN"]

    api_client = ChkptAPI(host=host, username=user, password=admin_pass, mode="gaia_api")
    api_client.login()

    endpoint = "show-static-routes"
    res = api_client.call(endpoint=endpoint)
    print(res.json())

    api_client.logout()


if __name__ == "__main__":
    gaia_test()

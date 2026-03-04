from rich import print  # noqa
import ipdb  # noqa


class ChkptAPI:
    def __init__(
        self,
        host,
        username,
        password,
        mode="web_api",
        api_version=None,
        ssl_verify=False,
    ):
        self.host = host
        self.username = username
        self.password = password

        if api_version is None:
            if mode == "web_api":
                api_version = "2"
            elif mode == "gaia_api":
                api_version = "1.8"

        self.ssl_verify = ssl_verify
        self.headers = {"Content-Type": "application/json"}
        self.base_url = f"https://{host}/{mode}/v{api_version}/"


if __name__ == "__main__":
    host = "chkpnt-pod99.lasthop.io"
    user = "admin"
    admin_pass = "testpass"

    # Test Gaia API
    api_client = ChkptAPI(
        host=host, username=user, password=admin_pass, mode="gaia_api"
    )
    print("Testing ChkptAPI Class (Gaia API)")
    print(api_client.base_url)
    print()

    # Test Mgmt API
    api_client = ChkptAPI(
        host=host, username=user, password=admin_pass, mode="web_api"
    )
    print("Testing ChkptAPI Class (Mgmt API)")
    print(api_client.base_url)
    print()


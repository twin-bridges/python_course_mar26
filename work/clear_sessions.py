import os
from rich import print
from dotenv import load_dotenv
from cpapi import APIClient, APIClientArgs


class chkp_exception(Exception):
    pass


def cfg_host_object(api_client, host_object):

    payload = {"name": host_object["name"]}
    api_res = api_client.api_call(command="show-host", payload=payload)

    payload = host_object
    if api_res.success:
        api_res = api_client.api_call(command="set-host", payload=payload)

    else:
        api_res = api_client.api_call(command="add-host", payload=payload)

    if not api_res.success:
        msg = api_res.error_message
        raise chkp_exception(f"Error creating/updating host object: {msg}")

    return api_res


def cfg_fw_rule(api_client, corp_fw_rule):

    payload = {"name": corp_fw_rule["name"], "layer": corp_fw_rule["layer"]}
    api_res = api_client.api_call(command="show-access-rule", payload=payload)

    payload = corp_fw_rule
    if api_res.success:
        api_res = api_client.api_call(command="set-access-rule", payload=payload)
    else:
        api_res = api_client.api_call(command="add-access-rule", payload=payload)

    if not api_res.success:
        msg = api_res.error_message
        raise chkp_exception(f"Error creating/updating access rule: {msg}")

    return api_res


def main():
    host = "chkpnt-pod99.lasthop.io"

    # This looks for a .env file and loads it
    load_dotenv()
    username = "admin"
    password = os.environ["CHKP_ADMIN"]

    api_version = "2"
    no_ssl_verify = True

    client_args = APIClientArgs(
        server=host, api_version=api_version, unsafe=no_ssl_verify, context="web_api"
    )

    with APIClient(client_args) as api_client:
        api_client.login(username, password)

        payload = {"details-level": "full"}
        response = api_client.api_call(command="show-sessions", payload=payload)
        sessions = response.data
        print(f"Number of sessions with locks: {sessions['total']}")
        import ipdb

        ipdb.set_trace()

        for session in sessions["objects"]:
            if session["locks"] > 0:
                import ipdb

                ipdb.set_trace()
                uid = session["uid"]
                payload = {"uid": f"{uid}"}
                api_client.api_call(command="take-over-session", payload=payload)
                api_client.api_call(command="discard", payload=None)

        response = api_client.api_call(command="show-sessions", payload=payload)
        sessions = response.data
        print(f"Number of sessions with locks: {sessions['total']}")


if __name__ == "__main__":
    main()

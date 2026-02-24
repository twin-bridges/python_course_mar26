from chkpt_exceptions import ChkPntConfigError, ChkPntPolicyInstallError
from rich import print
import ipdb  # noqa


def extract_fw_name(fqdn):
    # Extract the fw_name from the DNS name
    if "." in fqdn:
        fw_name = fqdn.split(".")[0]
        return fw_name
    else:
        raise ValueError("Invalid firewall name: {fqdn}")


def display_fw_policy(api_client, layer="Network"):
    payload = {"name": layer}
    api_res = api_client.api_call(command="show-access-rulebase", payload=payload)
    fw_rules = api_res.data["rulebase"]
    print(fw_rules)


def install_fw_policy(api_client, policy_package="Standard", targets=None):
    """
    Install the firewall policy on firewall.

    This code ASSUMES all-in-one firewall i.e. target firewall is web_api host by default.
    """
    if targets is None:
        fw_name = extract_fw_name(api_client.server)
        targets = [fw_name]

    payload = {"policy-package": policy_package, "targets": targets}
    api_res = api_client.api_call(command="install-policy", payload=payload)
    if not api_res.success:
        msg = f"Failed to install firewall policy: {payload}"
        raise ChkPntPolicyInstallError(msg)


def cfg_fw_policy(api_client, fw_rules):
    """Use mgmt API to configure firewall policy rules."""

    fw_name = extract_fw_name(api_client.server)
    management_rules = [
        {
            "layer": "Network",
            "name": "Ansible Management Access",
            "source": [
                "Ansible Server",
                "Windows SmartConsole",
                "Windows SmartConsole Public",
            ],
            "destination": fw_name,
            "service": "Any",
            "action": "Accept",
            "position": 1,
        },
        {
            "layer": "Network",
            "name": "SSH Access",
            "source": "Any",
            "destination": fw_name,
            "service": "SSH",
            "action": "Accept",
            "position": 2,
        },
    ]

    for fw_rule in management_rules:
        # Check if fw_rule already exists
        obj_exists = False
        payload = {"layer": fw_rule["layer"], "name": fw_rule["name"]}
        api_res = api_client.api_call(command="show-access-rule", payload=payload)

        if api_res.success:
            obj_exists = True
        if obj_exists:
            print(f"Updating firewall rule: {fw_rule}")
            api_res = api_client.api_call(command="set-access-rule", payload=fw_rule)
        else:
            print(f"Configuring firewall rule: {fw_rule}")
            api_res = api_client.api_call(command="add-access-rule", payload=fw_rule)

        if not api_res.success:
            msg = f"Failed to configure firewall rule: {fw_rule}"
            raise ChkPntConfigError(msg)

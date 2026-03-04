import ipdb

def test_blocked_ips_group(web_api_session):
    # api_session is the logged-in client object from the fixture
    import ipdb

    ipdb.set_trace()
    endpoint = "show-group"
    payload = {"name": "Blocked IPs"}
    response = web_api_session.api_call("show-group", payload=payload)

    assert response.success is True

    group_name = response.data["name"]
    assert "Blocked IPs" == group_name

    # Membership check
    members = response.data["members"]
    assert len(members) == 10

def test_host_objects(web_api_session):

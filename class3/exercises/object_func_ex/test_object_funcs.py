from object_funcs import cfg_host_object, cfg_network_object, cfg_group_object


def test_host_object_creation(web_api_session):

    test_host_obj = {
        "name": "Test Host1",
        "ipv4-address": "10.31.10.101",
        "color": "black",
    }

    (api_res, status) = cfg_host_object(web_api_session, test_host_obj)
    assert api_res.success is True
    assert status in ["created", "updated"]


def test_network_object_creation(web_api_session):

    test_network_obj = {
        "name": "Test Network1",
        "subnet": "10.31.10.0",
        "color": "green",
        "mask-length": 24,
    }

    (api_res, status) = cfg_network_object(web_api_session, test_network_obj)
    assert api_res.success is True
    assert status in ["created", "updated"]


def test_group_object_creation(web_api_session):

    test_group_obj = {
        "name": "Test Group1",
        "members": [
            "Test Network1",
        ],
        "color": "blue",
    }

    (api_res, status) = cfg_group_object(web_api_session, test_group_obj)
    assert api_res.success is True
    assert status in ["created", "updated"]

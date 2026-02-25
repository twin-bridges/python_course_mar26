# Some TCP service
fw_service = {
    "uid": "97aeb3d1-9aea-11d5-bd16-0090272ccb30",
    "name": "ftp-port",
    "type": "service-tcp",
    "domain": {
        "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
        "name": "Check Point Data",
        "domain-type": "data domain",
    },
    "port": "21",
    "icon": "Services/TCPService",
    "color": "forest green",
}
fw_service_keys = list(fw_service.keys())

# Gracefully handle with try/except with finally
try:
    print("before Error")
    # fw_service["service_type"]
    # Try to access list element that doesn't exist
    fw_service_keys[100]
    print("after Error")
except Exception:
    print("Very generic exception handler.")
    print("...be careful here.")
finally:
    print("Always happens")

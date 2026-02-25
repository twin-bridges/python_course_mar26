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

# Try to access a key that doesn't exist
fw_service["service_type"]

# Gracefully handle with try/except
try:
    print("before KeyError")
    fw_service["service_type"]
    print("after KeyError")
except KeyError:
    print("Inside exception handler")

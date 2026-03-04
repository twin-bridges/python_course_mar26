def split_ip_addr(ip_addr):
    octets = ip_addr.split(".")
    if len(octets) != 4:
        raise ValueError("Invalid ip_addr, split('.') didn't return 4 octets")

    return octets

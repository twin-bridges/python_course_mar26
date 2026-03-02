# Pool size 5: 0:00:02.135320 (Threads)
# Pool size 2: 0:00:06.356690 (Threads)
#
# Pool size 5: 0:00:02.155889 (Processes)
from concurrent.futures import ThreadPoolExecutor, as_completed

# from concurrent.futures import ProcessPoolExecutor, as_completed
from datetime import datetime
from netmiko import ConnectHandler
from my_devices import device_list


def ssh_conn(device):
    net_connect = ConnectHandler(**device)
    host = net_connect.host
    cmd = "show interface eth0"
    data = net_connect.send_command(cmd)
    return (host, data)


if __name__ == "__main__":
    start_time = datetime.now()
    max_threads = 5

    pool = ThreadPoolExecutor(max_threads)
    # pool = ProcessPoolExecutor(max_threads)

    future_list = []
    for a_device in device_list:
        future = pool.submit(ssh_conn, a_device)
        future_list.append(future)

    # Process as completed
    print()
    for future in as_completed(future_list):
        (host, result) = future.result()
        print(f"\n{host}:")
        print("-" * 20)
        for line in result.splitlines():
            if "ipv4-address" in line:
                print(line)
        print()

    end_time = datetime.now()
    print()
    print(end_time - start_time)
    print()

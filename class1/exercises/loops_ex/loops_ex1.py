from rich import print

my_firewalls = [
    "pod1-gaia",
    "pod2-gaia",
    "pod3-gaia",
    "pod4-gaia",
    "pod5-gaia",
]

for fw in my_firewalls:
    print(fw)

for fw in my_firewalls:
    if fw == "pod5-gaia":
        print(f"\nConnecting to fw: {fw}\n")

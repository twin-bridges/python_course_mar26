from rich import print

my_firewalls = [
    "pod1-gaia",
    "pod2-gaia",
    "pod3-gaia",
    "pod4-gaia",
    "pod5-gaia",
    "pod98-gaia",
    "pod99-gaia",
]

for fw in my_firewalls:
    if fw == "pod4-gaia":
        continue
    if fw == "pod98-gaia":
        break
    print(fw)

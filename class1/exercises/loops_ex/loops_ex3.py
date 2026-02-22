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

for idx, fw in enumerate(my_firewalls):
    print(f"{idx} -> {fw}")

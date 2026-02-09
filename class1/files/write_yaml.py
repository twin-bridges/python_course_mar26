import yaml

data = {
    "current-version": "1.8",
    "supported-versions": ["1", "1.1", "1.2", "1.3", "1.4", "1.5", "1.6", "1.7", "1.8"],
}

with open("gaia_api.yaml", "w") as f:
    yaml.dump(data, f, default_flow_style=False)

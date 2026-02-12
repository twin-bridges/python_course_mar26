#!/usr/bin/env python
import ipdb  # noqa
import yaml 
from rich import print


with open("api_support_versions.yml") as f:
    api_versions = yaml.safe_load(f)

supported_versions = api_versions["supported-versions"]

# ['1', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '1.8']
if "1.8" in supported_versions:
    api_version = "1.8"

api_version = "1.8"
if "1." in api_version:
    base_api = "v1"
elif "2." in api_version:
    base_api = "v2"

if base_api == "v1" and float(api_version) >= 1.8:
    print("API Version 1.8 or later (not V2)")

if base_api == "v1" or base_api == "v2":
    print("API V1 or V2")


from pathlib import Path
from rich import print
import ipdb  # noqa

# Pathlib home
home = Path.home()
netmiko_yml_file = home / ".netmiko.yml"

print(netmiko_yml_file)

# Read file
with open(netmiko_yml_file) as f:
    netmiko_yml_data = f.read()
print(netmiko_yml_data)

# Alternate read (pathlib magic)
netmiko_yml_data = netmiko_yml_file.read_text()
print(netmiko_yml_data)

# More difficult path
home = Path.home()
sessions_file = (
    home / "python_course_mar26" / "class2" / "complex_dstruct" / "sessions.json"
)

ipdb.set_trace()
sessions_file.exists()
sessions_file.is_file()
sessions_file.is_dir()

# Get the parent dir
sessions_file.name
parent_dir = sessions_file.parent
ipdb.set_trace()
print(parent_dir)

# Creating directories
# Path("./test1/2026/check_point").mkdir(parents=True, exist_ok=True)

# Find all JSONs in this folder
home = Path.home()
course_dir = home / "python_course_mar26"
# Recursive search
print()
for f in course_dir.rglob("*.json"):
    print(f)

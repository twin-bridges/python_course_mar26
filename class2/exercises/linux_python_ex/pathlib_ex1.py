from pathlib import Path
from rich import print
import yaml

# Pathlib home
home = Path.home()
firewalls_file = (
    home / "python_course_mar26/class2/exercises/linux_python_ex/firewalls.yml"
)

print(f"\n{firewalls_file=}")
print(f"Exists: {firewalls_file.exists()}")
print(f"Is file: {firewalls_file.is_file()}")

parent_dir = firewalls_file.parent
print(f"\n{parent_dir=}")
print(f"Parent exists: {parent_dir.exists()}")
print(f"Is dir: {parent_dir.is_dir()}")

## Read file as YAML
with open(firewalls_file) as f:
    fw_list = yaml.safe_load(f)

print(f"\n{fw_list=}\n")

# Create temp work dir
work_dir = home / "tmp_work"
if not work_dir.exists():
    print(f"Creating {work_dir}")
    work_dir.mkdir()

# Add new entries to firewall list
fw_list += ["ber-fw1", "ber-fw2"]

new_fw_file = work_dir / "firewalls.yml"
print(fw_list)
with open(new_fw_file, "w") as f:
    yaml.dump(fw_list, f, default_flow_style=False)

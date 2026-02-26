### Pathlib Exercise

Use the following to import pathlib

```python
from pathlib import Path
```

Create the following Path object:

```python
home = Path.home()
firewalls_file = (
    home / "python_course_mar26/class2/exercises/linux_python_ex/firewalls.yml"
)
```

Next verify the 'firewalls_file' exists and is a file.

Extract the parent directory (i.e. the directory that contains the file 'firewalls.yml' and verify this directory exists and is in fact a directory.

Use the 'yaml' library to read in the contents of this 'firewalls_file' as YAML. Print out the contents of that file (it should be a list of firewalls).

Next use pathlib to create the following directory. You can use code similar to the following:

```python
work_dir = home / "tmp_work"
if not work_dir.exists():
    print(f"Creating {work_dir}")
    work_dir.mkdir()
```

Now add on the following two firewalls to your list of firewalls: ["ber-fw1", "ber-fw2"] 

Finally, create a new "firewalls.yml" file inside the 'work_dir' that you created above. Once again use pathlib and the YAML library to accomplish this.


import subprocess
from pathlib import Path


def subprocess_runner(cmd_list, exercise_dir):
    with subprocess.Popen(
        cmd_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=exercise_dir
    ) as proc:
        std_out, std_err = proc.communicate()
    return (std_out.decode(), std_err.decode(), proc.returncode)


if __name__ == "__main__":
    cmd_list = ["ls", "-a", "-l"]
    print("Executing ls -al:")
    std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=".")
    print(std_out)
    print(std_err)

    home = Path.home()
    script = home / "python_course_mar26" / "class2" / "gaia_ssh" / "show_version.py"
    python = home / "VENV/py3_venv/bin/python"

    if script.is_file() and python.is_file():
        print("Executing Python script:")
        cmd_list = [python, script]
        std_out, std_err, return_code = subprocess_runner(cmd_list, exercise_dir=".")
        print(std_out)
        print(std_err)

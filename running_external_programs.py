import subprocess

# completed = subprocess.run(
#    ["clear", "ls", "-l"], capture_output=True, text=True
# )

try:
    completed = subprocess.run(
        ["python3", "other.py"],
        capture_output=True,
        text=True,
        check=True,
    )
    print(type(completed))
    print("args", completed.args)
    print("return_code", completed.returncode)
    print("stderr", completed.stderr)
    # print("stdout", completed.stdout)

    print(completed.stdout)
except subprocess.CalledProcessError as error:
    print("Error", error)

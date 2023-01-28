import subprocess

print(subprocess.run(["ls", "-l"], capture_output=True))

print(' ')

print(subprocess.run(["ls", "-l"], capture_output=False))

print(' ')
list_files = subprocess.run(["ls", "-l"])
print("The exit code was: %d" % list_files.returncode)

useless_cat_call = subprocess.run(["cat"],
                                  stdout=subprocess.PIPE,
                                  text=True,
                                  input="Hello from the other side")

print(useless_cat_call.stdout)  # Hello from the other side

#    stdout=subprocess.PIPE tells Python to redirect the output of the command to an object so it can be manually read later
#    text=True returns stdout and stderr as strings. The default return type is bytes.
#    input="Hello from the other side" tells Python to add the string as input to the cat command.


# subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False, cwd=None, timeout=None, check=False, encoding=None, errors=None, text=None, env=None, universal_newlines=None, **other_popen_kwargs)
# https://docs.python.org/3/library/subprocess.html


# subprocess.Popen allows further code execution even while it is still processing

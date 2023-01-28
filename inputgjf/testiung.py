import subprocess

output1 = subprocess.run(["ls", "-l"], capture_output=True)

print(output1)

import subprocess
import os

res = subprocess.check_output(
    ['git', '-C', r'C:\jty\WorkSpace\GoldenShark', 'pull'])
print(res)

print(len(os.listdir(r'C:\jty\WorkSpace\GoldenShark')))

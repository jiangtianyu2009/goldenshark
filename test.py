import subprocess

res = subprocess.check_output(
    ['git', '-C', r'C:\jty\WorkSpace\GoldenShark', 'pull'])
print(res)

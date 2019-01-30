import os

cwd = os.getcwd()
print(cwd)

files = os.listdir(cwd)
print(files)

os.chdir('..')
print(os.getcwd())
print(*os.listdir(os.getcwd()))

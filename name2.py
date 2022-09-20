#!/usr/bin/python3
print("Python scripting")
import os
os.system('touch 4.txt')
os.system('git status')
os.system('git add .')
os.system('git status')
os.system('git commit -m"second"')
os.system('git status')
os.system('git log')
os.system('git remote add origin https://github.com/anilsb06/python_script.git')
os.system('git push origin master')

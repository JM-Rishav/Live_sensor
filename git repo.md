git repo
create folder for building project
go inside and open vscode
create virtual env
activate vir env
create package
setup and run
# python setup.py install
requirement and run
# pip install -r requirements.txt



# To create a environment (virtual environment)
conda create -p venv python = 3.8
conda create -p venv python = 3.8 -y  # this proceeds without permission, for the above one it will ask permission
# if you made a mistake, you can always use
conda deactivate

https://github.com/JM-Rishav/Live_sensor.git

# we use .gitignore to ignore some of the files which we don't want to be uploaded on github
#venv contains all the virtual environment requirement installation files, it is 
#very high in size, due to dependecies files, libraries. 
.gitignore 

# How to make folder as package
we put __init__.py file in it, then it becomes as a package and one can use it.

# why do we make setup.py file
we use setup.py file for
1. for installing packages
2. managing dependecies
3. managing distribution 

# __init__.py will become package when i run setup.py file
setup.py file will contain bunch of codes
"from setuptools import find_packages , setup"
" #from typing import list "

# find_package ka kaam hai jake packages check karna
# wo check karega toh use sirf filhal "__init__.py" milega


# what is -r in pip install -r requirements.txt
it is basically falg
stands for "requirements" 

# what is egg-info file and when and how it is made.
egg-info file is made when we execute the setup.py file
it stores the dependencies (its called meta-data)

# what the purpose of find_packages, and why we use
search all the package one by one
it basically checks all the directories in the path

# what is the difference b/w -p and -n while creating virtual invironment
we use "-p" to give full path and store at specific location 
to store at default path we use "-n"


# make a new branch in git
git branch developer1
git branch devloper2

# switch b/w branches
git checkout developer1
"Switched to branch 'developer1'"

# to merge developer1 and main branch
# merge any 2 branches
# if i am in main : it will merge with main
git merge developer1

# delete a branch
git branch -d devloper2

# what are the levels of logging
debug 
info 
warning
error
critical

# which is the smallest level of logging
smallest is debug and viceversa is critical
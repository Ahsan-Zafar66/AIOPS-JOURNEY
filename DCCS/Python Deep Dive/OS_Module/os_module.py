# importing os module
import os

# printing the current working directory
print("Current Wokring Directory is {}--------".format(os.getcwd()))
print("ahsan is using vscode")

# changing directory using forward slash
os.chdir("D:/7th Semester")
print("Current Wokring Directory is {}--------".format(os.getcwd()))
# listing ocntents od directory
print(os.listdir())

# changing directory using backward slash, if you use backward slash use it twice at places 
# where one is required and # thrice where two are required because backslash is an escape character
os.chdir("D:\\8th Semester")
print("Current Wokring Directory is {}--------".format(os.getcwd()))
print(os.listdir())


def mycode():
    print("Ahsan is learning python")

# mycode()

if (__name__=="main"):
    print("Ahsan is also doing ielts")
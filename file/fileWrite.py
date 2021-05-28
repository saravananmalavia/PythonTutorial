import os
filePath = os.getcwd()
fileName = filePath + "/PythonTutorial/file/demofile4.txt" 
# f = open(fileName, "a")
# f = open(fileName, "x")
os.remove(filePath)
# f.write("This is demo for file append")
# f.close()

# #open and read the file after the appending:
# f = open(fileName, "r")
# print(f.read())
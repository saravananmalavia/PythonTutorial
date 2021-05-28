import os
filePath = os.getcwd()
fileName = filePath + "/PythonTutorial/file/demofile.txt" 
# print(fileName)
f = open(fileName, "r")
# print(f.read())
# print(f.read(5))
# print(f.readline())
# print(f.readline())
for x in f:
  print(x)
f.close()

import os
import shutil
e = os.getcwd()
#print(e)
#os.mkdir("/Users/Test")
os.listdir()
#print(os.listdir())
os.path.exists("Test")
#print(os.path.exists("Test"))
Root,ext = os.path.splitext("ABC.txt")
#print(ext)
source = "ABC.txt"
destination = "Test/ABC.txt"
shutil.copy(source, destination)
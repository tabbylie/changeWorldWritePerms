import os
import sys

try:
    directoryToSearch = os.path.abspath(sys.argv[1])
except:
    print("Requires a directory to search!")
try:
    isVerbose = True if sys.argv[2] else False
except:
    isVerbose = False

def log(printStatement):
    if isVerbose:
        print(printStatement)

def searchDir(directory):
    allFilesAndDirs = os.listdir(directory)
    for filesOrDir in allFilesAndDirs:
        filesOrDir = os.path.join(directory, filesOrDir)
        if os.path.isdir(filesOrDir):
            log(f"{filesOrDir} is a directory; searching now.")
            searchDir(os.path.abspath(filesOrDir))
            continue
        status = os.stat(os.path.join(directory, filesOrDir))
        permsCode = int(oct(status.st_mode)[-3:])
        if permsCode == 777:
            os.chmod(filesOrDir, 0o775)
            print(f"{filesOrDir} perms are now {775}.")
        else:
            log(f"{filesOrDir} perms not changed. Continuing")
            continue

searchDir(directoryToSearch)
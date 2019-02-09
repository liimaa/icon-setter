import sys, os, re
from shutil import move

def icos(dr):
    for root, dirs, files in os.walk(dr):
        #print(root, dirs, files, "\n")
        for directory in dirs:
            folderPath = os.path.join(root, directory)
            print(folderPath)

            os.mkdir(directory)

def main(args):
    icos(args)

if __name__ == '__main__':
    main(sys.argv[1])

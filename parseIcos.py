import sys, os, re
from shutil import move

def icos(dr):
    for root, dirs, files in os.walk(dr):
        print(root, dirs, files, "\n")
        for item in files:
            p1 = item.lower()
            p2 = p1[:-4]
            p3 = p2.split("by_", 1)[0] #by_someone
            p4 = re.sub('\([^()]*\)', ' ', p3)
            p5 = re.sub('\[[^\]]*\]', ' ', p4)
            p6 = p5.replace("anime_", "")
            p7 = p6.replace("icon_folder", "")
            p8 = p7.replace("256px", "")
            p9 = p8.replace("_f_s_", "")
            p10 = p9.replace("526px","")
            p11 = p10.split("folder_", 1)[0]
            p12 = p11.split("icon_", 1)[0]
            p13 = re.sub('[^A-Za-z0-9]', ' ', p12)
            p14 = " ".join(p13.split())
            folderPath = os.path.join(root, item)

            print("Original name:", item)
            print("Parsed name:  ", p14)
            print("Path: ", folderPath, "\n")

            move(folderPath, p14 + ".ico")

def main(args):
    icos(args)

if __name__ == '__main__':
    main(sys.argv[1])

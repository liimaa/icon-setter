#Usage > py main.py anime_folder_path icon_folder_path
#How it works ?
#icon name == folder name > icon sets to folder
import subprocess, os, sys, re

#Does desktop.ini file
def setDesktop_ini(savePath, icoFolder ,customIconPath):
	completeName = os.path.join(savePath, "desktop.ini")
	a = os.path.isfile(completeName)
	if(a == False):
		f = open(completeName,"w")
		f.write("[.ShellClassInfo]" + "\n"
		"ConfirmFileOp=0" + "\n" +
		"IconFile=" + icoFolder +"\\"+ customIconPath+".ico" + "\n" +
		"IconIndex=0"
		)
		f.close()
	else:
		print("Icon set:    ", a, "\n")

#Protect folder & hide windows.ini
def defendDesktop_ini(folder):
	subprocess.call(["attrib", "+s", folder], shell=True)
	subprocess.call(["attrib", "+h", folder+"\desktop.ini"], shell=True)

def listAnime(dr, dr2):
	for root, dirs, files in os.walk(dr):
		#print(root, dirs, files)
		for directory in dirs:
			folderPath = os.path.join(root, directory)
			p1 = re.sub('\([^()]*\)', ' ', directory)
			p2 = re.sub('\[[^\]]*\]', ' ', p1)
			p3 = re.sub('[^A-Za-z0-9]', ' ', p2)
			p4 = " ".join(p3.split())
			directoryParsed = p4.lower()

			print("Folder name: ", directory)
			print("Parsed name: ", directoryParsed)
			print("Folder path: ", folderPath)
			print("Icon path:   ", dr2 + "\\" + directoryParsed, "\n")

			#sets icos
			setDesktop_ini(folderPath, dr2, directoryParsed)
			defendDesktop_ini(folderPath)

	icos = []
	for root, dirs, files in os.walk(dr2):
		#print(root, dirs, files, "\n")
		for item in files:
			icos.append(item)
	#dump icos
	#print(icos)

def main(animeFolder, iconFolder):
	listAnime(animeFolder, iconFolder)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])

'''
Make linux version
Linux
subprocess.Popen([
"gvfs-set-attribute", "-t", "string",
os.path.abspath("t"), "metadata::custom-icon",
"file:///"+os.path.abspath(os.path.join("t", "5.ico"))
], shell=True)
'''

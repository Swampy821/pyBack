import os, os.path, sys
pmName = 'config/dirConfig.py'
execfile(pmName)
dirtocheck = '/home/steve/pythonProjects/'
for root, _, files in os.walk(dirtocheck):
	for f in files:
		fullpath = os.path.join(root, f)
		sys.stdout.write("%s \n" % fullpath);
		f = open("dirList.txt",'a')
		f.write(fullpath+'\n');
		f.close()
#Logging files. Project may just turn into a project logger. Make new Repo.
#Copy Files from config to backup directory here.
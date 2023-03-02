import os

newDir = "TMVAPlots_230209"
listDirs = [ dir_ for dir_ in os.listdir("./") if "TMVAClassification_DNN" in dir_ ]
# ['TMVAClassification_DNN_Low_year_comb_Batch2000']
# plost weights
# overtrain_DNN.png  rejBvsS.png
#-> overtrain_DNN_DNN_Low_year_comb_Batch2000.png
#-> overtrain_DNN_Low_year_comb_Batch2000.png

cmdFcn1 = lambda dir_ : "cp {DIR}/plots/overtrain_DNN.png {NEWDIR}/overtrain_{DIR}.png".format(DIR=dir_, NEWDIR=newDir)
cmdFcn2 = lambda dir_: "cp {DIR}/plots/rejBvsS.png {NEWDIR}/rejBvsS_{DIR}.png".format(DIR=dir_, NEWDIR=newDir)

cmdlist1 = map(cmdFcn1, listDirs)
cmdlist2 = map(cmdFcn2, listDirs)

# make new dir
if not os.path.exists(newDir):
    os.mkdir(newDir)
# mv plots
for cmd in cmdlist1:
    os.system(cmd)
for cmd in cmdlist2:
    os.system(cmd)

rsync_cmd   = "rsync -arv {DIR} boh@lxplus.cern.ch:/eos/user/b/boh/www/nanoV9/".format(DIR=newDir)
cpindex_cmd = "ssh boh@lxplus.cern.ch cp /eos/user/b/boh/www/nanoV9/index.php /eos/user/b/boh/www/nanoV9/{DIR}/index.php".format(DIR=newDir)

os.system(rsync_cmd)
os.system(cpindex_cmd)


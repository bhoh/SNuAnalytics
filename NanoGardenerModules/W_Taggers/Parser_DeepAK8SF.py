import csv
filename='DeepAK8V2_Top_W_SFs.csv'
SFdict={}
##SFdict['W']['2016']['Nominal']['0p5']['200']['300']['SF']
csv_file=open(filename)
print "Read ",filename
csv_reader = csv.reader(csv_file, delimiter=',')
line_count = 0
nameidxlist=[]
valueidxlist=[]
for row in csv_reader:

    if line_count==0: ##name of each column
        #['DeepAK8_V2Training; Object', ' Year', ' version', ' MistaggingRate[%]', ' pT_low[GeV]', ' pT_high[GeV]', ' SF', ' SF_lowerErr', ' SF_upperErr']
        #['W', ' 2016', ' Nominal', ' 0p5', ' 200', ' 300', ' 1.04', ' 0.09', ' 0.10']
        idx=0
        for name in row:
            #print name
            if not 'SF' in name:
                nameidxlist.append(idx)
            else:
                valueidxlist.append(idx)
            idx+=1
        #print "nameidxlist=",nameidxlist
        #print "valueidxlist=",valueidxlist
    else: ##not line_cout==0
        #namelist=[]
        #valuenamelist=[]
        idx=0
        suffix=''
        #print 'nameidxlist=',nameidxlist
        for name in row:
            name=name.replace(' ','')
            #print idx,name,'idx in nameidxlist=',idx in nameidxlist
            if idx in nameidxlist:
                #print 'suffix=',suffix
                check='if not "'+name+'" in SFdict'+suffix+':'
                suffix+="['"+name+"']"
                exec(check+"SFdict"+suffix+'={}')
            elif idx in valueidxlist:

                if idx==valueidxlist[0]:
                    
                    exec("SFdict"+suffix+'=[]')
                #print "SFdict"+suffix+'='+name
                #if 'W' in suffix:print("SFdict"+suffix+'.append('+name+')')
                exec("SFdict"+suffix+'.append('+name+')')
                    
            idx+=1
        #for name in valuenamelist:
        #    exec("SFdict"+suffix+'["'+name+'"]=')
    line_count+=1

#print SFdict['W']['2016']['Nominal']['0p5']['200']['300']



def Print1yr(YEAR,WP,VERSION):

    #YEAR='2018'
    #WP='0p5'
    #VERSION='Nominal'
    
    #DeepAK8WP5
    BranchName=''
    if VERSION=='Nominal':BranchName+='DeepAK8WP'+WP
    if VERSION=='MassDecorr': BranchName+='DeepAK8WP'+WP+'MD'
    BranchName=BranchName.replace('p0','')
    #print '--',YEAR,'--'
    #print BranchName
    #WtaggerFatjet_DeepAK8WP5_nom_pt
    #[1.04, 0.09, 0.1]# nom down up
    
    nom200300=SFdict['W'][YEAR][VERSION][WP]['200']['300'][0]
    nom300400=SFdict['W'][YEAR][VERSION][WP]['300']['400'][0]
    nom400800=SFdict['W'][YEAR][VERSION][WP]['400']['800'][0]
    nom800=SFdict['W'][YEAR][VERSION][WP]['400']['800'][0]
    
    up200300=float(nom200300+SFdict['W'][YEAR][VERSION][WP]['200']['300'][2])
    up300400=float(nom300400+SFdict['W'][YEAR][VERSION][WP]['300']['400'][2])
    up400800=float(nom400800+SFdict['W'][YEAR][VERSION][WP]['400']['800'][2])
    up800=float(nom400800+SFdict['W'][YEAR][VERSION][WP]['400']['800'][2])
    
    
    down200300=float(nom200300-SFdict['W'][YEAR][VERSION][WP]['200']['300'][1])
    down300400=float(nom300400-SFdict['W'][YEAR][VERSION][WP]['300']['400'][1])
    down400800=float(nom400800-SFdict['W'][YEAR][VERSION][WP]['400']['800'][1])
    down800=float(nom400800-SFdict['W'][YEAR][VERSION][WP]['400']['800'][1])
    
    #print
    print "WJID['"+YEAR+"']['"+BranchName+"']['effSF']={"
    print'''
    'nom':'\
    (WtaggerFatjet_{12}_nom_pt>=200 && WtaggerFatjet_{12}_nom_pt<300 )*{0}+\\
    (WtaggerFatjet_{12}_nom_pt>=300 && WtaggerFatjet_{12}_nom_pt<400 )*{1}+\\
    (WtaggerFatjet_{12}_nom_pt>=400 && WtaggerFatjet_{12}_nom_pt<800 )*{2}+\\
    (WtaggerFatjet_{12}_nom_pt>=800)*{3}\\
    ',
    'up':'\
    (WtaggerFatjet_{12}_nom_pt>=200 && WtaggerFatjet_{12}_nom_pt<300 )*{4}+\\
    (WtaggerFatjet_{12}_nom_pt>=300 && WtaggerFatjet_{12}_nom_pt<400 )*{5}+\\
    (WtaggerFatjet_{12}_nom_pt>=400 && WtaggerFatjet_{12}_nom_pt<800 )*{6}+\\
    (WtaggerFatjet_{12}_nom_pt>=800)*{7}\\
    ',
    'down':'\
    (WtaggerFatjet_{12}_nom_pt>=200 && WtaggerFatjet_{12}_nom_pt<300 )*{8}+\\
    (WtaggerFatjet_{12}_nom_pt>=300 && WtaggerFatjet_{12}_nom_pt<400 )*{9}+\\
    (WtaggerFatjet_{12}_nom_pt>=400 && WtaggerFatjet_{12}_nom_pt<800 )*{10}+\\
    (WtaggerFatjet_{12}_nom_pt>=800)*{11}\\
    ',\
    \
    '''.format(nom200300,nom300400,nom400800,nom800,up200300,up300400,up400800,up800,down200300,down300400,down400800,down800,BranchName,YEAR)
    print "}"



for YEAR in ['2018','2017','2016']:
    for WP in ['0p5','1p0','2p5','5p0']:
        for VERSION in ['Nominal','MassDecorr']:
            Print1yr(YEAR,WP,VERSION)

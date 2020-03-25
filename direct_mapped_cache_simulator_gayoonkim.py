import math

#direct-mapped cache
#block size= 1 word
# number of cache blocks = 128

#about input address
n=128 #number of blocks in a cache
m=1 #number of words in a block
addrss=[] #save the address from input file 
hexa=[] #save the 32bit address
cchad=[] #input cache index
tg=[] #input tag
cindex=range(0,128) #block index


infile=input('cache_simulator ')
f=open(infile,'r')

lines=f.readlines()
f.close()
for line in lines:
    a=line.replace('\n','')
    addrss.append(a)

for i in range(len(addrss)): #change 16bit address to 32bit
    b='{0:032b}'.format(int(addrss[i], 16))
    hexa.append(b)


for j in hexa: #making block address
    cchad.append(j[23:30]) #cache index
    tg.append(j[:23]) #tag

dec=[]
for a in cchad:
    b=int(a,2)
    dec.append(b)
    
#Frame of Direct mapped cache
from pandas import DataFrame
cindex=range(0,128) #cache index in cache
cache=DataFrame(columns=['valid','tag'], index=cindex)
cache['valid']=0

#for the writing test.out
output=[]
chit=0
cmiss=0

#Simulation of a direct-mapped cache

for i in range(len(dec)):
    for j in range(128):
        if dec[i]==cache.index[j] and cache.valid[j]==1 and tg[i]==cache.tag[j]:
            chit+=1
            output.append('hit')
        elif dec[i]==cache.index[j] and cache.valid[j]==1 and tg[i]!=cache.tag[j]:
            cmiss+=1
            cache.loc[j,'tag']=tg[i]
            output.append('miss')
        elif dec[i]==cache.index[j] and cache.valid[j]!=1: #update the valid bit and tag
            cmiss+=1
            output.append('miss')
            cache.loc[j,'valid']=1
            cache.loc[j,'tag']=tg[i]

#print the simulation result on excel file
f=open(infile[:-4]+'.out.csv','w')
for a in range(len(addrss)):
    f.write(addrss[a])
    f.write(' ')
    f.write(output[a])
    f.write('\n')
       
f.write('# of cache hits\n')
f.write(str(chit))
f.write('\n')
f.write('# of cache misses\n')
f.write(str(cmiss))
f.write('\n')
f.close()

import copy;  from collections import Counter; import sys;


## infile: is one that include the information collateral sensitivity profile of each drug
## outfile: this will be the outputfile that have all possible cycles
## maxLimit: this is the maximum limit if you choice to a maximum number of drugs per cycles. if not sure just make the largest possible

infile=sys.argv[1]; outfile=sys.argv[2]; maxLimit=sys.argv[3];
#print infile , outfile, maxLimit,  ## read file 

drugDicMap={}; header=True;

with open(infile) as FileObj:
    for line in FileObj:
        if header : 
            header=False;
            continue
        line=line.replace("\n","");
        result=line.split("\t")
        if len(result) == 2 :            
            if result[0] in drugDicMap.keys():   
                drugDicMap[result[0]].append(result[1])
            else:   
                drugDicMap[result[0]] = [result[1]]

lst=drugDicMap.keys();

def getDrugCycles(prefix,currentItem, drugMap,  maxLimit, fileWriter):
    if len(prefix) == maxLimit: return ;
    
    for item in drugMap[currentItem]:
        if item in drugMap.keys():
            result=Counter(prefix)
            for i in result.keys():                
                if result[i] > 1 :  return;
            prefix1=prefix+[item]
            if (prefix1[0] == item) :
                str="";  
                for x in prefix1: str=str+","+x;   
                str=str+"\n";  fileWriter.write(str)
            getDrugCycles(prefix1, item,drugMap, maxLimit,fileWriter)

items=[]; 
fileWriter=open(outfile,'w')
for i in drugDicMap.keys():  getDrugCycles(items,i, drugDicMap, maxLimit, fileWriter)
fileWriter.close()
    




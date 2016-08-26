

inputFile=$1;
maxSize=$2

python $workspace/CollateralSensitivityDrugCycling/DrugCycleDetector.py $inputFile $inputFile.list 15
        
sort -u  $inputFile.list  | sed 's/^,//g' | awk -F"," '{if($1==$NF && NF>2) print NF-1"\t"$0}'   | sort -n > $inputFile.cycleSize.DrugCycles.txt

cut -f1  $inputFile.cycleSize.DrugCycles.txt | sort | uniq -c   | awk '{print $2"\t"$1}' | sort -n | 
awk '{if(FNR==1) print "CycleSize\tNumberOfCycles"; print $0}' > $inputFile.summary.txt

#!/bin/bash
#This script takes in a file with a full list of transcriptions formatted as per the Sphinx documentation 
# with the filnames in parentheses.  The script assumes that all audio files are in the same level directory and end in .wav. 
# The script uses 10-fold cross validation to create training and test sets.

clear
echo "Removing prior files"
rm train_1.transcription
rm train_1.fileids 
rm test_1.txt 
#rm train_2.txt 
#rm train_3.txt 
#rm train_4.txt 
#rm train_5.txt 
#rm train_6.txt 
#rm train_7.txt 
#rm train_8.txt 
#rm train_9.txt 
#rm train_10.txt 
#rm test_2.txt 
#rm test_3.txt 
#rm test_4.txt 
#rm test_5.txt 
#rm test_6.txt 
#rm test_7.txt 
#rm test_8.txt 
#rm test_9.txt 
#rm test_10.txt 

echo "Creating training and test sets"

# calculate number of lines in each test set
typeset -i totalLines
totalLines=`cat "${1}.txt" | wc -l` 
typeset -i linesPerSubset
linesPerSubset=$((totalLines / 10)) 

# create test and train sets
#1. shuffle text file
#2. divide lines into 10 pieces
#3. loop through all lines in file.  place line into files based on what number it is

gshuf ${1}.txt >> shuffled.txt

typeset -i i
i=0
while IFS='' read -r line || [[ -n "$line" ]]; do
	i=$(( $i + 1 ))
	if [ $i -gt $linesPerSubset ]
	then
		echo "$line" >> "train_1.transcription"
		if [[ $line =~ \((.+)\) ]]; then
    			matchWithParens=${BASH_REMATCH[1]}
			echo ${matchWithParens} >> train_1.fileids
		else
    			echo "unable to parse string $strname"
		fi
	else 
		echo "$line" >> "test_1.txt"
	fi
done < "shuffled.txt"

rm shuffled.txt

echo "training model"

sphinx_fe -argfile en-us/feat.params \
        -samprate 16000 -c train_1.fileids \
       -di . -do . -ei wav -eo mfc -mswav yes

./bw \
 -hmmdir en-us \
 -moddeffn en-us/mdef.txt \
 -ts2cbfn .ptm. \
 -feat 1s_c_d_dd \
 -svspec 0-12/13-25/26-38 \
 -cmn current \
 -agc none \
 -dictfn cmudict-en-us.dict \
 -ctlfn train_1.fileids \
 -lsnfn train_1.transcription \
 -accumdir .

./mllr_solve \
    -meanfn en-us/means \
    -varfn en-us/variances \
    -outmllrfn mllr_matrix -accumdir .

cp -a en-us en-us-adapt

./map_adapt \
    -moddeffn en-us/mdef.txt \
    -ts2cbfn .ptm. \
    -meanfn en-us/means \
    -varfn en-us/variances \
    -mixwfn en-us/mixture_weights \
    -tmatfn en-us/transition_matrices \
    -accumdir . \
    -mapmeanfn en-us-adapt/means \
    -mapvarfn en-us-adapt/variances \
    -mapmixwfn en-us-adapt/mixture_weights \
    -maptmatfn en-us-adapt/transition_matrices

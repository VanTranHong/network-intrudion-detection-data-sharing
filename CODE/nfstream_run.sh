# declare -a StringArray=("Wednesday-14-02-2018" "Wednesday-21-02-2018" "Wednesday-28-02-2018" "Thursday-01-03-2018" "Thursday-15-02-2018" "Thursday-22-02-2018" "Friday-16-02-2018" "Friday-23-02-2018")
# declare -a StringArray=("Tuesday-20-02-2018")
declare -a StringArray=("Monday" "Tuesday" "Wednesday" "Thursday" "Friday")
 
# Iterate the string array using for loop
for val in ${StringArray[@]}
do
   python nfstream_extract.py --day $val --year 2017 &
#     echo $val
done;

wait 
echo "All done"

grep Err -r $1 --exclude="*.py"
grep ERROR -r $1 --exclude="*.py"
echo "Number of total jobs"
ls $1/*.sh |wc -l
echo "finished jobs"
ls $1/*.done |wc -l

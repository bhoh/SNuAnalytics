
COMBINE_BASE=/cms/ldap_home/bhoh/HiggsCombTool/CMSSW_10_6_4/src/HiggsAnalysis/CombinedLimit/python
SCRIPT_BASE=${PWD}
MODLE_FILE_NAME=ChargedHiggsCB.py

echo $COMBINE_BASE
echo $SCRIPT_BASE

if [[ -f "$COMBINE_BASE/$MODLE_FILE_NAME" ]]
then
    rm $COMBINE_BASE/$MODLE_FILE_NAME
fi

ln -s $SCRIPT_BASE/$MODLE_FILE_NAME $COMBINE_BASE/$MODLE_FILE_NAME


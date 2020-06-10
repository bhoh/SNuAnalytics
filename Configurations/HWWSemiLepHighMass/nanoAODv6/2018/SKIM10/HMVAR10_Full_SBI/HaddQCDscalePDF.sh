StartTime=$(date +%s)
##
BOOST=(Boosted Resolved)
for bst in ${BOOST[@]};do
    dir=`ls -d rootFile_*${bst}*/`
    mkdir -p $dir/Combined

    pushd $dir/Combined/
    mkdir -p temp/
    mkdir -p qcdscale_pdf_only/
    (hadd -f -j 10 -d temp/ qcdscale_pdf_only/qcdscale_pdf_only.root ../QCDscaleAccept/*.root ../pdfAccept/*.root;hadd -f -j 10 -d temp/ hadd_combined.root qcdscale_pdf_only/qcdscale_pdf_only.root ../hadd.root)
    
    popd

done


EndTime=$(date +%s)
echo $EndTime
echo "runtime : $(($EndTime - $StartTime)) sec"

pushd plots_semilep_Resolved/
getidx
popd
tar -cf plots_semilep_Resolved.tar plots_semilep_Resolved/
scp plots_semilep_Resolved.tar jhchoi@147.47.242.40:/home/jhchoi/www/HWW/plots/Resolved/

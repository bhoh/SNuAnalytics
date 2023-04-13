#Plot2018_220322

rsync -arv $1 boh@lxplus.cern.ch:/eos/user/b/boh/www/nanoV9/$2
ssh boh@lxplus.cern.ch cp /eos/user/b/boh/www/nanoV9/index.php /eos/user/b/boh/www/nanoV9/$2/index.php
#copy to all sub directories
#ssh boh@lxplus.cern.ch for d in /eos/user/b/boh/www/nanoV9/$2/*; do cp /eos/user/b/boh/www/nanoV9/index.php "$d"; done
ssh boh@lxplus.cern.ch 'for d in /eos/user/b/boh/www/nanoV9/$2/*/; do cp /eos/user/b/boh/www/nanoV9/index.php "$d/index.php"; done'
ssh boh@lxplus.cern.ch 'for d in /eos/user/b/boh/www/nanoV9/$2/*/*/; do cp /eos/user/b/boh/www/nanoV9/index.php "$d/index.php"; done'


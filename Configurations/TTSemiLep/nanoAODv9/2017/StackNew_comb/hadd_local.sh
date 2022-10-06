
[ ! -d $1 ] && mkdir $1
[ -d /cms_scratch/bhoh/$1 ] && hadd -d /cms_scratch/bhoh/ -j 20 $1/hadd.root /cms_scratch/bhoh/$1/*.root

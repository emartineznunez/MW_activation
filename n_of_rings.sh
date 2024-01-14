nofm=$(awk '{if(NF==2) n=$1};/Conformational/{print n;exit}' FINAL_LL_P/MINinfo )
for i in $(seq $nofm)
do
  echo 57 > mingeom
  echo "" >> mingeom
  select.sh FINAL_LL_P geom min $i >> mingeom
  echo MIN $i
  n_of_rings.py mingeom
done

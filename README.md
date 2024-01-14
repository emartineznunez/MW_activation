# AutoMeKin

<p align="center">
   <img src="logo.png" alt="alt text" width="400" height="200">
</p>

AutoMeKin is employed in this example to study a MW-activated chemical reaction.

FINAL_LL_P contains the results after 12 iterations when MD sampling is used exciting a subset of atoms.

This script shows how to create an interactive html with amk_tools (https://github.com/dgarayr/amk_tools) from int1 (MIN13) and int2 (MIN53):

<code>amk_gen_view.py FINAL_LL_P/ RXNet.cg --cutoff_path 10  --paths MIN13  MIN53 </code>

To run the test type:

<code>nohup llcalcs.sh P.dat 30 10 30 > llcalcs.log 2>&1 & </code>

The ouput file will be named network.html

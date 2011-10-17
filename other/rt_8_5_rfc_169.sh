#/bin/sh 

cv=$1
pv=$2

# change . and - with _
ncv=`echo $cv | sed -e 's/\./_/g' | sed -e 's/\-/_/g'`
# remove age from cv
cr=`echo $cv | awk -F"-" '{ print $1 }'`

echo 'Name: No xmlrpc-c RPMs'
#echo 'RT 8.5 RFC https://storm.cnaf.infn.it:8443/redmine/issues/169'

echo 'Description: The distribution of xmlrpc-c RPMs on SL5 contains a memory leask that affects the StoRM Frontend Server.'

echo 'Output:'

echo 'mkdir -p storm-xmlrpc-c'
mkdir -p storm-storm-xmlrpc-c &> /tmp/rt_8_5_rfc_169.txt 

echo 'cd storm-xmlrpc-c/'
cd storm-xmlrpc-c/ &> /tmp/rt_8_5_rfc_169.txt

echo 'etics-workspace-setup'
etics-workspace-setup &> /tmp/rt_8_5_rfc_169.txt

echo 'etics-get-project --noask emi'
etics-get-project --noask emi &> /tmp/rt_8_5_rfc_169.txt

echo etics-checkout --platform "sl5_x86_64_gcc412EPEL" --verbose --noask --project "emi" --project-config emi_R_$pv\_rc --config emi-storm-xmlrpc-c_stable_1_25 emi.storm.xmlrpc-c
etics-checkout --platform "sl5_x86_64_gcc412EPEL" --verbose --noask --project "emi" --project-config emi_R_$pv\_rc --config emi-storm-xmlrpc-c_stable_1_25 emi.storm.xmlrpc-c &> /tmp/rt_8_5_rfc_169.txt

echo etics-build --createsource --platform "sl5_x86_64_gcc412EPEL" --verbose --config emi-storm-xmlrpc-c_stable_1_25 emi.storm.xmlrpc-c
etics-build --platform "sl5_x86_64_gcc412EPEL" --verbose --config emi-storm-xmlrpc-c_stable_1_25 emi.storm.xmlrpc-c &> /tmp/rt_8_5_rfc_169.txt

echo ls dist/emi/emi.storm.xmlrpc-c/$cr/sl5_x86_64_gcc412EPEL/storm-xmlrpc-c-$cv.sl5.x86_64.rpm
a=`ls dist/emi/emi.storm.xmlrpc-c/$cr/sl5_x86_64_gcc412EPEL/storm-xmlrpc-c-$cv.sl5.x86_64.rpm`

echo ls dist/emi/emi.storm.xmlrpc-c/$cr/sl5_x86_64_gcc412EPEL/storm-xmlrpc-c-apps-$cv.sl5.x86_64.rpm
b=`ls dist/emi/emi.storm.xmlrpc-c/$cr/sl5_x86_64_gcc412EPEL/storm-xmlrpc-c-apps-$cv.sl5.x86_64.rpm`

echo ls dist/emi/emi.storm.xmlrpc-c/$cr/sl5_x86_64_gcc412EPEL/storm-xmlrpc-c-c++-$cv.sl5.x86_64.rpm
c=`ls dist/emi/emi.storm.xmlrpc-c/$cr/sl5_x86_64_gcc412EPEL/storm-xmlrpc-c-c++-$cv.sl5.x86_64.rpm`

echo ls dist/emi/emi.storm.xmlrpc-c/$cr/sl5_x86_64_gcc412EPEL/storm-xmlrpc-c-client-$cv.sl5.x86_64.rpm
d=`ls dist/emi/emi.storm.xmlrpc-c/$cr/sl5_x86_64_gcc412EPEL/storm-xmlrpc-c-client-$cv.sl5.x86_64.rpm`

echo ls dist/emi/emi.storm.xmlrpc-c/$cr/sl5_x86_64_gcc412EPEL/storm-xmlrpc-c-client++-$cv.sl5.x86_64.rpm
e=`ls dist/emi/emi.storm.xmlrpc-c/$cr/sl5_x86_64_gcc412EPEL/storm-xmlrpc-c-client++-$cv.sl5.x86_64.rpm`

echo ls dist/emi/emi.storm.xmlrpc-c/$cr/sl5_x86_64_gcc412EPEL/storm-xmlrpc-c-devel-$cv.sl5.x86_64.rpm
f=`ls dist/emi/emi.storm.xmlrpc-c/$cr/sl5_x86_64_gcc412EPEL/storm-xmlrpc-c-devel-$cv.sl5.x86_64.rpm`

r=''
for x in $a $b $c $d $e $f
do
  echo $x | grep -q "x86_64" && r="PASSED" || r="FAILD"
  if [ $r = "FAILD" ]
  then
    echo $r
    break
  fi
done
rm /tmp/rt_8_5_rfc_169.txt

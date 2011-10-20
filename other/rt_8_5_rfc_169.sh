#/bin/sh 

cv=$1
pv=$2

# change . and - with _
ncv=`echo $cv | sed -e 's/\./_/g' | sed -e 's/\-/_/g'`
# remove age from cv
cr=`echo $cv | awk -F"-" '{ print $1 }'`

#echo 'Name: No xmlrpc-c RPMs'

echo 'Description: The distribution of xmlrpc-c RPMs on SL5 contains a memory leask that affects the StoRM Frontend Server.'
echo 'RFC Unique ID: https://storm.cnaf.infn.it:8443/redmine/issues/169'

mkdir -p storm-xmlrpc-c &> /tmp/rt_8_5_rfc_169.txt 

cd storm-xmlrpc-c/ &> /tmp/rt_8_5_rfc_169.txt

etics-workspace-setup &> /tmp/rt_8_5_rfc_169.txt

etics-get-project --noask emi &> /tmp/rt_8_5_rfc_169.txt

etics-checkout --platform "sl5_x86_64_gcc412EPEL" --verbose --noask --project "emi" --project-config emi_R_$pv\_rc --config emi-storm-xmlrpc-c_stable_1_25_new emi.storm.xmlrpc-c &> /tmp/rt_8_5_rfc_169.txt

etics-build --platform "sl5_x86_64_gcc412EPEL" --verbose --config emi-storm-xmlrpc-c_stable_1_25_new emi.storm.xmlrpc-c &> /tmp/rt_8_5_rfc_169.txt

a=`ls dist/emi/emi.storm.xmlrpc-c/$cr/sl5_x86_64_gcc412EPEL/storm-xmlrpc-c-$cv.sl5.x86_64.rpm`

b=`ls dist/emi/emi.storm.xmlrpc-c/$cr/sl5_x86_64_gcc412EPEL/storm-xmlrpc-c-apps-$cv.sl5.x86_64.rpm`

c=`ls dist/emi/emi.storm.xmlrpc-c/$cr/sl5_x86_64_gcc412EPEL/storm-xmlrpc-c-c++-$cv.sl5.x86_64.rpm`

d=`ls dist/emi/emi.storm.xmlrpc-c/$cr/sl5_x86_64_gcc412EPEL/storm-xmlrpc-c-client-$cv.sl5.x86_64.rpm`

e=`ls dist/emi/emi.storm.xmlrpc-c/$cr/sl5_x86_64_gcc412EPEL/storm-xmlrpc-c-client++-$cv.sl5.x86_64.rpm`

f=`ls dist/emi/emi.storm.xmlrpc-c/$cr/sl5_x86_64_gcc412EPEL/storm-xmlrpc-c-devel-$cv.sl5.x86_64.rpm`

r=''
for x in $a $b $c $d $e $f
do
  echo $x | grep -q "x86_64" && r="PASSED" || r="FAILD"
  if [ $r = "RESULT: FAILD" ]
  then
    echo $r
    break
  fi
done
echo 'RESULT: PASSED'

echo 'Output:'

echo 'mkdir -p storm-xmlrpc-c'
echo 'cd storm-xmlrpc-c/'
echo 'etics-workspace-setup'
echo 'etics-get-project --noask emi'
echo etics-checkout --platform "sl5_x86_64_gcc412EPEL" --verbose --noask --project "emi" --project-config emi_R_$pv\_rc --config emi-storm-xmlrpc-c_stable_1_25_new emi.storm.xmlrpc-c
echo etics-build --createsource --platform "sl5_x86_64_gcc412EPEL" --verbose --config emi-storm-xmlrpc-c_stable_1_25_new emi.storm.xmlrpc-c
echo ls dist/emi/emi.storm.xmlrpc-c/$cr/sl5_x86_64_gcc412EPEL/storm-xmlrpc-c-$cv.sl5.x86_64.rpm
echo ls dist/emi/emi.storm.xmlrpc-c/$cr/sl5_x86_64_gcc412EPEL/storm-xmlrpc-c-apps-$cv.sl5.x86_64.rpm
echo ls dist/emi/emi.storm.xmlrpc-c/$cr/sl5_x86_64_gcc412EPEL/storm-xmlrpc-c-c++-$cv.sl5.x86_64.rpm
echo ls dist/emi/emi.storm.xmlrpc-c/$cr/sl5_x86_64_gcc412EPEL/storm-xmlrpc-c-client-$cv.sl5.x86_64.rpm
echo ls dist/emi/emi.storm.xmlrpc-c/$cr/sl5_x86_64_gcc412EPEL/storm-xmlrpc-c-client++-$cv.sl5.x86_64.rpm
echo ls dist/emi/emi.storm.xmlrpc-c/$cr/sl5_x86_64_gcc412EPEL/storm-xmlrpc-c-devel-$cv.sl5.x86_64.rpm

rm /tmp/rt_8_5_rfc_169.txt

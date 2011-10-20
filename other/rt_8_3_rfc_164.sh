#/bin/sh 

cv=$1
pv=$2

# change . and - with _
ncv=`echo $cv | sed -e 's/\./_/g' | sed -e 's/\-/_/g'`
# remove age from cv
cr=`echo $cv | awk -F"-" '{ print $1 }'`

#echo 'Name: No StoRM Backend Server Src RPM'

echo 'Description: The source RPM of the storm-backend-server component is not created at build time.'
echo 'RFC Unique ID: https://storm.cnaf.infn.it:8443/redmine/issues/164'

mkdir -p storm-backend-server &> /tmp/rt_8_3_rfc_164.txt 

cd storm-backend-server/ &> /tmp/rt_8_3_rfc_164.txt

etics-workspace-setup &> /tmp/rt_8_3_rfc_164.txt

etics-get-project --noask emi &> /tmp/rt_8_3_rfc_164.txt

etics-checkout --platform "sl5_x86_64_gcc412EPEL" --verbose --noask --project "emi" --project-config emi_R_$pv\_rc --config emi-storm-backend-server_R_$ncv emi.storm.backend-server &> /tmp/rt_8_3_rfc_164.txt

etics-build --platform "sl5_x86_64_gcc412EPEL" --verbose --config emi-storm-backend-server_R_$ncv emi.storm.backend-server &> /tmp/rt_8_3_rfc_164.txt

a=`ls dist/emi/emi.storm.backend-server/$cr/src/storm-backend-server-$cv.sl5.src.rpm`

echo $a | grep -q "src" && echo "RESULT: PASSED" || echo "RESULT: FAILD"

echo 'Output:'

echo 'mkdir -p storm-backend-server'
echo 'cd storm-backend-server/'
echo 'etics-workspace-setup'
echo 'etics-get-project --noask emi'
echo etics-checkout --platform "sl5_x86_64_gcc412EPEL" --verbose --noask --project "emi" --project-config emi_R_$pv\_rc --config emi-storm-backend-server_R_$ncv emi.storm.backend-server
echo etics-build --createsource --platform "sl5_x86_64_gcc412EPEL" --verbose --config emi-storm-backend-server_R_$ncv emi.storm.backend-server
echo ls dist/emi/emi.storm.backend-server/$cr/src/storm-backend-server-$cv.sl5.src.rpm

rm /tmp/rt_8_3_rfc_164.txt

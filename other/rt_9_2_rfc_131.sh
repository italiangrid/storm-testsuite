#/bin/sh 

cv=$1
pv=$2

# change . and - with _
ncv=`echo $cv | sed -e 's/\./_/g' | sed -e 's/\-/_/g'`
# remove age from cv
cr=`echo $cv | awk -F"-" '{ print $1 }'`

#echo 'Name: Non Compliant StoRM GridHttps Server RPM name'

echo 'Description: The RPM binary name of the storm-gridhttps-server component does not contain architecture after the OS name.'
echo 'RFC Unique ID: https://storm.cnaf.infn.it:8443/redmine/issues/131'

mkdir -p storm-gridhttps-server &> /tmp/rt_9_2_rfc_131.txt 

cd storm-gridhttps-server/ &> /tmp/rt_9_2_rfc_131.txt

etics-workspace-setup &> /tmp/rt_9_2_rfc_131.txt

etics-get-project --noask emi &> /tmp/rt_9_2_rfc_131.txt

etics-checkout --platform "sl5_x86_64_gcc412EPEL" --verbose --noask --project "emi" --project-config emi_R_$pv\_rc --config emi-storm-gridhttps-server_R_$ncv emi.storm.gridhttps-server &> /tmp/rt_9_2_rfc_131.txt

etics-build --platform "sl5_x86_64_gcc412EPEL" --verbose --config emi-storm-gridhttps-server_R_$ncv emi.storm.gridhttps-server &> /tmp/rt_9_2_rfc_131.txt

a=`ls dist/emi/emi.storm.gridhttps-server/$cr/sl5_x86_64_gcc412EPEL/storm-gridhttps-server-$cv.sl5.noarch.rpm`

echo $a | grep -q "noarch" && echo "RESULT: PASSED" || echo "RESULT: FAILD"

echo 'Output:'

echo 'mkdir -p storm-gridhttps-server'
echo 'cd storm-gridhttps-server/'
echo 'etics-workspace-setup'
echo 'etics-get-project --noask emi'
echo etics-checkout --platform "sl5_x86_64_gcc412EPEL" --verbose --noask --project "emi" --project-config emi_R_$pv\_rc --config emi-storm-gridhttps-server_R_$ncv emi.storm.gridhttps-server
echo etics-build --platform "sl5_x86_64_gcc412EPEL" --verbose --config emi-storm-gridhttps-server_R_$ncv emi.storm.gridhttps-server
echo ls dist/emi/emi.storm.gridhttps-server/$cr/sl5_x86_64_gcc412EPEL/storm-gridhttps-server-$cv.sl5.noarch.rpm

rm /tmp/rt_9_2_rfc_131.txt
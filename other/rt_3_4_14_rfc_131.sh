#/bin/sh 

cv=$1
pv=$2

# change . and - with _
ncv=`echo $cv | sed -e 's/\./_/g' | sed -e 's/\-/_/g'`
# remove age from cv
cr=`echo $cv | awk -F"-" '{ print $1 }'`

echo 'RT 3.4.14 RFC https://storm.cnaf.infn.it:8443/redmine/issues/131'

echo 'mkdir -p storm-gridhttps-server'
mkdir -p storm-gridhttps-server &> /tmp/rt_3.3.14_rfc_131.txt 

echo 'cd storm-gridhttps-server/'
cd storm-gridhttps-server/ &> /tmp/rt_3.3.14_rfc_131.txt

echo 'etics-workspace-setup'
etics-workspace-setup &> /tmp/rt_3.3.14_rfc_131.txt

echo 'etics-get-project --noask emi'
etics-get-project --noask emi &> /tmp/rt_3.3.14_rfc_131.txt

echo etics-checkout --platform "sl5_x86_64_gcc412EPEL" --verbose --noask --project "emi" --project-config emi_R_$pv\_rc --config emi-storm-gridhttps-server_R_$ncv emi.storm.gridhttps-server
etics-checkout --platform "sl5_x86_64_gcc412EPEL" --verbose --noask --project "emi" --project-config emi_R_$pv\_rc --config emi-storm-gridhttps-server_R_$ncv emi.storm.gridhttps-server &> /tmp/rt_3.3.14_rfc_131.txt

echo etics-build --platform "sl5_x86_64_gcc412EPEL" --verbose --config emi-storm-gridhttps-server_R_$ncv emi.storm.gridhttps-server
etics-build --platform "sl5_x86_64_gcc412EPEL" --verbose --config emi-storm-gridhttps-server_R_$ncv emi.storm.gridhttps-server &> /tmp/rt_3.3.14_rfc_131.txt

echo ls dist/emi/emi.storm.gridhttps-server/$cr/sl5_x86_64_gcc412EPEL/storm-gridhttps-server-$cv.sl5.noarch.rpm
a=`ls dist/emi/emi.storm.gridhttps-server/$cr/sl5_x86_64_gcc412EPEL/storm-gridhttps-server-$cv.sl5.noarch.rpm`

echo $a | grep -q "noarch" && echo "PASS" || echo "FAIL"
rm /tmp/rt_3.3.14_rfc_131.txt
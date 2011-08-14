#/bin/sh 

echo 'RT 3.3.14 RFC https://storm.cnaf.infn.it:8443/redmine/issues/131'

echo 'mkdir -p storm-gridhttps-server'
mkdir -p storm-gridhttps-server &> /tmp/rt_3.3.14_rfc_131.txt 

echo 'cd storm-gridhttps-server/'
cd storm-gridhttps-server/ &> /tmp/rt_3.3.14_rfc_131.txt

echo 'etics-workspace-setup'
etics-workspace-setup &> /tmp/rt_3.3.14_rfc_131.txt

echo 'etics-get-project emi'
etics-get-project emi &> /tmp/rt_3.3.14_rfc_131.txt

echo 'etics-checkout --platform "sl5_x86_64_gcc412EPEL" --verbose --project "emi" --project-config emi_R_1_rc --config emi-storm-gridhttps-server_R_1_0_4_1 emi.storm.gridhttps-server'
etics-checkout --platform "sl5_x86_64_gcc412EPEL" --verbose --project "emi" --project-config emi_R_1_rc --config emi-storm-gridhttps-server_R_1_0_4_1 emi.storm.gridhttps-server &> /tmp/rt_3.3.14_rfc_131.txt

echo 'etics-build --platform "sl5_x86_64_gcc412EPEL" --verbose --config emi-storm-gridhttps-server_R_1_0_4_1 emi.storm.gridhttps-server'
etics-build --platform "sl5_x86_64_gcc412EPEL" --verbose --config emi-storm-gridhttps-server_R_1_0_4_1 emi.storm.gridhttps-server &> /tmp/rt_3.3.14_rfc_131.txt

echo 'ls dist/emi/emi.storm.gridhttps-server/1.0.4/sl5_x86_64_gcc412EPEL/storm-gridhttps-server-1.0.4-1.sl5.noarch.rpm'
a=`ls dist/emi/emi.storm.gridhttps-server/1.0.4/sl5_x86_64_gcc412EPEL/storm-gridhttps-server-1.0.4-1.sl5.noarch.rpm`

echo $a | grep -q "noarch" && echo "PASS" || echo "FAIL"
#rm /tmp/rt_3.3.14_rfc_131.txt

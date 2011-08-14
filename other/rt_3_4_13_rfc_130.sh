#/bin/sh 

echo 'RT 3.3.13 RFC https://storm.cnaf.infn.it:8443/redmine/issues/130'

echo 'mkdir -p storm-gridhttps-plugin'
mkdir -p storm-gridhttps-plugin &> /tmp/rt_3.3.13_rfc_130.txt 

echo 'cd storm-gridhttps-plugin/'
cd storm-gridhttps-plugin/ &> /tmp/rt_3.3.13_rfc_130.txt

echo 'etics-workspace-setup'
etics-workspace-setup &> /tmp/rt_3.3.13_rfc_130.txt

echo 'etics-get-project emi'
etics-get-project emi &> /tmp/rt_3.3.13_rfc_130.txt

echo 'etics-checkout --platform "sl5_x86_64_gcc412EPEL" --verbose --project "emi" --project-config emi_R_1_rc --config emi-storm-gridhttps-plugin_R_1_0_2_1 emi.storm.gridhttps-plugin'
etics-checkout --platform "sl5_x86_64_gcc412EPEL" --verbose --project "emi" --project-config emi_R_1_rc --config emi-storm-gridhttps-plugin_R_1_0_2_1 emi.storm.gridhttps-plugin &> /tmp/rt_3.3.13_rfc_130.txt

echo 'etics-build --platform "sl5_x86_64_gcc412EPEL" --verbose --config emi-storm-gridhttps-plugin_R_1_0_2_1 emi.storm.gridhttps-plugin'
etics-build --platform "sl5_x86_64_gcc412EPEL" --verbose --config emi-storm-gridhttps-plugin_R_1_0_2_1 emi.storm.gridhttps-plugin &> /tmp/rt_3.3.13_rfc_130.txt

echo 'ls dist/emi/emi.storm.gridhttps-plugin/1.0.2/sl5_x86_64_gcc412EPEL/storm-gridhttps-plugin-1.0.2-1.sl5.noarch.rpm'
a=`ls dist/emi/emi.storm.gridhttps-plugin/1.0.2/sl5_x86_64_gcc412EPEL/storm-gridhttps-plugin-1.0.2-1.sl5.noarch.rpm`

echo $a | grep -q "noarch" && echo "PASS" || echo "FAIL"
rm /tmp/rt_3.3.13_rfc_130.txt

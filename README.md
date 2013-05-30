# StoRM testsuite

## Requirements

### Robot Framework 

This testsuite uses [Robot Framework](https://code.google.com/p/robotframework/). For SL*, 
Robot Framework is not on a repository, and it is needed to manually install it

First install python 2.6

	yum install python 26

then download Robot (actually 2.7.7 is the latest version) and install it:

	wget https://robotframework.googlecode.com/files/robotframework-2.7.7.tar.gz
	tar -xzf robotframework-2.7.7.tar.gz
	cd robotframework-2.7.7
	sudo python26 setup.py install

### Repositories

You need [EGI-trustanchors](http://repository.egi.eu/sw/production/cas/1/current/repo-files/EGI-trustanchors.repo) repo installed on your host. Download it and move it into /etc/yum.repos.d/ directory. Then launch:

	yum clean all

Install also the latest EMI repositories (you can find the latest SL5 or SL6 rpm [here](http://www.eu-emi.eu/emi-3-montebianco)):

	wget http://emisoft.web.cern.ch/emisoft/dist/EMI/3/sl6/x86_64/base/emi-release-3.0.0-2.el6.noarch.rpm
	yum localinstall --nogpgcheck emi-release-3.0.0-2.el6.noarch.rpm

in case of an SL6 installation.

### IGI-test-CA

Tests are made for IGI-test-CA signed certificates, so download [this](http://radiohead.cnaf.infn.it:9999/job/test-ca/os=SL5_x86_64/lastSuccessfulBuild/artifact/igi-test-ca/rpmbuild/RPMS/noarch/igi-test-ca-1.0.2-2.noarch.rpm) rpm and install it with rpm -ivh command.

	wget http://radiohead.cnaf.infn.it:9999/job/test-ca/os=SL5_x86_64/lastSuccessfulBuild/artifact/igi-test-ca/rpmbuild/RPMS/noarch/igi-test-ca-1.0.2-2.noarch.rpm
	rpm -ivh igi-test-ca-1.0.2-2.noarch.rpm

### Third-party clients and others

This testsuite needs to execute several clients' commands. For example, it needs to use commands of:

* StoRM clientSRM
* dCache srmclient
* LCG-utils
* ldap client
* VOMS client

So, including all the dependencies, the following packages have to be installed on testsuite host:

* java openjdk 1.6.0
* openldap-clients
* ca-policy-egi-core
* globus-gass-copy-progs
* emi-storm-srm-client-mp
* lcg-util
* voms-clients
* dcache-srmclient

Run:

	yum install java-1.6.0-openjdk openldap-clients ca-policy-egi-core globus-gass-copy-progs emi-storm-srm-client-mp lcg-util voms-clients dcache-srmclient

### VOMS clients

As seen before, the voms clients package installed, i.e. voms-proxy-* commands must be available. Actually, the testsuite needs to create a VOMS proxy for the testers.eu-emi.eu VO, so configure your VOMS client to satisfy this requirement (add the needed files to /etc/vomses and /etc/grid-security/vomsdir).

## Getting the testsuite 

You need git installed at this point. If it's not installed run:

	yum install git

Checkout the code using the following command:

	git clone https://github.com/italiangrid/storm-testsuite.git

## Run tests

Execute the Robot Framework command-line passing at least the storm backend hostname (a standalone deployment scenario):
        
	pybot --variable backEndHost:<your-BE-hostname> tests/

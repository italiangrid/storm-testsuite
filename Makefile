include Makefile.inc

PACKAGE := tstorm
VERSION=$(version)
RELEASE=$(release)
DISTBIN=$(distbin)
DISTSOURCE=$(distsource)
OS=$(os)

clean:
	rm -f *.pyc *.pyo
	rm -f tstorm/*.pyc tstorm/*.pyo
	rm -f tstorm/utils/*.pyc tstorm/utils/*.pyo
	rm -f tstorm/test/*.pyc tstorm/test/*.pyo
	rm -f *.tar.gz MANIFEST

srctar:
	python setup.py sdist -d .
	@echo "The src tar is in $(PACKAGE)-$(VERSION)-$(RELEASE).tar.gz"

bintar:
	python setup.py bdist -d .

SPECTSTORM=t-storm.spec
RPM_MAIN_DIR = $(PWD)/rpm
RPM_TMP_DIR = $(RPM_MAIN_DIR)/tmp
RPM_SOURCE = $(RPM_MAIN_DIR)/SOURCES
RPM_SPEC = $(RPM_MAIN_DIR)/SPECS
RPM_BUILD = $(RPM_MAIN_DIR)/BUILD
RPM_RPM = $(RPM_MAIN_DIR)/RPMS
RPM_SRPM = $(RPM_MAIN_DIR)/SRPMS
RPM_DIRS = $(RPM_MAIN_DIR) $(RPM_SOURCE) $(RPM_SPEC) $(RPM_BUILD) $(RPM_RPM) $(RPM_SRPM)
RPMBUILDOPTS = --define "_topdir $(RPM_MAIN_DIR)" --nodeps

rpmbuild: srctar
	mkdir -p $(RPM_DIRS)
	cp $(PACKAGE)-$(VERSION)-$(RELEASE).tar.gz $(RPM_SOURCE)
	cp $(SPECTSTORM) $(RPM_SPEC)
	rpmbuild \
        $(RPMBUILDOPTS) \
        -ba  $(RPM_SPEC)/$(SPECTSTORM)

distsrc:
	mkdir -p $(DISTSOURCE)
	mv $(PACKAGE)-$(VERSION)-$(RELEASE).tar.gz $(PACKAGE)-$(VERSION)-$(RELEASE).src.tar.gz
	cp $(PACKAGE)-$(VERSION)-$(RELEASE).src.tar.gz $(DISTSOURCE)/$(PACKAGE)-$(VERSION)-$(RELEASE).$(OS).src.tar.gz
	cp $(RPM_SRPM)/*.rpm $(DISTSOURCE)

distbin: bintar
	mkdir -p $(DISTBIN)
	mv $(PACKAGE)-$(VERSION)-$(RELEASE).linux*.tar.gz $(PACKAGE)-$(VERSION)-$(RELEASE).tar.gz
	cp $(PACKAGE)-$(VERSION)-$(RELEASE).tar.gz $(DISTBIN)/$(PACKAGE)-$(VERSION)-$(RELEASE).$(OS).tar.gz
	cp $(RPM_RPM)/*.rpm $(DISTBIN)

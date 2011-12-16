include Makefile.inc

PACKAGE := tstorm
VERSION=$(version)
RELEASE=$(release)

clean:
	rm -f *.pyc *.pyo
	rm -f tstorm/*.pyc tstorm/*.pyo
	rm -f tstorm/utils/*.pyc tstorm/utils/*.pyo
	rm -f tstorm/test/*.pyc tstorm/test/*.pyo
	rm -f *.tar.gz MANIFEST

srctar:
	python setup.py sdist -d .
	@echo "The src tar is in ${PACKAGE}-${VERSION}-${RELEASE}.tar.gz"

bintar:
	python setup.py bdist -d .
	@echo "The bin tar is in ${PACKAGE}-${VERSION}-${RELEASE}.tar.gz"

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
	cp $(PACKAGE)-$(VERSION)-${RELEASE}.tar.gz $(RPM_SOURCE)
	cp $(SPECTSTORM) $(RPM_SPEC)
	rpmbuild \
        $(RPMBUILDOPTS) \
        -ba  $(RPM_SPEC)/$(SPECTSTORM)

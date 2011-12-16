include Makefile.inc

PACKAGE := emi-t-storm
SPECVERSION=$(version)-$(release)

clean:
	rm -f *.pyc *.pyo
	rm -f tstorm/*.pyc tstorm/*.pyo
	rm -f tstorm/utils/*.pyc tstorm/utils/*.pyo
	rm -f tstorm/test/*.pyc tstorm/test/*.pyo
	rm -f *.tar.gz MANIFEST

srctar:
	python setup.py sdist -d .
	@echo "The src tar is in ${PACKAGE}-${SPECVERSION}.tar.gz"

bintar:
	python setup.py bdist -d .
	@echo "The bin tar is in ${PACKAGE}-${SPECVERSION}.tar.gz"

rpmbuild: srctar
	rpmbuild --nodeps -ta ${PACKAGE}-${SPECVERSION}.tar.gz


	
	

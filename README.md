The StoRM Testsuite
===============================

T-StoRM Testsuite provides an easy way to test your StoRM installation.
It is separated into two different modules one in charge of testing the service
from its interfaces, one performing sanity checks directly on StoRM host

Supported platforms
Scientific Linux 5 on x86_64 architecture
Scientific Linux 6 on x86_64 architecture

### Building
Required packages:

* epel
* git
* automake
* autoconf
* libtool
* python
* rpm-build

Build command:
```bash
./bootstrap
./configure --prefix=/usr --bindir=/usr/bin --sysconfdir=/etc --datadir=/usr/share
make rpm
```

# Contact info

If you have problems, questions, ideas or suggestions, please contact us at
the following URLs

* GGUS (official support channel): http://www.ggus.eu

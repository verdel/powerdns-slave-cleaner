==========================================================================
powerdns-slave-cleaner - Script for removing slave zones
==========================================================================


What is this?
*************
``powerdns-slave-cleaner`` provides an executable called ``powerdns-slave-cleaner``


Installation
************
*on most UNIX-like systems, you'll probably need to run the following*
``install`` *commands as root or by using sudo*

**from source**

::

  pip install git+http://github.com/verdel/powerdns-slave-cleaner

**or**

::

  git clone git://github.com/verdel/powerdns-slave-cleaner.git
  cd powerdns-slave-cleaner
  python setup.py install

as a result, the ``powerdns-slave-cleaner`` executable will be installed into a system ``bin``
directory

Usage
-----
::

    powerdns-slave-cleaner --help
    usage: powerdns-slave-cleaner [-h] -a HOST [-p PORT] -k API_KEY [--use-ssl]
                                     [--dry-run]

    Script for removing slave zones

    optional arguments:
      -h, --help            show this help message and exit
      -a HOST, --host HOST  powerdns slave server api address
      -p PORT, --port PORT  powerdns slave server api port (defaults to 8081)
      -k API_KEY, --api-key API_KEY
                            powerdns slave server api key
      --use-ssl             use https instead http
      --dry-run             read-only mode. just show changes

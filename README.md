# powerdns-slave-cleaner - Script for removing slave zones

## What is this?

This script get local domain zone on slave PowerDNS server by API request.

For each received domain zone, the script receives the master server addresses (if you do not specify a value for the `--master-host` option).

If you specify a value for the `--master-host` option, the specified address will be used to access the zone master API.

After that, a request is made through the API to each master server.

If the master server does not have a zone record corresponding to the local record,
then the local zone is deleted.

`powerdns-slave-cleaner` provides an executable called `powerdns-slave-cleaner`

## Installation

_on most UNIX-like systems, you'll probably need to run the following_
`install` _commands as root or by using sudo_

**from source**

```shell
pip install git+http://github.com/verdel/powerdns-slave-cleaner
```

**or**

```shell
git clone git://github.com/verdel/powerdns-slave-cleaner.git
cd powerdns-slave-cleaner
python setup.py install
```

as a result, the `powerdns-slave-cleaner` executable will be installed into a system `bin`
directory

## Usage

```shell
powerdns-slave-cleaner [-h] --host HOST [--port PORT] --api-key API_KEY [--master-host MASTER_HOST] [--master-port MASTER_PORT] [--master-api-key MASTER_API_KEY]
                       [--use-ssl] [--dry-run]

Script for removing slave zones

optional arguments:
  -h, --help            show this help message and exit
  --host HOST           powerdns slave server api address
  --port PORT           powerdns slave server api port (defaults to 8081)
  --api-key API_KEY     powerdns slave server api key
  --master-host MASTER_HOST
                        powerdns master server api address
  --master-port MASTER_PORT
                        powerdns master server api port (defaults to 8081)
  --master-api-key MASTER_API_KEY
                        powerdns master server api key (defaults to slave server api key
  --use-ssl             use https instead http
  --dry-run             read-only mode. just show changes
```

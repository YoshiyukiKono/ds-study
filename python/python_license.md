# Python License

https://ja.stackoverflow.com/questions/48650/python%E3%83%91%E3%83%83%E3%82%B1%E3%83%BC%E3%82%B8%E3%81%AE%E3%83%A9%E3%82%A4%E3%82%BB%E3%83%B3%E3%82%B9%E3%82%92%E7%A2%BA%E8%AA%8D%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95

## pip-licenses
### Install
```
pip install pip-licenses
```

```
$ pip-license > licenses.txt
```

https://pypi.org/project/pip-licenses/#option-from-classifier

```
$ pip-licenses --from=classifier --with-system | grep entrypoints
 entrypoints         0.3         MIT License
```

```
pip-licenses --from=mixed --with-system --with-description --order=license --format=csv > license_<project>.csv
```

### Dependency (Required-by)
```
cdsw@9qd8w0glnboeencs:~$ pip3 show sasl
Name: sasl
Version: 0.2.1
Summary: Cyrus-SASL bindings for Python
Home-page: http://github.com/toddlipcon/python-sasl
Author: None
Author-email: None
License: UNKNOWN
Location: /home/cdsw/.local/lib/python3.6/site-packages
Requires: six
Required-by: thrift-sasl
cdsw@9qd8w0glnboeencs:~$ pip3 show thrift-sasl
Name: thrift-sasl
Version: 0.3.0
Summary: Thrift SASL Python module that implements SASL transports for Thrift (`TSa
slClientTransport`).
Home-page: https://github.com/cloudera/thrift_sasl
Author: Uri Laserson
Author-email: laserson@cloudera.com
License: Apache License, Version 2.0
Location: /home/cdsw/.local/lib/python3.6/site-packages
Requires: thrift, sasl
Required-by: 
cdsw@9qd8w0glnboeencs:~$ 
```

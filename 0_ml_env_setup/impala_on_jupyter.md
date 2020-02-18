# Impala on Jupyter

## Jupyter Notebook

https://github.com/YoshiyukiKono/Miscellaneous

https://github.com/LucaCanali/Miscellaneous

## Impala Shell

https://docs.cloudera.com/documentation/enterprise/6/6.3/topics/impala_impala_shell.html


## csv

https://note.nkmk.me/python-csv-reader-writer/

## SQL Magic

```
export PYTHONPATH=/home/cdsw/lib/python/
cdsw@jqzx07xhdu6pt60k:~/ipython-sql$ python setup.py install --home=~
```

```
cdsw@5ub14uojdbogvgyf:~/ipython-sql$ python setup.py install --home=~
running install
running bdist_egg
running egg_info
writing requirements to src/ipython_sql.egg-info/requires.txt
writing src/ipython_sql.egg-info/PKG-INFO
writing top-level names to src/ipython_sql.egg-info/top_level.txt
writing dependency_links to src/ipython_sql.egg-info/dependency_links.txt
reading manifest file 'src/ipython_sql.egg-info/SOURCES.txt'
reading manifest template 'MANIFEST.in'
writing manifest file 'src/ipython_sql.egg-info/SOURCES.txt'
installing library code to build/bdist.linux-x86_64/egg
running install_lib
running build_py
creating build/bdist.linux-x86_64/egg
creating build/bdist.linux-x86_64/egg/sql
copying build/lib/sql/parse.py -> build/bdist.linux-x86_64/egg/sql
copying build/lib/sql/connection.py -> build/bdist.linux-x86_64/egg/sql
copying build/lib/sql/column_guesser.py -> build/bdist.linux-x86_64/egg/sql
copying build/lib/sql/run.py -> build/bdist.linux-x86_64/egg/sql
copying build/lib/sql/magic.py -> build/bdist.linux-x86_64/egg/sql
copying build/lib/sql/__init__.py -> build/bdist.linux-x86_64/egg/sql
byte-compiling build/bdist.linux-x86_64/egg/sql/parse.py to parse.pyc
byte-compiling build/bdist.linux-x86_64/egg/sql/connection.py to connection.pyc
byte-compiling build/bdist.linux-x86_64/egg/sql/column_guesser.py to column_guesser.
pyc
byte-compiling build/bdist.linux-x86_64/egg/sql/run.py to run.pyc
byte-compiling build/bdist.linux-x86_64/egg/sql/magic.py to magic.pyc
byte-compiling build/bdist.linux-x86_64/egg/sql/__init__.py to __init__.pyc
creating build/bdist.linux-x86_64/egg/EGG-INFO
copying src/ipython_sql.egg-info/PKG-INFO -> build/bdist.linux-x86_64/egg/EGG-INFO
copying src/ipython_sql.egg-info/SOURCES.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
copying src/ipython_sql.egg-info/dependency_links.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
copying src/ipython_sql.egg-info/not-zip-safe -> build/bdist.linux-x86_64/egg/EGG-INFO
copying src/ipython_sql.egg-info/requires.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
copying src/ipython_sql.egg-info/top_level.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
creating 'dist/ipython_sql-0.3.7.1-py2.7.egg' and adding 'build/bdist.linux-x86_64/egg' to it
removing 'build/bdist.linux-x86_64/egg' (and everything under it)
Processing ipython_sql-0.3.7.1-py2.7.egg
removing '/home/cdsw/lib/python/ipython_sql-0.3.7.1-py2.7.egg' (and everything under it)
creating /home/cdsw/lib/python/ipython_sql-0.3.7.1-py2.7.egg
Extracting ipython_sql-0.3.7.1-py2.7.egg to /home/cdsw/lib/python
ipython-sql 0.3.7.1 is already the active version in easy-install.pth

Installed /home/cdsw/lib/python/ipython_sql-0.3.7.1-py2.7.egg
Processing dependencies for ipython-sql==0.3.7.1
Searching for six==1.12.0
Best match: six 1.12.0
Adding six 1.12.0 to easy-install.pth file

Using /usr/local/lib/python2.7/site-packages
Searching for sqlparse==0.3.0
Best match: sqlparse 0.3.0
Processing sqlparse-0.3.0-py2.7.egg
sqlparse 0.3.0 is already the active version in easy-install.pth
Installing sqlformat script to /home/cdsw/bin

Using /home/cdsw/lib/python/sqlparse-0.3.0-py2.7.egg
Searching for SQLAlchemy==1.3.13
Best match: SQLAlchemy 1.3.13
Processing SQLAlchemy-1.3.13-py2.7-linux-x86_64.egg
SQLAlchemy 1.3.13 is already the active version in easy-install.pth

Using /home/cdsw/lib/python/SQLAlchemy-1.3.13-py2.7-linux-x86_64.egg
Searching for ipython==5.1.0
Best match: ipython 5.1.0
Adding ipython 5.1.0 to easy-install.pth file
Installing ipython script to /home/cdsw/bin
Installing iptest2 script to /home/cdsw/bin
Installing iptest script to /home/cdsw/bin
Installing ipython2 script to /home/cdsw/bin

Using /usr/local/lib/python2.7/site-packages
Searching for prettytable==0.7.2
Best match: prettytable 0.7.2
Processing prettytable-0.7.2-py2.7.egg
prettytable 0.7.2 is already the active version in easy-install.pth

Using /home/cdsw/lib/python/prettytable-0.7.2-py2.7.egg
Searching for pickleshare==0.7.5
Best match: pickleshare 0.7.5
Adding pickleshare 0.7.5 to easy-install.pth file

Using /usr/local/lib/python2.7/site-packages
Searching for simplegeneric==0.8.1
Best match: simplegeneric 0.8.1
Adding simplegeneric 0.8.1 to easy-install.pth file

Using /usr/local/lib/python2.7/site-packages
Searching for traitlets==4.3.2
Best match: traitlets 4.3.2
Adding traitlets 4.3.2 to easy-install.pth file

Using /usr/local/lib/python2.7/site-packages
Searching for Pygments==2.4.2
Best match: Pygments 2.4.2
Adding Pygments 2.4.2 to easy-install.pth file
Installing pygmentize script to /home/cdsw/bin

Using /usr/local/lib/python2.7/site-packages
Searching for prompt-toolkit==1.0.16
Best match: prompt-toolkit 1.0.16
Adding prompt-toolkit 1.0.16 to easy-install.pth file

Using /usr/local/lib/python2.7/site-packages
Searching for pexpect==4.7.0
Best match: pexpect 4.7.0
Adding pexpect 4.7.0 to easy-install.pth file

Using /usr/local/lib/python2.7/site-packages
Searching for pathlib2==2.3.3
Best match: pathlib2 2.3.3
Adding pathlib2 2.3.3 to easy-install.pth file

Using /usr/local/lib/python2.7/site-packages
Searching for backports.shutil-get-terminal-size==1.0.0
Best match: backports.shutil-get-terminal-size 1.0.0
Adding backports.shutil-get-terminal-size 1.0.0 to easy-install.pth file

Using /usr/local/lib/python2.7/site-packages
Searching for setuptools==41.0.1
Best match: setuptools 41.0.1
Adding setuptools 41.0.1 to easy-install.pth file
Installing easy_install script to /home/cdsw/bin
Installing easy_install-3.6 script to /home/cdsw/bin

Using /usr/local/lib/python2.7/site-packages
Searching for decorator==4.4.0
Best match: decorator 4.4.0
Adding decorator 4.4.0 to easy-install.pth file

Using /usr/local/lib/python2.7/site-packages
Searching for enum34==1.1.6
Best match: enum34 1.1.6
Adding enum34 1.1.6 to easy-install.pth file

Using /usr/local/lib/python2.7/site-packages
Searching for ipython-genutils==0.2.0
Best match: ipython-genutils 0.2.0
Adding ipython-genutils 0.2.0 to easy-install.pth file

Using /usr/local/lib/python2.7/site-packages
Searching for wcwidth==0.1.7
Best match: wcwidth 0.1.7
Adding wcwidth 0.1.7 to easy-install.pth file

Using /usr/local/lib/python2.7/site-packages
Searching for ptyprocess==0.6.0
Best match: ptyprocess 0.6.0
Adding ptyprocess 0.6.0 to easy-install.pth file

Using /usr/local/lib/python2.7/site-packages
Searching for scandir==1.10.0
Best match: scandir 1.10.0
Adding scandir 1.10.0 to easy-install.pth file

Using /usr/local/lib/python2.7/site-packages
Finished processing dependencies for ipython-sql==0.3.7.1
cdsw@5ub14uojdbogvgyf:~/ipython-sql$ pip3 list | grep ipython
ipython                            5.1.0      
ipython-genutils                   0.2.0      
ipython-sql                        0.3.7.1 
```

```
cdsw@5ub14uojdbogvgyf:~/ipython-sql$ pip3 list | grep ipython
ipython                            5.1.0      
ipython-genutils                   0.2.0      
ipython-sql                        0.3.7.1  
```

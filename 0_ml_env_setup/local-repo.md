## ローカルpypiリポジトリを作る

https://qiita.com/irotoris/items/13bce94bf9cc9ab36146

## pip installをオフライン環境で行う方法

https://qiita.com/analytics-hiro/items/2565adbb2c900e6738cd

https://pip.pypa.io/en/stable/reference/pip_download/#

## How do I create a local update server for Anaconda Python?

https://superuser.com/questions/979800/how-do-i-create-a-local-update-server-for-anaconda-python

Create a HTTP server and copy all the content from http://repo.continuum.io/pkgs/. Point to this new server with a .condarc file.

Choose a web server, and put the files referred to in the public repository (above) in there, with identical directory structure (but you don't need the /pkgs/free/ part). Use the respository file (eg. http://repo.continuum.io/pkgs/free/linux-64/repodata.json) to discover all the files, GET them and put onto your internal webserver.

Then, create a .condarc file with this template, supplying your internal web server like:

channels:
  - http://your.web.server/
This tells conda to get packages from your local repo, rather than the public Continuum one.

Once you've done this, running the command conda install anaconda will pull down the latest release of the Anaconda platform, from your internal repository. I have done the above, and can verify it works seamlessly. One word of caution: make sure you mirror the entire repository - don't try to optimise the packages that you include!


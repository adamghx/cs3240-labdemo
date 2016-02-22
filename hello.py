Adams-MacBook-Pro:~ AdamGuo$ pip install --upgrade pip
Requirement already up-to-date: pip in /Library/Python/2.7/site-packages/pip-8.0.2-py2.7.egg
Adams-MacBook-Pro:~ AdamGuo$ pip install --user psycopg2
Collecting psycopg2
  Using cached psycopg2-2.6.1.tar.gz
    Complete output from command python setup.py egg_info:
    running egg_info
    creating pip-egg-info/psycopg2.egg-info
    writing pip-egg-info/psycopg2.egg-info/PKG-INFO
    writing top-level names to pip-egg-info/psycopg2.egg-info/top_level.txt
    writing dependency_links to pip-egg-info/psycopg2.egg-info/dependency_links.txt
    writing manifest file 'pip-egg-info/psycopg2.egg-info/SOURCES.txt'
    warning: manifest_maker: standard file '-c' not found
    
    Error: pg_config executable not found.
    
    Please add the directory containing pg_config to the PATH
    or specify the full executable path with the option:
    
        python setup.py build_ext --pg-config /path/to/pg_config build ...
    
    or with the pg_config option in 'setup.cfg'.
    
    ----------------------------------------
Command "python setup.py egg_info" failed with error code 1 in /private/var/folders/h7/k8m3jn5n555_ljlm2nvfjd840000gn/T/pip-build-PcjEls/psycopg2
Adams-MacBook-Pro:~ AdamGuo$ sudo apt-get install libpq-dev python-devpip install --user psycopg2pip install --user psycopg2pip install --user psycopg2
Password:
sudo: apt-get: command not found
Adams-MacBook-Pro:~ AdamGuo$ sudo pip install --user psycopg2
The directory '/Users/AdamGuo/Library/Caches/pip/http' or its parent directory is not owned by the current user and the cache has been disabled. Please check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
The directory '/Users/AdamGuo/Library/Caches/pip' or its parent directory is not owned by the current user and caching wheels has been disabled. check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
Collecting psycopg2
  Downloading psycopg2-2.6.1.tar.gz (371kB)
    100% |████████████████████████████████| 372kB 609kB/s 
    Complete output from command python setup.py egg_info:
    running egg_info
    creating pip-egg-info/psycopg2.egg-info
    writing pip-egg-info/psycopg2.egg-info/PKG-INFO
    writing top-level names to pip-egg-info/psycopg2.egg-info/top_level.txt
    writing dependency_links to pip-egg-info/psycopg2.egg-info/dependency_links.txt
    writing manifest file 'pip-egg-info/psycopg2.egg-info/SOURCES.txt'
    warning: manifest_maker: standard file '-c' not found
    
    Error: pg_config executable not found.
    
    Please add the directory containing pg_config to the PATH
    or specify the full executable path with the option:
    
        python setup.py build_ext --pg-config /path/to/pg_config build ...
    
    or with the pg_config option in 'setup.cfg'.
    
    ----------------------------------------
Command "python setup.py egg_info" failed with error code 1 in /private/tmp/pip-build-9rYf5r/psycopg2
Adams-MacBook-Pro:~ AdamGuo$ sudo apt-get install libpq-dev python-dev
sudo: apt-get: command not found
Adams-MacBook-Pro:~ AdamGuo$ brew install postgresql
==> Installing dependencies for postgresql: openssl, readline
==> Installing postgresql dependency: openssl
==> Downloading https://homebrew.bintray.com/bottles/openssl-1.0.2d_1.yosemite.b
######################################################################## 100.0%
==> Pouring openssl-1.0.2d_1.yosemite.bottle.tar.gz
==> Caveats
A CA file has been bootstrapped using certificates from the system
keychain. To add additional certificates, place .pem files in
  /usr/local/etc/openssl/certs

and run
  /usr/local/opt/openssl/bin/c_rehash

This formula is keg-only, which means it was not symlinked into /usr/local.

Apple has deprecated use of OpenSSL in favor of its own TLS and crypto libraries

Generally there are no consequences of this for you. If you build your
own software and it requires this formula, you'll need to add to your
build variables:

    LDFLAGS:  -L/usr/local/opt/openssl/lib
    CPPFLAGS: -I/usr/local/opt/openssl/include

==> Summary
🍺  /usr/local/Cellar/openssl/1.0.2d_1: 464 files, 18M
==> Installing postgresql dependency: readline
==> Downloading https://homebrew.bintray.com/bottles/readline-6.3.8.yosemite.bot
######################################################################## 100.0%
==> Pouring readline-6.3.8.yosemite.bottle.tar.
:wq:

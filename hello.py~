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
==> Pouring readline-6.3.8.yosemite.bottle.tar.gz
==> Caveats
This formula is keg-only, which means it was not symlinked into /usr/local.

OS X provides the BSD libedit library, which shadows libreadline.
In order to prevent conflicts when programs look for libreadline we are
defaulting this GNU Readline installation to keg-only.


Generally there are no consequences of this for you. If you build your
own software and it requires this formula, you'll need to add to your
build variables:

    LDFLAGS:  -L/usr/local/opt/readline/lib
    CPPFLAGS: -I/usr/local/opt/readline/include

==> Summary
🍺  /usr/local/Cellar/readline/6.3.8: 40 files, 2.1M
==> Installing postgresql
==> Downloading https://homebrew.bintray.com/bottles/postgresql-9.4.5_2.yosemite
######################################################################## 100.0%
==> Pouring postgresql-9.4.5_2.yosemite.bottle.tar.gz
Error: The `brew link` step did not complete successfully
The formula built, but is not symlinked into /usr/local
Could not symlink include/ecpg_config.h
/usr/local/include is not writable.

You can try again using:
  brew link postgresql
==> /usr/local/Cellar/postgresql/9.4.5_2/bin/initdb /usr/local/var/postgres
Last 15 lines from /Users/AdamGuo/Library/Logs/Homebrew/postgresql/01.initdb:
2016-02-21 22:47:20 -0500

/usr/local/Cellar/postgresql/9.4.5_2/bin/initdb
/usr/local/var/postgres

The files belonging to this database system will be owned by user "AdamGuo".
This user must also own the server process.

initdb: file "/usr/local/share/postgresql/postgres.bki" does not exist
This might mean you have a corrupted installation or identified
the wrong directory with the invocation option -L.
Warning: The post-install step did not complete successfully
You can try again using `brew postinstall postgresql`
==> Caveats
If builds of PostgreSQL 9 are failing and you have version 8.x installed,
you may need to remove the previous version first. See:
  https://github.com/Homebrew/homebrew/issues/2510

To migrate existing data from a previous major version (pre-9.4) of PostgreSQL, see:
  https://www.postgresql.org/docs/9.4/static/upgrading.html

To have launchd start postgresql at login:
  ln -sfv /usr/local/opt/postgresql/*.plist ~/Library/LaunchAgents
Then to load postgresql now:
  launchctl load ~/Library/LaunchAgents/homebrew.mxcl.postgresql.plist
Or, if you don't want/need launchctl, you can just run:
  postgres -D /usr/local/var/postgres
==> Summary
🍺  /usr/local/Cellar/postgresql/9.4.5_2: 3021 files, 40M
Adams-MacBook-Pro:~ AdamGuo$ $ sudo mv /usr/lib/libpq.5.dylib /usr/lib/libpq.5.dylib.old 
-bash: $: command not found
Adams-MacBook-Pro:~ AdamGuo$ sudo mv /usr/lib/libpq.5.dylib /usr/lib/libpq.5.dylib.old 
Password:
Adams-MacBook-Pro:~ AdamGuo$ sudo ln -s /Library/PostgreSQL/9.4/lib/libpq.5.dylib /usr/lib
Adams-MacBook-Pro:~ AdamGuo$ export PATH=/Library/PostgreSQL/9.4/bin/:"$PATH”
> sudo pip install psycopg2
> 
> 
Adams-MacBook-Pro:~ AdamGuo$ psql -U postgres course1
-bash: psql: command not found
Adams-MacBook-Pro:~ AdamGuo$ sudo pip install PostgreSQL
The directory '/Users/AdamGuo/Library/Caches/pip/http' or its parent directory is not owned by the current user and the cache has been disabled. Please check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
The directory '/Users/AdamGuo/Library/Caches/pip' or its parent directory is not owned by the current user and caching wheels has been disabled. check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
Collecting PostgreSQL
  Could not find a version that satisfies the requirement PostgreSQL (from versions: )
No matching distribution found for PostgreSQL
Adams-MacBook-Pro:~ AdamGuo$ git
usage: git [--version] [--help] [-C <path>] [-c name=value]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           <command> [<args>]

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone      Clone a repository into a new directory
   init       Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add        Add file contents to the index
   mv         Move or rename a file, a directory, or a symlink
   reset      Reset current HEAD to the specified state
   rm         Remove files from the working tree and from the index

examine the history and state (see also: git help revisions)
   bisect     Find by binary search the change that introduced a bug
   grep       Print lines matching a pattern
   log        Show commit logs
   show       Show various types of objects
   status     Show the working tree status

grow, mark and tweak your common history
   branch     List, create, or delete branches
   checkout   Switch branches or restore working tree files
   commit     Record changes to the repository
   diff       Show changes between commits, commit and working tree, etc
   merge      Join two or more development histories together
   rebase     Forward-port local commits to the updated upstream head
   tag        Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch      Download objects and refs from another repository
   pull       Fetch from and integrate with another repository or a local branch
   push       Update remote refs along with associated objects

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
Adams-MacBook-Pro:~ AdamGuo$ git config --global user.name "Adam Guo"
Adams-MacBook-Pro:~ AdamGuo$ git config --global user.email "adamguo14@gmail.com"
Adams-MacBook-Pro:~ AdamGuo$ git config --global core.editor emacs
Adams-MacBook-Pro:~ AdamGuo$ cd Desktop
Adams-MacBook-Pro:Desktop AdamGuo$ mkdir CS3240
Adams-MacBook-Pro:Desktop AdamGuo$ cd CS3240
Adams-MacBook-Pro:CS3240 AdamGuo$ git clone https://github.com/adamghx/cs3240-labdemo.git
Cloning into 'cs3240-labdemo'...
remote: Counting objects: 5, done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 5 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (5/5), done.
Checking connectivity... done.
Adams-MacBook-Pro:CS3240 AdamGuo$ cd cs3240-labdemo
Adams-MacBook-Pro:cs3240-labdemo AdamGuo$ ls
LICENSE		README.md
Adams-MacBook-Pro:cs3240-labdemo AdamGuo$ emacs -nw

;; This buffer is for notes you don't want to save, and for Lisp evaluation.    
;; If you want to create a file, visit that file with C-x C-f,                  
;; then enter the text in that file's own buffer.                               
hello world


















-uuu:**-F1  *scratch*      All L4     (Lisp Interaction)------------------------


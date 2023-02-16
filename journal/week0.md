# Week 0 — Billing and Architecture

## REQUIRED WORK

### Pre-requisites for this week

Getting all the information and th base to be crated from the reference videos from ExamPro Playlist on YouTube, which includes:

## The Homework Tasks for Week0

AWS CLI is most ofter and widely used for working with AWS commands using a command prompt. We will start with installing the AWS CLI

### AWS CLI- Install

Ref link: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

Using `Brew` to install

Command

```
brew install awscli
```

Output

```
❯ which aws
aws not found
❯ brew install awscli
Running `brew update --auto-update`...
==> Downloading https://formulae.brew.sh/api/formula.json
######################################################################## 100.0%
==> Downloading https://formulae.brew.sh/api/cask.json
######################################################################## 100.0%
==> Fetching dependencies for awscli: openssl@1.1, readline, sqlite, xz, python@3.11, docutils and six
==> Fetching openssl@1.1
==> Downloading https://ghcr.io/v2/homebrew/core/openssl/1.1/manifests/1.1.1t
######################################################################## 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/openssl/1.1/blobs/sha256:97676d1a616421e472c46fc7930fa4a9ced51
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sha256:97676d1a616421e472c46fc793
######################################################################## 100.0%
==> Fetching readline
==> Downloading https://ghcr.io/v2/homebrew/core/readline/manifests/8.2.1
######################################################################## 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/readline/blobs/sha256:abe9d3f3eec3ba2339860faa6a978b9909194c65
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sha256:abe9d3f3eec3ba2339860faa6a
######################################################################## 100.0%
==> Fetching sqlite
==> Downloading https://ghcr.io/v2/homebrew/core/sqlite/manifests/3.40.1
######################################################################## 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/sqlite/blobs/sha256:d3092d3c942b50278f82451449d2adc3d1dc1bd724
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sha256:d3092d3c942b50278f82451449
######################################################################## 100.0%
==> Fetching xz
==> Downloading https://ghcr.io/v2/homebrew/core/xz/manifests/5.4.1
######################################################################## 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/xz/blobs/sha256:619b87932c5393af72b259b17ee8270275e0e5dc8893bd
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sha256:619b87932c5393af72b259b17e
######################################################################## 100.0%
==> Fetching python@3.11
==> Downloading https://ghcr.io/v2/homebrew/core/python/3.11/manifests/3.11.2-1
######################################################################## 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/python/3.11/blobs/sha256:7695af6d6b1bfc7a902ff85b0472b5c94cbc4
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sha256:7695af6d6b1bfc7a902ff85b04
######################################################################## 100.0%
==> Fetching docutils
==> Downloading https://ghcr.io/v2/homebrew/core/docutils/manifests/0.19_1
######################################################################## 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/docutils/blobs/sha256:263354453fe6a41c646d4d9b637f71fa5b09ee1d
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sha256:263354453fe6a41c646d4d9b63
######################################################################## 100.0%
==> Fetching six
==> Downloading https://ghcr.io/v2/homebrew/core/six/manifests/1.16.0_3
######################################################################## 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/six/blobs/sha256:0dee50367c6facbfc8f65e8a82bcd3e08d43da262b1ad
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sha256:0dee50367c6facbfc8f65e8a82
######################################################################## 100.0%
==> Fetching awscli
==> Downloading https://ghcr.io/v2/homebrew/core/awscli/manifests/2.10.0
######################################################################## 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/awscli/blobs/sha256:356d02624a9452047e24e68644ca985b4591dd95a4
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sha256:356d02624a9452047e24e68644
######################################################################## 100.0%
==> Installing dependencies for awscli: openssl@1.1, readline, sqlite, xz, python@3.11, docutils and six
==> Installing awscli dependency: openssl@1.1
==> Pouring openssl@1.1--1.1.1t.ventura.bottle.tar.gz
🍺  /usr/local/Cellar/openssl@1.1/1.1.1t: 8,101 files, 18.5MB
==> Installing awscli dependency: readline
==> Pouring readline--8.2.1.ventura.bottle.tar.gz
🍺  /usr/local/Cellar/readline/8.2.1: 50 files, 1.7MB
==> Installing awscli dependency: sqlite
==> Pouring sqlite--3.40.1.ventura.bottle.tar.gz
🍺  /usr/local/Cellar/sqlite/3.40.1: 11 files, 4.4MB
==> Installing awscli dependency: xz
==> Pouring xz--5.4.1.ventura.bottle.tar.gz
🍺  /usr/local/Cellar/xz/5.4.1: 95 files, 1.6MB
==> Installing awscli dependency: python@3.11
==> Pouring python@3.11--3.11.2.ventura.bottle.1.tar.gz
Error: The `brew link` step did not complete successfully
The formula built, but is not symlinked into /usr/local
Could not symlink bin/2to3
Target /usr/local/bin/2to3
is a symlink belonging to python@3.9. You can unlink it:
  brew unlink python@3.9

To force the link and overwrite all conflicting files:
  brew link --overwrite python@3.11

To list all files that would be deleted:
  brew link --overwrite --dry-run python@3.11

Possible conflicting files are:
/usr/local/bin/2to3 -> /usr/local/Cellar/python@3.9/3.9.13_1/bin/2to3
/usr/local/bin/idle3 -> /usr/local/Cellar/python@3.9/3.9.13_1/bin/idle3
/usr/local/bin/pydoc3 -> /usr/local/Cellar/python@3.9/3.9.13_1/bin/pydoc3
/usr/local/bin/python3 -> /usr/local/Cellar/python@3.9/3.9.13_1/bin/python3
/usr/local/bin/python3-config -> /usr/local/Cellar/python@3.9/3.9.13_1/bin/python3-config
/usr/local/share/man/man1/python3.1 -> /usr/local/Cellar/python@3.9/3.9.13_1/share/man/man1/python3.1
/usr/local/lib/pkgconfig/python3-embed.pc -> /usr/local/Cellar/python@3.9/3.9.13_1/lib/pkgconfig/python3-embed.pc
/usr/local/lib/pkgconfig/python3.pc -> /usr/local/Cellar/python@3.9/3.9.13_1/lib/pkgconfig/python3.pc
/usr/local/Frameworks/Python.framework/Headers -> /usr/local/Cellar/python@3.9/3.9.13_1/Frameworks/Python.framework/Headers
/usr/local/Frameworks/Python.framework/Python -> /usr/local/Cellar/python@3.9/3.9.13_1/Frameworks/Python.framework/Python
/usr/local/Frameworks/Python.framework/Resources -> /usr/local/Cellar/python@3.9/3.9.13_1/Frameworks/Python.framework/Resources
/usr/local/Frameworks/Python.framework/Versions/Current -> /usr/local/Cellar/python@3.9/3.9.13_1/Frameworks/Python.framework/Versions/Current
==> /usr/local/Cellar/python@3.11/3.11.2/bin/python3.11 -m ensurepip
==> /usr/local/Cellar/python@3.11/3.11.2/bin/python3.11 -m pip install -v --no-deps --no-index --upgrade --isol
==> Summary
🍺  /usr/local/Cellar/python@3.11/3.11.2: 3,176 files, 61.4MB
==> Installing awscli dependency: docutils
==> Pouring docutils--0.19_1.ventura.bottle.tar.gz
🍺  /usr/local/Cellar/docutils/0.19_1: 231 files, 2MB
==> Installing awscli dependency: six
==> Pouring six--1.16.0_3.all.bottle.tar.gz
🍺  /usr/local/Cellar/six/1.16.0_3: 20 files, 122.4KB
==> Installing awscli
==> Pouring awscli--2.10.0.ventura.bottle.tar.gz
==> Caveats
The "examples" directory has been installed to:
  /usr/local/share/awscli/examples

zsh completions and functions have been installed to:
  /usr/local/share/zsh/site-functions
==> Summary
🍺  /usr/local/Cellar/awscli/2.10.0: 13,172 files, 115.1MB
==> Running `brew cleanup awscli`...
Disable this behaviour by setting HOMEBREW_NO_INSTALL_CLEANUP.
Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
==> Upgrading 2 dependents of upgraded formulae:
Disable this behaviour by setting HOMEBREW_NO_INSTALLED_DEPENDENTS_CHECK.
Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
python@3.9 3.9.13_1 -> 3.9.16, python-tk@3.9 3.9.13 -> 3.9.16
==> Fetching python@3.9
==> Downloading https://ghcr.io/v2/homebrew/core/python/3.9/manifests/3.9.16
######################################################################## 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/python/3.9/blobs/sha256:06e42063af5803d934d891dbd15748ab156c54
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sha256:06e42063af5803d934d891dbd1
######################################################################## 100.0%
==> Fetching dependencies for python-tk@3.9: tcl-tk
==> Fetching tcl-tk
==> Downloading https://ghcr.io/v2/homebrew/core/tcl-tk/manifests/8.6.13
######################################################################## 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/tcl-tk/blobs/sha256:afd13198b0dbcc0eb4352614129f1cb06a614cea6d
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sha256:afd13198b0dbcc0eb435261412
######################################################################## 100.0%
==> Fetching python-tk@3.9
==> Downloading https://ghcr.io/v2/homebrew/core/python-tk/3.9/manifests/3.9.16
######################################################################## 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/python-tk/3.9/blobs/sha256:232df696df869d89550c0b3142b718f1743
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sha256:232df696df869d89550c0b3142
######################################################################## 100.0%
==> Upgrading python@3.9
  3.9.13_1 -> 3.9.16

==> Pouring python@3.9--3.9.16.ventura.bottle.tar.gz
==> /usr/local/Cellar/python@3.9/3.9.16/bin/python3.9 -m ensurepip
==> /usr/local/Cellar/python@3.9/3.9.16/bin/python3.9 -m pip install -v --no-deps --no-index --upgrade --isolat
==> Caveats
Python has been installed as
  /usr/local/bin/python3.9

Unversioned and major-versioned symlinks `python`, `python3`, `python-config`, `python3-config`, `pip`, `pip3`, etc. pointing to
`python3.9`, `python3.9-config`, `pip3.9` etc., respectively, have been installed into
  /usr/local/opt/python@3.9/libexec/bin

You can install Python packages with
  pip3.9 install <package>
They will install into the site-package directory
  /usr/local/lib/python3.9/site-packages

tkinter is no longer included with this formula, but it is available separately:
  brew install python-tk@3.9

If you do not need a specific version of Python, and always want Homebrew's `python3` in your PATH:
  brew install python3

See: https://docs.brew.sh/Homebrew-and-Python
==> Summary
🍺  /usr/local/Cellar/python@3.9/3.9.16: 3,066 files, 55.4MB
==> Running `brew cleanup python@3.9`...
Removing: /usr/local/Cellar/python@3.9/3.9.13_1... (3,130 files, 56.2MB)
==> Upgrading python-tk@3.9
  3.9.13 -> 3.9.16

==> Installing dependencies for python-tk@3.9: tcl-tk
==> Installing python-tk@3.9 dependency: tcl-tk
==> Pouring tcl-tk--8.6.13.ventura.bottle.tar.gz
🍺  /usr/local/Cellar/tcl-tk/8.6.13: 3,070 files, 52.8MB
==> Installing python-tk@3.9
==> Pouring python-tk@3.9--3.9.16.ventura.bottle.tar.gz
🍺  /usr/local/Cellar/python-tk@3.9/3.9.16: 5 files, 132.6KB
==> Running `brew cleanup python-tk@3.9`...
Removing: /usr/local/Cellar/python-tk@3.9/3.9.13... (5 files, 132.7KB)
==> Checking for dependents of upgraded formulae...
==> No broken dependents found!
==> Caveats
==> awscli
The "examples" directory has been installed to:
  /usr/local/share/awscli/examples

zsh completions and functions have been installed to:
  /usr/local/share/zsh/site-functions
==> python@3.9
Python has been installed as
  /usr/local/bin/python3.9

Unversioned and major-versioned symlinks `python`, `python3`, `python-config`, `python3-config`, `pip`, `pip3`, etc. pointing to
`python3.9`, `python3.9-config`, `pip3.9` etc., respectively, have been installed into
  /usr/local/opt/python@3.9/libexec/bin

You can install Python packages with
  pip3.9 install <package>
They will install into the site-package directory
  /usr/local/lib/python3.9/site-packages

tkinter is no longer included with this formula, but it is available separately:
  brew install python-tk@3.9

If you do not need a specific version of Python, and always want Homebrew's `python3` in your PATH:
  brew install python3

See: https://docs.brew.sh/Homebrew-and-Python
```

As instrcuted intalled `Python3` as well with command

```
 ❯ brew install python3
Warning: python@3.11 3.11.2 is already installed, it's just not linked.
To link this version, run:
  brew link python@3.11
❯ brew link python@3.11
Linking /usr/local/Cellar/python@3.11/3.11.2... 21 symlinks created.
```

![Proof here](/assets/AWS%20CLI%20Install%20and%20verify.png)

## HOMEWORK CHALLENGES

## ADDITIONAL HOMEWORK CHALLENGES

# TaskManager

[![Build Status](https://travis-ci.org/caiquepereira/TaskManager.svg?branch=master)](https://travis-ci.org/caiquepereira/TaskManager)
[![Coverage Status](https://coveralls.io/repos/github/caiquepereira/TaskManager/badge.svg?branch=master)](https://coveralls.io/github/caiquepereira/TaskManager?branch=master)

Task Manager project in Python using Django Framework.

# Author
Universidade de Brasília

Advanced Software Development (Desenvolvimento Avançado de Software)

Student: Caíque de Paula Pereira


# Installing twitter plugin

Install CMS
```bash
$ git clone https://github.com/cms-dev/cms.git
$ cd cms
$ sudo python setup.py build
$ sudo python setup.py install
```

Install tweepy
```bash
$ sudo pip install tweepy
```

Install plugin on taskbuster_project directory run
```bash
$ sudo python setup.py develop
$ sudo python setup.py install
```

# Running the development server

```bash
$ taskbuster/manage.py runserver
```

# Running the functional tests

```bash
$ taskbuster/manage.py test functional_tests
```

# Running the unittests

```bash
$ taskbuster/manage.py test taskbuster.test
```

# Checking coverage

```bash
$ coverage run --source='.' taskbuster/manage.py test
$ coverage report
```

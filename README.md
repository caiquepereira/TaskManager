# TaskManager

[![Build Status](https://travis-ci.org/caiquepereira/TaskManager.svg?branch=master)](https://travis-ci.org/caiquepereira/TaskManager)

Task Manager project in Python using Django Framework.

# Author
Universidade de Brasília

Advanced Software Development (Desenvolvimento Avançado de Software)

Student: Caíque de Paula Pereira

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
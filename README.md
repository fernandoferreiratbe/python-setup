# python-setup
This project was created in order to test Python packaging

### The central idea is to implement the principal (in my point of view) attributes of setup.py file and validate the build, dist and install process.

## Needs

* pip install virtualenv
* Create a folder for your project
* Access it and type: **virtualenv .venv**
* Activate your virtual environment: **source .venv/bin/activate**
* Acess the project directory

### To perform project building
```console
$ python setup.py sdist bdist_wheel
```

### To install in current activated virutal environment
```console
$ pip install . 
```

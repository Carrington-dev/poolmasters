# PoolMasters

### Introduction

This is PoolMasters, an online pool-maintainance company which is highly avalable. it provides all logos, fliers, images design etc needed to run a business. The client has paid for the website but it's in great shape. We are planning to intergrate  CI/CD in this platform on any cloud platform, emails with this platform so that it can be a fully functional business. This website contains email marketing in small portions which actual need s revision to cater for the new model updates

__To scale this website we will use autoscaling on AWS and an Elastic Load Balancer to distribute and channel traffic to the right instances__



### How to create environment

Install all packages on ubuntu. Requirements for ubuntu are in ubuntu_req.txt while requirements for the website are in requirements.txt

```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt update
sudo apt install python3-venv python3-dev libpq-dev postgresql postgresql-contrib nginx curl
```

To create an environment run

```python
python3 -m venv environment_name
```

### Creating the PostgreSQL Database and User 

#### Method 1

__This works if you don't want to scale your website automatically__

Now you can jump right in and create a database and database user for our Django application.

By default, Postgres uses an authentication scheme called “peer authentication” for local connections. Basically, this means that if the user’s operating system username matches a valid Postgres username, that user can login with no further authentication.

During the Postgres installation, an operating system user named postgres was created to correspond to the postgres PostgreSQL administrative user. You need to use this user to perform administrative tasks. You can use sudo and pass in the username with the -u option.

Log into an interactive Postgres session by typing:

```
sudo -u postgres psql
```

You will be given a PostgreSQL prompt where you can set up our requirements.

First, create a database for your project:

```postgresql
CREATE DATABASE myproject;
```

```postgresql
CREATE USER myprojectuser WITH PASSWORD 'password';
```

```postgresql
CREATE USER myprojectuser WITH PASSWORD 'password';
```

```postgresql
ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myprojectuser SET timezone TO 'UTC';
```

```postgresql
GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;
```

```postgresql
\q
```


#### Method 2 Using RDS Database Settings.

__This works if you want to scale__

Install pscopy2-binary

```python
pip3 install pscopy2-binary
```

set up permissions and roles on aws or use roles for the IAM user controlling the user

### How to install


```python

""" python3 -m venv environment_name """
source  environment_name/bin/activate
pip3 install -r requirements.txt
```


It is possible for Pillow to give you an error in ubuntu saying cairo is not installed same applies on windows as well. In windows install a library given on github.com while on ubuntu install the other libraries as well.

For scalablity avoid using an install as a database, proxy server and for storing media files as this won't work when trying to scale

__It is always a good idea to separate required packages based on specific modes e.g production modes and testing/development modes__

```python

django_proj/django_project/settings/dev.py
django_proj/django_project/settings/prod.py
```

### How to unistall a specific package

```python
 pip3 unistall -r package_name
```
### How to configure nginx

To run nginx on ubuntu you need to install it first
#### Installing nginx

```bash

sudo apt-get install nginx
```
#### Setup nginx

to setup nginx

```bash


```
content of the file

### How to configure gunicorn

```
sudo nano /etc/systemd/system/gunicorn.socket
```

Content of the file above
```
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
```

Now we will add the new file for Gunicorn

```
sudo nano /etc/systemd/system/gunicorn.service
```

Content of the file above
```
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target
```



### How to build a buildspec File
### How to build a AppSpec File
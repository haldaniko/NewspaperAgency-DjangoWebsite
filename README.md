# Newspaper Agency Project

Django project for managing newspapers and redactors in nespaper agency.

## Instalation

Python 3 must be already installed

```shell
git clone https://github.com/haldaniko/newspaper-agency-website.git
cd newspaper-agency-website
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata newspapers_db_data.json
python manage.py runserver
```

After loading data from fixture you can use following superuser (or create another one by yourself):
  - Login: `admin.user`
  - Password: `1qazcde3`


## Features

* Authentication functionality for Redactor/User
* Managing newspapers & topics directly from website interface
* Powerful admin panel for advanced managing

## Demo
![Website Interface](demo1.png)
![Website Interface](demo2.png)

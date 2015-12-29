# README #

```
virtualenv --no-site-packages kik
cd kik
. ./bin/activate
mkdir kik
cd kik
git init .
git remote add origin git@bitbucket.org:almacloud/kik.git
git pull origin master
pip install -r requirements.txt
cd src
./manage.py syncdb
./manage.py migrate
./manage.py runserver
```
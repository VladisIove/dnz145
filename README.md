
## 1 STEP
Download postgresql
If need change path to postgresql in docker-compose volumes postgres

## 2 STEP
Download docker-compose and docker

## 3 STEP
Create folder misc with file: db, django_conf and nginx_conf with need parameters

## 4 STEP
docker-compose up --build

## 5 STEP
Go into container "back" and do commands ( docker exec -it back sh ):
1. python manage.py makemigrations
2. python manage.py migrate
3. pythin manage.py collectstatic --noinput
4. python manage.py createsuperuser

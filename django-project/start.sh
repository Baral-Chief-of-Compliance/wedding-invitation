#!/bin/sh

set -o errexit

set -o pipefail

set -o nounset

echo "Создаем миграцию базы данных..."
python3 ./manage.py makemigrations

echo "Выполняем миграции базы данных..."
python3 ./manage.py migrate


#Проверяем, существует ли суперпользователь

if python3 ./manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); print(User.objects.filter(username='$DJANGO_SUPERUSER_USERNAME').exists())" | grep -q True; then

	echo "Суперпользователь $DJANGO_SUPERUSER_USERNAME уже существует."

else
	#Создаем суперпользователя
	echo "Создаем суперпользователя..."
	echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('$DJANGO_SUPERUSER_USERNAME', '$DJANGO_SUPERUSER_EMAIL', '$DJANGO_SUPERUSER_PASSWORD')" | python ./manage.py shell

	echo "Суперпользователь $DJANGO_SUPERUSER_USERNAME создан."

fi

python3 manage.py collectstatic --noinput

gunicorn -b 0.0.0.0:8000 wedding_invitation_project.wsgi:application

if [ $? -ne 0 ]; then
	echo "Django приложени не удалось запустить"
fi

echo "Django приложение запущено на http://localhost:8000/"
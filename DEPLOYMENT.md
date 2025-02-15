# Инструкция по развертыванию

## Предварительные требования

- Docker и Docker Compose
- Nginx
- Certbot
- Доменное имя, настроенное на ваш сервер

## Шаги по развертыванию

1. Клонируйте репозиторий:
```bash
git clone https://github.com/your-username/historystate.git
cd historystate
```

2. Создайте необходимые директории:
```bash
mkdir -p /var/www/historystate/media
mkdir -p /var/www/historystate/staticfiles
```

3. Скопируйте конфигурацию Nginx:
```bash
cp nginx/default.conf /etc/nginx/conf.d/
```

4. Получите SSL-сертификат:
```bash
certbot --nginx -d historystate.my-business-card.kz
```

5. Запустите приложение:
```bash
docker-compose up -d
```

6. Установите правильные права доступа:
```bash
chown -R www-data:www-data /var/www/historystate/media
chown -R www-data:www-data /var/www/historystate/staticfiles
chmod -R 755 /var/www/historystate/media
chmod -R 755 /var/www/historystate/staticfiles
```

## Переменные окружения

Создайте файл `.env` в корне проекта со следующими переменными:

```
DEBUG=0
POSTGRES_DB=historystate
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=postgres
DJANGO_SETTINGS_MODULE=historystate.settings
ALLOWED_HOSTS=historystate.my-business-card.kz,localhost,127.0.0.1
CSRF_TRUSTED_ORIGINS=https://historystate.my-business-card.kz
```

## Проверка работоспособности

1. Проверьте доступность сайта:
```bash
curl -I https://historystate.my-business-card.kz
```

2. Проверьте статические файлы:
```bash
curl -I https://historystate.my-business-card.kz/static/admin/css/base.css
```

3. Проверьте медиа-файлы:
```bash
curl -I https://historystate.my-business-card.kz/media/hero/example.jpg
```

## Обновление приложения

Для обновления приложения выполните:

```bash
git pull
docker-compose down
docker-compose up -d --build
python manage.py migrate
python manage.py collectstatic --noinput
``` 
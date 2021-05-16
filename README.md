# Django ecommerce api.

This is a ecommerce api built using [django-rest-framework](https://github.com/encode/django-rest-framework)

## Getting Started

Make shure you create a .env file inside [settings folder](https://github.com/julianarchila/ecommerce-django-api/tree/master/config/settings) with the following data:

```bash
DEBUG=True
SECRET_KEY=
```
Then just start the django project as usual.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

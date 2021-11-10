### How to start a project:

Clone and move to another repository:

```
git clone https://github.com/deadbit-dev/api_final_yatube.git
```

```
cd api_final_yatube
```

Create and activate a virtual environment:

```
python3 -m venv env
```

```
source env/bin/activate
```

Install dependencies from file requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Run migrations:

```
python3 manage.py migrate
```

Run the project:

```
python3 manage.py runserver
```
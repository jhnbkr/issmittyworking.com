# Is Smitty Working?
[https://issmittyworking.com](https://issmittyworking.com)

### Create Environment

Create Python virtual environment and install dependencies
```
python3 -m venv venv
source venv/bin/activate
make install
```

Copy `.env.template` to `.env` in the root and edit/remove necessary entries

### Run Application

Run Django development server
```
source venv/bin/activate
make run
```

Run Gunicorn web server
```
source venv/bin/activate
make web
```
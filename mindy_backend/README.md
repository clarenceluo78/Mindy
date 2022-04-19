## Installation Tutorial

### 1. install dependent modules
```
pip install -r requirements.txt
```

### 2. Database configuration
Open /Mindy/config/config.ini，modify content in [database] to:
```
engine = mysql
name = your database name
user = your database user
password = your password
host = your ip
port = your port
```

### 3. Initialize database

After installing the required third-party library and configuring the database information, we need to initialize the database.

Open the command line interface under the project path and run the following command to generate the database migration:

```
python manage.py makemigrations 
```

Run the following command to perform database migration:

```
python manage.py migrate
```

After execution, the database is initialized.

### 4. Create Super User

After initializing the database, you need to create an administrator account to manage the whole mrdoc. Open the command line terminal in the project path and run the following command:

```
python manage.py createsuperuser
```

Follow the prompts to enter the user name, email address and password.

### 5. Test Running

After completing the above steps, you can run and use mrdoc.

In the test environment, you can use the server provided by Django to run mrdoc. The command is:

```
python manage.py runserver
```
# Little-Lemon website

This is my second Django framework web development project.

Feel free to contribute to or copy this project:
You can clone it using the following command:
```git clone https://github.com/happychuks/little-lemon.git```

- change directory into the parent directory of the repository

- Switch to a virtual environment
  - This can be done by running the following command:
```bash
python3 -m venv env
source env/bin/activate
```
install all necessary dependencies from the requirements.txt file using the following command:
```pip3 install -r requirements.txt```

- Run the development server using the following command:
```bash
python3 manage.py runserver # To run the server
# Ctrl + C to stop the server
python3 manage.py makemigrations # To compile the migrations
python3 manage.py migrate  # To migrate the changes in Database
python3 manage.py shell # To run interactive shell
```

### To create admin profile using the following command:
```bash
python3 manage.py createsuperuser
# Enter necessary credentials
```

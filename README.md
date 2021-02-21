# Flaskini

Tiny rest api for introducing python and flask 

## How to start

1. **Set up environment**

- Using docker  
    Check [readme](deploy/README.md) for deploying a dev environment and migrating the database

- Manually  
    Install a mariaDB server with a database called flaskini and create tables following the scripts in `database/sql`
  
2. **Install requirements**

```pip3 install -r requirements.txt```
   
3. **Start the application**  

Configure `app.yaml` if needed and execute:

```python3 main.py```

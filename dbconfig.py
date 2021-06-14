dbconfig = {
    "dbname": 'LabDB', "host": 'localhost', "user": 'postgres', "password": '77829199'
}
config = " ".join([f"{key}={dbconfig[key]}" for key in dbconfig.keys()])

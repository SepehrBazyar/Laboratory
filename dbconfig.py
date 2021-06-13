dbconfig = {
    "dbname": 'LabDB', "host": 'localhost', "user": 'postgres', "password": '----'
}
config = " ".join([f"{key}={dbconfig[key]}" for key in dbconfig.keys()])

dbconfig = {
    "dbname": 'LabDB', "host": 'localhost', "user": 'postgres', "password": 'sepibzyr79'
}
config = " ".join([f"{key}={dbconfig[key]}" for key in dbconfig.keys()])

dbconfig = {
            "dbname": 'LabDB2', "host": 'localhost', "user": 'postgres', "password": '@@datb_new123!!'
        }
config = " ".join([f"{key}={dbconfig[key]}" for key in dbconfig.keys()])
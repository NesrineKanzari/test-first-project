import os


class database_config:
    DATABASE = os.getenv('DATABASE', 'mongodb')
    IPADDRESS = os.getenv('IPADDRESS', "localhost")
    PORT = os.getenv('PORT', '27017')
    # composition
    URL = f"{DATABASE}://{IPADDRESS}:{PORT}"
    # print(URL)

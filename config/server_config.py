import os


class ServerConfig:
    # TODO : get not set (env)
    IPADDRESS = os.getenv('IPADDRESS')
    PORT = os.getenv('PORT')



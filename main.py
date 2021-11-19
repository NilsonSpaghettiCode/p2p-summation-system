'''
Archivo main
'''
from app.service_main import start as run
from config.config import config as cfg

def main():
    run(cfg['ip_address'], cfg['port'])


if __name__ == '__main__':
    main()
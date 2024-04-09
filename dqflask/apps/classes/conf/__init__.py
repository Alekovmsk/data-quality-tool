import yaml
import paramiko
import json


class ConfYaml:
    # f = open("settings.conf", "r")
    # settings = {}
    # for cur in f:
    #     row = cur.strip().split('=')
    #     settings[row[0]] = row[1]

    # ssh = paramiko.SSHClient()
    # ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # ssh.connect(settings['CONFIG_HOST'], username=settings['CONFIG_USER'], password=settings['CONFIG_PASS'])
    # sftp = ssh.open_sftp()
    # config_file = sftp.open(settings['CONFIG_PATH'])
    # config = yaml.safe_load(config_file)
    # logging_file = sftp.open(settings['CONFIG_LOG_PATH'])
    # logging_conf = yaml.safe_load(logging_file)
    # logging_file = sftp.open(settings['CONFIG_LOG_PATH'])

    with open("config/config.yaml", "r") as conf:
        config = yaml.safe_load(conf)

    # config logging into file
    with open("config/logging.conf", "r") as conf:
        logging_conf = yaml.safe_load(conf)


class DqConfigDB(ConfYaml):
    def __init__(self, server_name):
        super().__init__()
        self.type = self.config['database'][server_name]['type']
        self.host = self.config['database'][server_name]['host']
        self.port = self.config['database'][server_name]['port']
        self.db = self.config['database'][server_name]['db']
        self.user = self.config['database'][server_name]['user']
        self.password = self.config['database'][server_name]['password']

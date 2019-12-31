import os
import json

DB_CONFIG = '/var/www/cvs_api/etc/db_config.json'

def parse_db_config():
    with open(DB_CONFIG, 'r') as fp:
        db_cfg = json.load(fp)
    return db_cfg

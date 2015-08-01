#!/usr/bin/env python
import os
import os.path
import sys
import ConfigParser as configparser


def get_config():
    config = configparser.ConfigParser()
    if os.path.exists('manage.cfg'):
        config.read('manage.cfg')
    return config


def get_settings_module(config):
    if 'test' in sys.argv and config.has_section('test'):
        return config.get('test', 'settings')
    elif config.has_section('default'):
        return config.get('default', 'settings')
    else:
        return 'deployment.settings'


if __name__ == "__main__":
    config = get_config()
    settings_module = get_settings_module(config)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

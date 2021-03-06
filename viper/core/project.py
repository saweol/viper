# This file is part of Viper - https://github.com/viper-framework/viper
# See the file 'LICENSE' for copying permission.

import os
from os.path import expanduser
import logging

from viper.core.config import Config
from viper.core.logger import init_logger

log = logging.getLogger('viper')

cfg = Config()

class Project(object):
    def __init__(self):
        self.name = None
        self.path = None
        self.base_path = None
        if cfg.paths.storage_path:
            self.path = cfg.paths.storage_path
            self.base_path = cfg.paths.storage_path
        else:
            self.path = os.path.join(expanduser("~"), '.viper')
            self.base_path = os.path.join(expanduser("~"), '.viper')

        if not os.path.exists(self.path):
            os.makedirs(self.path)

        if cfg.logging.log_file:
            log_file = cfg.logging.log_file
        else:
            log_file = os.path.join(self.base_path, "viper.log")
        init_logger(log_file_path=log_file, debug=cfg.logging.debug)
        log.debug("logger initiated")

    def open(self, name):
        if not os.path.exists(self.base_path):
            raise Exception("The local storage folder does not exist at path {}".format(
                base_path))

        if name == 'default':
            path = self.base_path
        else:
            path = os.path.join(self.base_path, 'projects', name)
            if not os.path.exists(path):
                os.makedirs(path)

        self.name = name
        self.path = path

    def get_path(self):
        if self.path and os.path.exists(self.path):
            return self.path
        else:
            return self.path

    def get_projects_path(self):
        return os.path.join(self.base_path, 'projects')

__project__ = Project()

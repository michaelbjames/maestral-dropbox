# -*- coding: utf-8 -*-
#
# Copyright © Spyder Project Contributors
# Licensed under the terms of the MIT License
# (see spyder/__init__.py for details)

"""
Maestral configuration options

Note: The 'account' section is used for internal purposes only to store some
basic information on the user account between connections. The 'internal'
section saves cursors and time-stamps for the last synced Dropbox state and
local state, respectively. Resetting those to the default values will trigger
a full download on the next startup.
"""

import os

# Local import
from .user import UserConfig
from .base import migrate_config_files

PACKAGE_NAME = os.getenv('MAESTRAL_CONFIG', 'maestral')
SUBFOLDER = 'maestral'


# =============================================================================
#  Defaults
# =============================================================================
DEFAULTS = [
            ('main',
             {
              'path': '',
              'default_dir_name': 'Dropbox (Maestral)',
              'excluded_folders': [],
              'excluded_files': ['desktop.ini',  'thumbs.db', '.ds_store',
                                 'icon\r', '.dropbox.attr', '.dropbox', '.maestral'],
              }),
            ('account',
             {
              'account_id': '',
              'email': '',
              'display_name': '',
              'abbreviated_name': '',
              'type': '',
              'usage': '',
              'usage_type': '',
              }),
            ('app',
             {
              'notifications': True,
              'log_level_file': 20,
              'log_level_console': 20,
              }),
            ('internal',
             {
              'cursor': '',
              'lastsync': None,
              'recent_changes': [],
              }),
            ]


# =============================================================================
# Config instance
# =============================================================================
# IMPORTANT NOTES:
# 1. If you want to *change* the default value of a current option, you need to
#    do a MINOR update in config version, e.g. from 3.0.0 to 3.1.0
# 2. If you want to *remove* options that are no longer needed in our codebase,
#    or if you want to *rename* options, then you need to do a MAJOR update in
#    version, e.g. from 3.0.0 to 4.0.0
# 3. You don't need to touch this value if you're just adding a new option
CONF_VERSION = '3.4.0'

migrate_config_files()

# Main configuration instance
try:
    CONF = UserConfig(PACKAGE_NAME, defaults=DEFAULTS, load=True,
                      version=CONF_VERSION, subfolder=SUBFOLDER, backup=True,
                      raw_mode=True)
except Exception:
    CONF = UserConfig(PACKAGE_NAME, defaults=DEFAULTS, load=False,
                      version=CONF_VERSION, subfolder=SUBFOLDER, backup=True,
                      raw_mode=True)

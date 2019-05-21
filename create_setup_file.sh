#!/bin/bash
touch refactor_oc/refactor_oc/local_settings.py
echo -e $'import sys\n
if \'test\' in sys.argv:\n
  DATABASES = {\n
    \'default\': {\'ENGINE\': \'django.db.backends.sqlite3\'}\n
  }' > refactor_oc/refactor_oc/local_settings.py
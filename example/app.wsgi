import sys
import os
sys.path.insert(0, r'{{APP_PATH}}')
activate_this = r'{{APP_PATH}}/.venv/Scripts/activate_this.py' if os.path.isdir(r'{{APP_PATH}}/.venv/Scripts') else r'{{APP_PATH}}/.venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
from {{APP_NAME}} import app
application = app.app
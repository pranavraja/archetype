# Setup

Run the following to bootstrap your flask template app:

	virtualenv .venv --distribute
	.venv/bin/activate or .venv\Scripts\activate.bat
	pip install -r requirements.txt
	python debug.py

The app should now be serving on [http://localhost:5000/](http://localhost:5000/).

In production, the app can be run from a WSGI-compatible server using `app.wsgi`. To configure Apache, add the following to your httpd.conf:

	<VirtualHost *>
        ServerName your.domain.com
        WSGIScriptAlias /{{APP_NAME}} {{APP_PATH}}/app.wsgi
        <Directory {{APP_PATH}}>
                Order deny,allow
                Allow from all
        </Directory>
    </VirtualHost>
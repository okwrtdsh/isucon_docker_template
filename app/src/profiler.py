#!flask/bin/python
from werkzeug.contrib.profiler import ProfilerMiddleware, MergeStream
from app import app

app.config['PROFILE'] = True
app.wsgi_app = ProfilerMiddleware(app.wsgi_app, profile_dir="/tmp/profiles")
app.run(debug = True)

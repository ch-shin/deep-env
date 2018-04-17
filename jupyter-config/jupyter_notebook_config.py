from os import environ as env
from notebook.auth import passwd

c = get_config()
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.open_browser = False
c.NotebookApp.allow_root = True
c.NotebookApp.notebook_dir = env['HOME']
c.NotebookApp.password = unicode(passwd(env['JUPYTER_PASSWD']))

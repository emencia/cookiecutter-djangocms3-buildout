# -*- coding: utf-8 -*-
INSTALLED_APPS = add_to_tuple(INSTALLED_APPS, 'sendfile')

# Backend type: do not define any other backend that the development one, for 
# other environnement define backend in their own setting file
SENDFILE_BACKEND = 'sendfile.backends.development' # Dummy backend for django's wsgi 'runserver'
#SENDFILE_BACKEND = 'sendfile.backends.nginx' # For Nginx
#SENDFILE_BACKEND = 'sendfile.backends.xsendfile' # For Apache or Lighttpd

# Protected files directory name, this dir have to exists in your project, but don't put 
# it under media or static dir as it will be served unprotected
PROTECTED_MEDIAS_DIRNAME = 'protected_medias'

# Send File paths and url
SENDFILE_ROOT = join(PROJECT_PATH, PROTECTED_MEDIAS_DIRNAME)
SENDFILE_URL = '/%s' % PROTECTED_MEDIAS_DIRNAME

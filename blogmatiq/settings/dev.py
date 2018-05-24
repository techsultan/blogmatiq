from blogmatiq.settings.main import * 



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


STATIC_ROOT = ""
MEDIA_ROOT = ""


#Django-CORS-headers configuration
# Allow requests from the Angular5 
# localhost port (4200) to go through
CORS_ORIGIN_WHITELIST = (
	'http://localhost:4200',
	'http://127.0.0.1:4200',
	)

CSRF_TRUSTED_WHITELIST = (
	'http://localhost:4200',
	)
#Only send the CORS headers for requests to the /api section
#CORS_URLS_REGEX = r'^api/.*$'

CORS_ALLOW_METHODS = (
	'DELETE',
	'GET',
	'OPTIONS',
	'PATCH',
	'POST',
	'PUT'
	)

#List of non-standard HTTP headers that can be used when making the actual request
from corsheaders.defaults import default_headers
CORS_ALLOW_HEADERS = default_headers

CORS_ORIGIN_ALLOW_ALL = True

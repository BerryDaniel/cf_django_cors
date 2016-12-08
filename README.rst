==============
cf_django_cors
==============

django middleware to add cors response headers without a proxy server


Configuration
-------------

Add the following to the django settings

.. code-block:: python

   MIDDLEWARE_CLASSES = (
       'exchange.cors.middleware.CorsMiddleware',
   ) + MIDDLEWARE_CLASSES

By default this will add the following "response" headers:

.. code-block::

   Access-Control-Allow-Headers:x-requested-with, Content-Type, origin, authorization, accept, client-security-token
   Access-Control-Allow-Methods:DELETE, GET, OPTIONS, POST, PUT
   Access-Control-Allow-Origin:*
   Access-Control-Max-Age:1000

In order the adjust the headers, you will need to set the following OS environments:

+ ALLOW_ORIGIN (string)
+ ALLOW_HEADERS (string)
+ ALLOW_METHODS (string)
+ MAX_AGE (integer)

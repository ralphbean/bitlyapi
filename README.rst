=====================
Python bit.ly wrapper
=====================

This is a thin Python wrapper for the `bit.ly API`_.  Basic usage looks like
this::

  >>> import bitlyapi
  >>> b = bitlyapi.BitLy(api_user, api_key)
  >>> url = 'http://www.google.com/'
  >>> res = b.shorten(longUrl=url)
  >>> 
  >>> print res[url]['shortUrl']
  http://bit.ly/6Hwstb

The return from any method call is a dict containing the results of
decoding the JSON returned from bit.ly.  For example::

  >>> import pprint
  >>> pprint.pprint(res)
  {'http://www.google.com/': {'hash': '2V6CFi',
                              'shortCNAMEUrl': 'http://bit.ly/6Hwstb',
                              'shortKeywordUrl': '',
                              'shortUrl': 'http://bit.ly/6Hwstb',
                              'userHash': '6Hwstb'}}

You can supply arbitrary keywords to method calls and they will be passed
to the `bit.ly API`_::

  >>> res = b.shorten(longUrl=url, keyword='mycustomkeyword')

.. Note::

    Requesting custom short links using the `keyword` argument is not supported
    anymore by the API.

.. _bit.ly API: http://code.google.com/p/bitly-api/wiki/ApiDocumentation


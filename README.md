# Masque - Simple Urlopen() Disguising
**masque** is a simple Python 3 module designed to wrap the standard ```urlopen()``` function from ```urllib```. This module is designed to help hide scraping or crawling activity and evade common user-agent filters. It can be configured to include randomized sets of HTTP headers with the outbound request, using values common with a variety of browsers and desktop environments. It includes a standard set of HTTP headers that can be added to requests specified in the ```headers.json``` file, including:

* Accept (Always added by default)
* User-Agent (Always added by default)
* Accept-Language
* Cache-control
* Referer
* Sec-CH-UA-Mobile
* Sec-CH-UA-Platform
* Sec-Fetch-Mode
* Sec-Fetch-User
* Upgrade-Insecure-Requests
* Via
<!-- HTML comment to break list at end -->
In addition to randomizing the HTTP headers, **masque** can also add a randomized time delay before each request is opened. This can be configured via the ```settings.json``` configuration file. This feature is designed to avoid bans for potential DDoS behavior and to make the crawler/scraper less predictable.

# Using Masque

**masque** can be easily installed in existing or new Python applications. Simply copy ```masque.py``` and the ```conf``` directory into your Python code directory, and replace all existing imports of urlopen() with the **masque** equivalent:

```python
from masque import urlopen

print(urlopen('https://en.wikipedia.org/wiki/Python_(programming_language)').read())
```

You can use **masque**'s ```urlopen()``` function exactly as you would the standard ```urllib``` version. This includes the ability to pass in data for POST requests, use a pre-built ```Request``` object, and set custom timeouts.

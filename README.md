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

Tl;dr coming soon

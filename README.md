# jsO2D

Often when using HTTP requests to fetch information within HTML, I find that the information I'm looking for is actually buried deep in the JS of <script> element, which was intended to be rendered by a web browser to compose the finished HTML.

This makes the information significantly more difficult to parse out than if it was accessible in ordinary HTML elements by CSS Selectors.

So, I wrote myself a helper function to parse out object variables from JavaScript, remove their comments so they're valid JSON, and convert them to Python dictionaries so I can feaibly access their information.

Use:
```
"""
pass the JavaScript element's name and its <script> element's text to jsO2D.js_obj_from_script_to_dict
and you have yourself a navigable Python dictionary with little effort
"""
>>> import requests
>>> from bs4 import BeautifulSoup
>>> import re
>>> import jsO2D
>>>
>>>
>>> url = "https://www.youtube.com/feed/storefront"
>>> response = requests.get(url)
>>> soup = BeautifulSoup(response.text, "html.parser")
>>> pattern = re.compile(r"ytInitialData\s=\s({.*});")
>>> script_elem = soup.find("script", text=pattern)
>>>
>>> dicty = jsO2D.js_obj_from_script_to_dict("ytInitialData", script_elem.string)
>>> print(list(dicty.keys()))
['responseContext', 'contents', 'header', 'trackingParams', 'topbar']
>>>
```
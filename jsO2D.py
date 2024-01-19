import re
import regex  # conditional look-arounds
import json

# legit regex: (?<=javascript_object_name\s*=\s*){.+?}(?=;)


def js_obj_from_script_to_dict(javascript_object_name, script):
    """
    parses Javascript for an object and returns it as a dictionary
    """

    def _remove_comments(string):
        """
        removes comments from JS source
        """
        pattern = r"(\".*?\"|\'.*?\')|(/\*.*?\*/|//[^\r\n]*$)"
        regex = re.compile(pattern, re.MULTILINE | re.DOTALL)

        def _replacer(match):
            if match.group(2) is not None:
                return ""
            else:
                return match.group(1)

        return regex.sub(_replacer, string)

    reggy = rf"(?<={javascript_object_name}\s*=\s*){{.+?}}(?=;)"
    jaysean = regex.search(reggy, _remove_comments(script))
    sanjay = json.loads(jaysean.group())
    return sanjay


def demo():
    import requests
    from bs4 import BeautifulSoup

    url = "https://www.youtube.com/feed/storefront"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    for script in soup.find_all("script"):
        try:
            dicty = js_obj_from_script_to_dict("ytInitialData", script.string)
        except AttributeError:
            pass
        except TypeError:
            pass

    print(list(dicty.keys()))

import re
import regex  # conditional look-arounds
import json
# legit regex: (?<=var(.|\n)*?javascript_object_name(.|\n)*?=(.|\n)*?)(?<!var(.|\n)*?javascript_object_name(.|\n)*?=(.|\n)*?;(.|\n)*?)({((.|\n)*?)});


def js_obj_from_script_to_dict(javascript_object_name, script):
	"""
	parses Javascript for an object and returns it as a dictionary
	"""
	def _remove_comments(string):
		"""
		removes comments from JS source
		"""
		pattern = r"(\".*?\"|\'.*?\')|(/\*.*?\*/|//[^\r\n]*$)"
		regex = re.compile(pattern, re.MULTILINE|re.DOTALL)
		def _replacer(match):
		    if match.group(2) is not None:
		        return ""
		    else:
		        return match.group(1)
		return regex.sub(_replacer, string)


	reggy = fr"(?<=var(.|\n)*?{javascript_object_name}(.|\n)*?=(.|\n)*?)(?<!var(.|\n)*?{javascript_object_name}(.|\n)*?=(.|\n)*?;(.|\n)*?)({{((.|\n)*?)}});"
	jaysean = regex.search(reggy, _remove_comments(script))
	sanjay = json.loads(jaysean.group(8))
	return sanjay

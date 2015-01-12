import sublime


SUBLIMESETTINGS = None
SETTINGS = None


def readSettings(config):
	global SETTINGS, SUBLIMESETTINGS
	SUBLIMESETTINGS = sublime.load_settings("Preferences.sublime-settings")
	SETTINGS = sublime.load_settings(config)


def getDefaultSettings(key, val=None):
	global SUBLIMESETTINGS
	if SUBLIMESETTINGS is None:
		return val
	return SUBLIMESETTINGS.get(key, val)

def getSettings(key, val=None):
	global SETTINGS
	if SETTINGS is None:
		return val
	return SETTINGS.get(key, val)

def isValidBracket(bracket):
	for pair_obj in getSettings("brackets", []):
		pair = pair_obj["bracket"]
		if len(pair) == 1:
			if pair == bracket:
				return True
		else:
			if pair[0] == bracket or pair[1] == bracket:
				return True
	return False

def isPairBracket(bracket):
	for pair_obj in getSettings("brackets", []):
		pair = pair_obj["bracket"]
		if len(pair) > 1:
			if pair[0] == bracket or pair[1] == bracket:
				return True
	return False

def isOpenBracket(bracket):
	for pair_obj in getSettings("brackets", []):
		pair = pair_obj["bracket"]
		if len(pair) == 1:
			if pair == bracket:
				return True
		else:
			if pair[0] == bracket:
				return True
	return False

def getMatchingBracket(bracket):
	for pair_obj in getSettings("brackets", []):
		pair = pair_obj["bracket"]
		if len(pair) == 1:
			if pair == bracket:
				return pair
		else:
			if pair[0] == bracket:
				return pair[1]
			elif pair[1] == bracket:
				return pair[0]
	return None
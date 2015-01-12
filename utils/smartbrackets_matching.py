def isInQuote(view, line, end, quote):
	isopen = False
	for pos in range(line, end):
		if view.substr(pos-1) != "\\" and view.substr(pos) == quote:
			isopen = not isopen
	return isopen

def getQuoteLevel(view, line, end, quote, level=0):
	isopen = False
	for pos in range(line, end):
		if view.substr(sublime.Region(pos, pos+(level*2)+2)) == ("\\\\"*level)+"\\"+quote:
			return self.getQuoteLevel(line, end, quote, level+1)
		elif view.substr(pos) == quote:
			isopen = not isopen
	if isopen:
		return level+1
	else:
		return level

def getQuotePair(view, line, search, quote, level=1):
	isopen = False
	found = False
	openq = None
	for pos in range(line[0], line[1]):
		# print("@" + str(pos)+"="+view.substr(pos))
		if view.substr(sublime.Region(pos, pos+((level-1)*2)+1)) == ("\\\\"*(level-1))+quote:
			isopen = not isopen
			if isopen:
				# print("Found open at " + str(pos) + "/" + str(search))
				if pos == search:
					found = True
				openq = [pos, pos+((level-1)*2)+1]
			else:
				# print("Found close at " + str(pos) + "/" + str(search))
				if pos == search:
					found = True
				if found:
					return [openq, [pos, pos+((level-1)*2)+1]]
			pos=pos+((level-1)*2)+1
	return [openq, None]
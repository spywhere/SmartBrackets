import sublime
import sublime_plugin
from ..utils import *


class SmartBracketsRemoveCommand(sublime_plugin.TextCommand):
	def isInQuote(self, line, end, quote):
		isopen = False
		for pos in range(line, end):
			if self.view.substr(pos-1) != "\\" and self.view.substr(pos) == quote:
				isopen = not isopen
		return isopen

	def getQuoteLevel(self, line, end, quote, level=0):
		isopen = False
		for pos in range(line, end):
			if self.view.substr(sublime.Region(pos, pos+(level*2)+2)) == ("\\\\"*level)+"\\"+quote:
				return self.getQuoteLevel(line, end, quote, level+1)
			elif self.view.substr(pos) == quote:
				isopen = not isopen
		if isopen:
			return level+1
		else:
			return level

	def getQuotePair(self, line, search, quote, level=1):
		isopen = False
		found = False
		openq = None
		for pos in range(line[0], line[1]):
			# print("@" + str(pos)+"="+self.view.substr(pos))
			if self.view.substr(sublime.Region(pos, pos+((level-1)*2)+1)) == ("\\\\"*(level-1))+quote:
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


	def run(self, edit, left_delete=True):
		for sel in self.view.sel():
			if sel.empty():
				if left_delete:
					text = self.view.substr(sel.a-1);

					# if is pairBracket
					#	 pair = getBracketPair(text) # Both from open and close bracket
					# 	 erase pair
					# else
					# 	 pair = getQuotePair(text)
					#	 erase pair

					if isValidBracket(text) and isOpenBracket(text):
						line = self.view.line(sel.a-1)
						close = None
						balance = 0

						if isPairBracket(text):
							for pos in range(sel.a, self.view.size()):
								if self.view.substr(pos) == text:
									balance = balance+1
								if self.view.substr(pos) == getMatchingBracket(text):
									if balance == 0:
										close = sublime.Region(pos, pos+1)
										break
									else:
										balance = balance-1
						if close is not None:
							self.view.erase(edit, close)


					if isValidBracket(text) and isOpenBracket(text) and not isPairBracket(text):
						line = self.view.full_line(sel.a)
						print("Quote Level: " + str(self.getQuoteLevel(line.begin(), sel.a, text)))
						pair = self.getQuotePair([line.begin(), line.end()], sel.a-1, text)
						print("Pairs: "+str(pair))
						if pair[1] is not None:
							self.view.erase(edit, sublime.Region(pair[1][0],pair[1][1]))
						if pair[0] is not None:
							self.view.erase(edit, sublime.Region(pair[0][0],pair[0][1]))
					else:
						self.view.erase(edit, sublime.Region(sel.a-1,sel.a))

					if isValidBracket(text) and not isOpenBracket(text):
						line = self.view.line(sel.a-1)
						close = None
						balance = 0

						if isPairBracket(text):
							for pos in range(sel.a-1, 0, -1):
								if self.view.substr(pos) == text:
									balance = balance+1
								if self.view.substr(pos) == getMatchingBracket(text):
									if balance == 0:
										close = sublime.Region(pos, pos+1)
										break
									else:
										balance = balance-1
						if close is not None:
							self.view.erase(edit, close)
				else:
					text = self.view.substr(sublime.Region(sel.a,sel.a+1));
					self.view.erase(edit, sublime.Region(sel.a,sel.a+1))
			else:
				self.view.erase(edit, sel)

	def description(self, left_delete=True):
		if left_delete:
			return "Left Delete"
		else:
			return "Right Delete"

# "a"b"c""d"e"f"
# " \" \\\" \\\" \" "
# " \"  \" "
# a[c[e[]f]d]b
# [({[({})]})]
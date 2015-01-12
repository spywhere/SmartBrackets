import sublime
import sublime_plugin
from ..utils import *


class SmartBracketsAddCommand(sublime_plugin.TextCommand):
	def run(self, edit, bracket):
		sels = self.view.sel()
		nsels = []
		for sel in sels:
			if sel.empty():
				# if inside quote, insert once

				self.view.insert(edit, sel.begin(), bracket)
				if getDefaultSettings("auto_match_enabled") and isValidBracket(bracket) and isOpenBracket(bracket):
					self.view.insert(edit, sel.begin()+1, getMatchingBracket(bracket))
				nsels.append(sublime.Region(sel.begin()+1, sel.begin()+1))
			else:
				if getDefaultSettings("auto_match_enabled") and isValidBracket(bracket) and isOpenBracket(bracket):
					self.view.insert(edit, sel.end(), getMatchingBracket(bracket))
					self.view.insert(edit, sel.begin(), bracket)
					nsels.append(sublime.Region(sel.begin()+1, sel.end()+1))
				else:
					self.view.erase(edit, sel)
					self.view.insert(edit, sel.begin(), bracket)
					nsels.append(sublime.Region(sel.begin()+1, sel.begin()+1))

		self.view.sel().clear()
		for sel in nsels:
			self.view.sel().add(sel)

	def description(self, bracket):
		return "Insert Characters"
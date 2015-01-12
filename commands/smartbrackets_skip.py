import sublime
import sublime_plugin


class SmartBracketAddCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.run_command("move", {"by": "characters", "forward": True})

	def description(self):
		return "Insert Characters"

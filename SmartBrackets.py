import sublime
from .commands import *
from .utils import *


def plugin_loaded():
	# auto_match_enabled
    readSettings("SmartBrackets.sublime-settings")
    # print(getMatchingBracket(""))
    # print(str(isPairBracket("\"")))
    pass

# a[c{e(test)f}d]b
# {([(["([{}])"])])}

'''
Demonstration
=============

abc.push("A");

convert to

abc[]="A";

'''
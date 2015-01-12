## SmartBrackets

A better brackets matching plugin for Sublime Text 3

### Features
 * Bracket level matching
 * Add and remove brackets as a pair
 * Bracket completion, exclusively for Objective-C

### Important Notes
On completion of SmartBrackets, it will override `Backspace`, `Delete` and all brackets key bindings as default. If you are using these keys, please check the settings before use.

By now, SmartBrackets only override `Backspace` key and still use default Sublime Text's brackets adding feature.

Note! SmartBrackets will do all the same default actions as Sublime Text does when no bracket matching is used.

### How it's work
Brackets in SmartBrackets have 2 types...

 * Open/Close
    * Consists of open bracket and close bracket such as: [] or ()
    * This type of bracket will work almost the same as Sublime Text 3 does
 * Quote
 	* Consists of only character that use both open and close such as: " or '
 	* This type of bracket required a escape character to be used as a nested quote
 	* This type of bracket will matched the highlighted quote and will be nested when multi-level quotes are found

### Installation
By now, SmartBrackets is not ready for public distribution due to unstable brackets adding feature. But if you want, you can clone this repository into your *Sublime Text 3 / Packages* folder by using...

	cd PACKAGES_PATH
	git clone git://github.com/spywhere/SmartBrackets.git

PACKAGES_PATH is related to folder which can be accessed via the *Preference > Browse Packages...*

### Settings
Settings are accessed via the *Preferences > Package Settings > SmartBrackets*

Default settings should not be modified. However, you can copy the relevant settings into SmartBrackets user settings file
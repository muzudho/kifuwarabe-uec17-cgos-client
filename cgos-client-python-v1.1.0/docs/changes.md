# Python CGOS Client - Change Log


## Version 1.0.0

* Add genmove_analyze extention


## Version 0.3.1

* Fix for configuration: passing multiple parameters to engine should now work properly on non-Windows sytems


## Version 0.3.0

* Support for multiple engines
* Backwards-incompatible configuration file changes:
	* New mandatory attribute **Name** for each engine, giving display name
	* New mandatory attribute **NumberOfGames** for each engine, indicating how many games it plays  
	  before switching to next

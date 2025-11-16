# Python CGOS Client - むずでょブランチ版

This client connects Go programs that implement the [GTP](http://www.lysator.liu.se/~gunnar/gtp/)
protocol to the	[Computer Go Server](http://www.yss-aya.com/cgos/) (CGOS). If you downloaded this, you know what they are.
*Any* GTP engine is supported, not just those written in Python.

## Information

This is version **1.0.0**.  


Original CGOS Python client was developed by &copy;2009 Christian Nentwich and [contributors](contributors.html)  
and is licensed to you under the terms of the  
[GNU General Public License version 3 (GPLv3)](http://www.opensource.org/licenses/gpl-3.0.html).  

CGOS was developed and operated by Don Daily from 2007 to 2012; Hiroshi Yamashita reopened the server in 2015.  

Major changes in version 1.0.0 include Python3 support and support for sending analysis information.  

Please read the [change log](changes.html).  

**For the avoidance of doubt:** this licence makes no claim *whatsoever* about the Go programs  
used with this client, in particular any programs using this client to connect to CGOS shall **not**  
meet the definition of a "covered work", or derivative work, under this license.  

The CGOS server and TCL client are &copy; Don Daily and others and are not included here.  

* [Features](#features)
* [Usage](#usage)
* GTP
	* [GTP Commands](#gtp)
	* [GTP Extensions](#ext)
	* Configuration
		* [Logging](#logging)
		* [Displaying Games using GoGUI](#observer)
		* [Alternating Between Multiple Engines](#multipleengines)
		* [Sample Configuration](#samplecfg)

<a name="features"></a>
## Features

Features in common with standard CGOS TCL client:  

* Textual configuration file
* Waits for server restart when server crashes or is unreachable (checks every 30 seconds + small random amount)
* Supports resume if the engine crashes. Just restart the client and it will catch up the game.
* Kill file to terminate connections
* Supports multiple engines, and automatic switching (but <a href="#multipleengines">the behaviour</a> is slightly different)

Additional features:  

* Local SGF persistence (with move times and results)
* Support for [observers](#observer). Any GTP engine or display,  
  like [GoGUI](http://gogui.sourceforge.net/), can be used to observe games locally.
* [GTP extensions](#ext) that can help with your engine's logging
* Separate detailed [logging files](#logging) for: CGOS, the engine and the observer (if any). Standard output  
  stream logging at high level for user observation.
* From time to time, shows some stats: uptime, games won, games lost. May be expanded with e-mail notification in the future.

Features not yet supported:  

* Engine switching is not yet supported


<a name="usage"></a>
# Usage

Developed on Python 3.10, no extensions required. It may work on Python 2.5, but that is not tested. If you are using Windows,  
get the package	from [here](http://www.python.org/download/windows/), it's a good standalone installer.  
You will have to provide a configuration file. See `sample.cfg` for an example, or see [below](#samplecfg).  
Run the client using:  

PowerShell ではなく、Command Prompt を使ってください。  

```shell
# Windows
cd cgos-client-python-v1.1.0-muzudho-branch
#C:\Python3\Python src\cgosclient.py config.cfg
python src\cgosclient.py config.cfg
```

To kill the client, please place a "kill file" in the location you specified in the configuration  
file. You may of course kill the process, too, but the kill file will ensure that you will finish  
the current game and log off nicely. After the engine quits, the kill file will be deleted.  

**Note:** If a kill file is put in place, the client will quit ASAP if it is not currently in  
a game. In practice, this means when the next status message is received by the server, usually within a minute.  


<a name="gtp"></a>
## GTP Commands

*Playing* engines need the following GTP commands:  

* Mandatory: **list_commands**, **boardsize**, **clear_board**, **komi**, **play**, **genmove**, **quit**
* Optional: **time_left**, **time_settings**

If the time commands are missing, no time control instructions will be passed to the engine. Further notes:  

* **time_left** will always be sent immediately before **genmove**, as with the TCL client
* **quit**: if your engine or observer takes too long to respond, it will be sent a terminate signal to  
  make sure it does not get up anymore


### Command Ordering and Game Control

It can be difficult for a GTP engine to decide when a game has started or a game is over. With the Python CGOS client,  
you can infer the following:  

* `clear_board` will be the decisive command indicating that the game has started. All time setup and board  
  setup happens before it. There *may* be a list of `play` commands sent in rapid succession after  
  `clear_board`, but only if the connection or server previously crashed and the game needs to be caught up. In  
  principle, you can trigger any pondering code after `clear_board`.
* `cgos-gameover`, described in the next section, definitively ends the game. You may deallocate  
  resources in response to this command.


<a name="ext"></a>
## GTP Extensions

The following GTP extensions are available. If your engine records its own logs, or writes its own  
SGF records with analysis information in them, you may find them useful.  

|Command|When Called|Meaning|
|----|----|----|
|cgos-opponent_name|Between boardsize and clear_board|Gives the name of the opponent engine (the CGOS login name)|
|cgos-opponent_rating|Between boardsize and clear_board|Gives the current CGOS rating of the opponent engine. This will be a<br/>number or a number followed by a question mark|
|cgos-gameover|After two passes, resignation or illegal move|Final result as reported by the server. Will be in format required by SGF<br/>[RE](http://www.red-bean.com/sgf/properties.html#RE) property, meaning:<br/><ul><li><code>B+{score}</code> or <code>W+{score}</code>, e.g. <code>B+0.5</code>, or</li><li><code>B+Resign</code> or <code>W+Resign</code>, or</li><li><code>B+Time</code> or <code>W+Time</code>, or</li><li><code>B+Forfeit</code> or <code>W+Forfeit</code></li></ul>|


<a name="logging"></a>
## Logging

The client will produce the following log files at debug level - standard output stream  
logging is at info level or higher only:  

* **engine.log** - Log of GTP command stream to and from the engine
* **cgos.log** - Client/server command stream
* **observer.log** - Log of GTP stream to observer GTP engine, if any

All of these log files are set up as rolling files that be renamed `engine.log.1`,  
and so on, when they get beyond 2MB. A maximum of 5 rolling log files is kept.  


<a name="observer"></a>
## Displaying Games Using GoGUI

The Python CGOS client can stream the GTP command stream to a secondary engine called  
an "observer" engine. It is up to you how you use this, for example:  

* You could run a secondary copy of your program and show move evaluations
* You can run GoGUI and get a local view of what your program is doing when it is  
  playing. This means that a) you do not have to connect using the server viewing client  
  and b) you save the server a bit of work.

First, download GoGUI from [gogui.sourceforge.net](http://gogui.sourceforge.net/).  
Next, make sure you use <code>gogui-display</code> as an observer in your configuration file,  
like so in Windows:  

```
GTPObserver:  
    CommandLine = C:\Program Files\Java\jdk1.6.0_13\bin\java.exe -jar C:\path\to\gogui-1.1.9\lib\gogui-display.jar
```

Please do **not** use `javaw.exe`, stick with `java.exe`, or the input stream to  
gogui-display will be cut off. In Linux:  

```
GTPObserver:
    CommandLine = /usr/bin/java -jar /path/to/gogui-1.1.9/lib/gogui-display.jar
```

Either way, please note that if you close the GoGUI window, the client will think the observer  
engine crashed and terminate your connection. You will then have to restart to resume your game.  
If you wish to stop displaying, put a kill file in place (see above), then start the client  
again without an observer.  

<a name="multipleengines"></a>
## Alternating Between Multiple Engines

In the [configuration file](#samplecfg), each GTP engine has an attribute called  
`NumberOfGames`. This attribute is mandatory in this version of the client, even if there  
is only one engine, though in the case of one engine it is ignored.  
Multiple GTP engines are played sequentially in a round-robin fashion. For example, if  
`NumberOfGames` is set to 2 for **EngineA** and to 3 for **EngineB**, the client  
will play the engines as follows:  

|Game|Engine|
|----|----|
|1|EngineA|
|2|EngineA|
|3|EngineB|
|4|EngineB|
|5|EngineB|
|6|EngineA|
|7|EngineA|
|8|EngineB|
|9|...|

Recommendations:  

* If you are planning to play for a long time (e.g. a day or longer of 9x9), set the  
  game counts to five or higher. This minimises the number of reconnects and restarts that have to be  
  performed.
* If your engines leak memory, set it lower - but set up at least two engines or the  
  attribute will be ignored.


<a name="samplecfg"></a>
## Sample Configuration

This sample configuration shows how [GNU Go](http://www.gnu.org/software/gnugo/)  
can be connected to play on CGOS, 9x9 board size, and with GoGUI running locally to view all  
games.  

In addition, the client will play round-robin between two engine configurations, running the  
engine at level 8 for 5 games, followed by level 10 for 2 games, and then starting over.  


```ini
Common:
  KillFile = kill.txt

GTPEngine:
  # Name to display on console / in logs
  Name = Gnugo Level 8

  CommandLine = gnugo.exe --mode gtp --score aftermath --capture-all-dead --chinese-rules --level 8

  ServerHost = cgos.boardspace.net
  ServerPort = 6867
  ServerUser = myuser
  ServerPassword = mypw

  # Switch to next engine after this many games
  NumberOfGames = 5

  # Optional: persist games here
  SGFDirectory = ..\sgf9x9

GTPEngine:
  Name = Gnugo Level 10
  CommandLine = gnugo.exe --mode gtp --score aftermath --capture-all-dead --chinese-rules --level 10

  ServerHost = cgos.boardspace.net
  ServerPort = 6867
  ServerUser = myuser-level10
  ServerPassword = mypw-level10

  # Switch back to first engine after this many games
  NumberOfGames = 2

  # Optional: persist games here
  SGFDirectory = ..\sgf9x9


# Observer engine (e.g. GoGUI)
GTPObserver:
  CommandLine = C:\Program Files\Java\jdk1.6.0_13\bin\java.exe -jar C:\path\to\gogui-1.1.9\lib\gogui-display.jar
```

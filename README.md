# HT_Resolve_Python
Python scripts and notes for Resolve



## Setup on Mac
I am still trying to figure this out.  The following is what I think made it work on my iMac Pro, but it did not work - and still does not - on my MacBook Pro.  When I figure out what works properly, I will update this read-me.

It looks like Resolve needs the stock 3.6 python.  I picked up the package for Apple here:  https://www.python.org/ftp/python/3.6.7/python-3.6.7-macosx10.9.pkg

Once that is installed, your ~/.bash_profile will be updated, but that won't matter because nothing will use that if launched from launchd.

It may be that you need launchctl to set the environment which I think can be done with a LaunchAgent.  Some research lead me to the environment.plist that I have put into the LaunchAgents folder of this repo.  You can copy that to your ~/Library/LaunchAgents folder and it should set the environment thet next time you start.  Like I said, above, this is not yet working on my MacBook, but I believe it is what allowed Resolve to find Python 3.6.6 on my iMac Pro.

You also may need to set the Python Version to 3.6 in the "Script" panel in "Fusion Settings". To do that, open the Fusion Page, click on the Fusion menu and select "Fusion Settings".  From the pop-up dialog, click on "Script" on the left side and select "3.6".

The scripts need to be in the Comp folder to be found by Resolve. The setupEnv.py script can be run from a terminal (shell) to install the files like this:  'python3 setupEnv.py'

## NOTE:  There is no warrenty or guarantee with these.  These are experiments. Use at your own risk but feel free to submit pull requests if you fix or improve something.

They are experiments and/or starting points for things I hope to have working eventually.


## Installation:

To get these working for Resolve, copy these files to "/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Scripts/Comp/"
You can copy these by running the setupEnv.py script like this:  'python3 setupEnv.py'


## Files:

- LaunchAgents/environment.plist -  I believe this sets the environment when launching Resolve and other tasks.  Put this in ~/Library/LaunchAgents and it should let you run python3 from Resolve.
- listClipDescriptionAndKeywords.py - lists the clips in the open project
- moveMetaDataCommentsToKeywords.py - moves descriptions to keywords.  note that descriptions with commas (,) will become multiple keywords.
- removeAllKeywords.py - remove all keywords from all clips
- setupEnv.py - import this to get the module loaded from a hard-coded path if needed.  This script removes the need to copy the Resolve script into the Comp folder.
- test.py - just a test of the python in resolve.  Lists all the clips that are used in the media pool.
- whatVersion.py - just reports the version of python


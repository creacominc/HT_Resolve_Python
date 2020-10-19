# HT_Resolve_Python
Python scripts for Resolve


## Setup on Mac
It looks like Resolve needs they stock 3.6 python.  I picked up the package for Apple here:  https://www.python.org/ftp/python/3.6.7/python-3.6.7-macosx10.9.pkg

Once that is installed, your ~/.bash_profile will be updated, but that won't matter because nothing will use that if launched from launchd.

To get the correct path and use your own scripts within Resolve, copy the resolve setup from "/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting/Examples/python_get_resolve.py" to your python script folder: "/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Scripts/Comp/"

I won't include python_get_resolve.py here since it should be shipped with Resolve.

My scripts include it so that it can load the Resolve python class when it cannot find it using the missing environment variables.

## NOTE:  Note all of these work.

They are experiments and/or starting points for things I hope to have working eventually.


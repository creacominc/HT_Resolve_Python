# HT_Resolve_Python
Python scripts and notes for Resolve



## Setup on Mac

It looks like Resolve needs the stock 3.6 python.  I picked up the package for Apple here:  https://www.python.org/ftp/python/3.6.7/python-3.6.7-macosx10.9.pkg

The scripts need to be in the Comp folder to be found by Resolve. The setupEnv.py script can be run from a terminal (shell) to install the files like this:  'python3 setupEnv.py'

## NOTE:  There is no warrenty or guarantee with these.  These are experiments. Use at your own risk but feel free to submit pull requests if you fix or improve something.

They are experiments and/or starting points for things I hope to have working eventually.


## Installation:

To get these working for Resolve, copy these files to "/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Scripts/Comp/"
You can copy these by running the setupEnv.py script like this:  'python3 setupEnv.py'

## Usage:

To use the scripts, click on Workspace->Scripts->Comp then select the script you want to run.  If there are errors or output, they will appear in the Console which you can see with Workspace->Console.


## Files:

- LaunchAgents/environment.plist -  I believe this sets the environment when launching Resolve and other tasks.  Put this in ~/Library/LaunchAgents and it should let you run python3 from Resolve.
- listClipDescriptionAndKeywords.py - lists the clips in the open project
- moveMetaDataCommentsToKeywords.py - moves descriptions to keywords.  note that descriptions with commas (,) will become multiple keywords.
- removeAllKeywords.py - remove all keywords from all clips
- setupEnv.py - import this to get the module loaded from a hard-coded path if needed.  This script removes the need to copy the Resolve script into the Comp folder.
- test.py - just a test of the python in resolve.  Lists all the clips that are used in the media pool.
- whatVersion.py - just reports the version of python
- copyFilePath.py - I was asked to create a dialog box to allow someone to copy the file path for the clip to the user selected location of the Keywords, Comments, or Description fields.  This script, once installed, can be run from Workspace->Scripts->Comp->copyFilePath and will copy the path for every clip in the project.  The path, if found, can be removed with the 'Remove' button.


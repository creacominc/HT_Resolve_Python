#!/usr/bin/env python
# 
# Create a GUI in DaVinci Resolve to allow the user to copy the file paths 
# to the Keywords, Comments, or Description field for the clip.  
# To copy the file path, select the target and click on 'Copy'.  
# To remove the path from the field, click 'Remove'.
# The 'Close' button closes the dialog without making any changes.

# This logic is based on information from 
# "Building GUIs With Fusion's UI Manager"
# see:  https://www.steakunderwater.com/wesuckless/viewtopic.php?t=1411

from setupEnv import getResolveObj

copyTo : str = ''
remove  : bool = False

def iterateFolder( folder, copyTo: str, remove: bool ):
    clips = folder.GetClipList()
    for clip in clips :
        #
        properties  = clip.GetClipProperty()
        #
        name        = properties['Clip Name']
        filePath    = properties['File Path']
        keywords    = properties['Keyword']
        #
        # skip records with no file path (ie timelines)
        if not filePath:
            continue
        #
        comments    = properties['Comments']
        keywords    = properties['Keyword']
        description = properties['Description']
        #
        if copyTo == 'Keywords':
            if (filePath in keywords) and (remove == True):
                # remove from keywords
                parts = keywords.split( filePath )
                keywords = ''
                for elem in parts:
                    keywords += elem 
                keywords = keywords.strip(', ').rstrip(', ')
                clip.SetMetadata( 'Keywords', keywords )
            elif (filePath not in keywords) and (remove == False):
                # add to keywords
                if (keywords):
                    keywords += ", "
                keywords += filePath
                clip.SetMetadata( 'Keywords', keywords )
        elif copyTo == 'Comments':
            if (filePath in comments) and (remove == True):
                # remove from comments
                parts = comments.split( filePath )
                comments = ''
                for elem in parts:
                    comments += elem 
                comments = comments.strip(', ').rstrip(', ')
                clip.SetMetadata( 'Comments', comments )
            elif (filePath not in comments) and (remove == False):
                # add to comments
                if (comments):
                    comments += ", "
                comments += filePath
                clip.SetMetadata( 'Comments', comments )
        elif copyTo == 'Description':
            if (filePath in description) and (remove == True):
                # remove from comments
                parts = description.split( filePath )
                description = ''
                for elem in parts:
                    description += elem 
                description = description.strip(', ').rstrip(', ')
                clip.SetMetadata( 'Description', description )
            elif (filePath not in description) and (remove == False):
                # add to comments
                if (description):
                    description += ", "
                description += filePath
                clip.SetMetadata( 'Description', description )
    #
    subFolders = folder.GetSubFolderList()
    for sub in subFolders:
        iterateFolder( sub, copyTo, remove )


ui = fu.UIManager
disp = bmd.UIDispatcher(ui)
# create the dialog
dlg = disp.AddWindow({'WindowTitle': 'Copy File Path To...', 'ID': 'MyWin', 'Geometry': [100, 100, 500, 75],},[
    ui.VGroup({'Spacing': 0,},[
        # Add your GUI elements here:
        ui.HGroup({'Weight': 0.0,},[
            ui.Label({'ID': 'Label', 'Text': 'Copy File Path to:', 'Weight': 0.1}),
            ui.ComboBox({'ID':'Target', 'Text':'Text Value' }),
        ]),
        ui.VGap(),
        ui.HGroup({'Weight': 0.1},[
            ui.Button({'ID': 'CopyButton', 'Text': 'Copy', 'Geometry': [0, 0, 30, 50], 'Weight': 0.1}),
            ui.Button({'ID': 'ClearButton', 'Text': 'Remove', 'Geometry': [0, 0, 30, 50], 'Weight': 0.1}),
            ui.Button({'ID': 'CloseButton', 'Text': 'Close', 'Geometry': [0, 0, 30, 50], 'Weight': 0.1}),
        ]),
    ]),
])
# get all items so that they can be modified
itm = dlg.GetItems()
# add the items to the drop-down list
itm["Target"].AddItems( ['Keywords', 'Comments', 'Description'] )

# The window was closed
def _func(ev):
    disp.ExitLoop()
dlg.On.MyWin.Close = _func

# Copy Button:
def _func(ev):
    global copyTo
    global remove
    copyTo = itm["Target"].CurrentText
    remove  = False
    disp.ExitLoop()
dlg.On.CopyButton.Clicked = _func

# Remove Button:
def _func(ev):
    global copyTo
    global remove
    copyTo = itm["Target"].CurrentText
    remove  = True
    disp.ExitLoop()
dlg.On.ClearButton.Clicked = _func

# Close Button:
def _func(ev):
    global copyTo
    global remove
    copyTo = ''
    remove  = False
    disp.ExitLoop()
dlg.On.CloseButton.Clicked = _func

# show the dialog
dlg.Show()
disp.RunLoop()
dlg.Hide()

# call the modifaction function with the parameters from the dialog
if copyTo:
    resolve = getResolveObj()
    projectManager = resolve.GetProjectManager()
    project = projectManager.GetCurrentProject()
    mediaPool = project.GetMediaPool()
    rootFolder = mediaPool.GetRootFolder()
    iterateFolder( rootFolder, copyTo, remove )

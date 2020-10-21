#!/usr/bin/env python3
from setupEnv import getResolveObj
import sys


# def iterateFolder( folder ):
#     clips = folder.GetClipList()
#     for clip in clips :
#         properties = clip.GetClipProperty()
#         name      = properties['Clip Name']
#         optimized = properties['Optimized Media']
#         #clipType  = properties['Type']
#         usage     = properties['Usage']
#         description = properties['Description']
#         comments    = properties['Comments']
#         keywords    = properties['Keyword']
#         #metaData = clip.GetMetadata()
#         print( 'Clip: [' + name + '], \tUsage: [' + usage + '], \tOptimized: [' + optimized + '],  \tDescription: [' + description + '], \tComments: [' + comments + '],\tKeywords: [' + keywords + ']' )

#     subFolders = folder.GetSubFolderList()
#     for sub in subFolders:
#         iterateFolder( sub )


KEYWORD = 'HasFusionComp'
TRACKTYPE = 'video'

resolve = getResolveObj()
projectManager = resolve.GetProjectManager()
project = projectManager.GetCurrentProject()
# mediaPool = project.GetMediaPool()
# rootFolder = mediaPool.GetRootFolder()
timelineCount = project.GetTimelineCount()
# check each timeline for a fusion comp.  if it has one and does not have the keyword, add the keyword
for tmlindx in range(int(timelineCount)) :
    timeline = project.GetTimelineByIndex( tmlindx + 1 )
    tlName = timeline.GetName()
    tlTrackCount = timeline.GetTrackCount( TRACKTYPE )
    for trackIndx in range(int(tlTrackCount)) :
        tlItems = timeline.GetItemListInTrack( TRACKTYPE, trackIndx+1 )
        for tlItem in tlItems :
            itemName = tlItem.GetName()
            fuCompCount = tlItem.GetFusionCompCount()
            if ( fuCompCount > 0 ):
                print( "timeline: " + tlName + ", track: " + str(trackIndx) + ", Name: " + itemName + ", Comps: " + str(fuCompCount) )



# iterateFolder( rootFolder )

#!/usr/bin/env python3
from setupEnv import getResolveObj
import sys

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
                # # if this clip does not have the keyword, add it.
                # clip = tlItem.GetMediaPoolItem()
                # if ( clip ) :
                #     keywords = clip.GetMetadata( 'Keywords' )
                #     if ( keywords is None or len(keywords.strip().strip(',')) == 0 ) :
                #         print( "Setting keywords to: " + KEYWORD )
                #         clip.SetMetadata( 'Keywords', KEYWORD )
                #     elif ( KEYWORD not in keywords ):
                #         print( "Adding keyword to: " + keywords )
                #         clip.SetMetadata( 'Keywords', keywords + ',' + KEYWORD )

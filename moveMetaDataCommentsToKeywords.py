#!/usr/bin/env python
from setupEnv import getResolveObj
import sys

resolve = getResolveObj()
projectManager = resolve.GetProjectManager()
project = projectManager.GetCurrentProject()
mediaPool = project.GetMediaPool()
rootFolder = mediaPool.GetRootFolder()

clips = rootFolder.GetClipList()
for clip in clips :
    properties = clip.GetClipProperty()
    name      = properties['Clip Name']
    optimized = properties['Optimized Media']
    clipType  = properties['Type']
    usage     = int(properties['Usage'])
    description = properties['Description']
    keywords    = properties['Keyword']

    metaData = clip.GetMetadata()
    if ( 'Description' in metaData ):
        description = metaData[ 'Description' ].strip()
        if ( 'Keywords' in metaData  and (len(metaData['Keywords'].strip().strip(",")) > 0)):
            keywords = metaData[ 'Keywords' ].strip()
            print( 'Appending description (' + description + ') to keywords (' + keywords + ')' )
            clip.SetMetadata( 'Keywords', keywords + ',' + description )
        else:
            print( 'Copying description (' + description + ') to keywords' )
            clip.SetMetadata( 'Keywords',  description )
        clip.SetMetadata( 'Description', '' )


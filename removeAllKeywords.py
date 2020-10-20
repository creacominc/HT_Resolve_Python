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

    if ( 'Keywords' in metaData ):
        clip.SetMetadata( 'Keywords', '' )


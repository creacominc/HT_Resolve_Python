#!/usr/bin/env python
from setupEnv import getResolveObj
import sys


def iterateFolder( folder ):
    clips = folder.GetClipList()
    for clip in clips :
        properties = clip.GetClipProperty()
        name      = properties['Clip Name']
        optimized = properties['Optimized Media']
        clipType  = properties['Type']
        usage     = int(properties['Usage'])
        description = properties['Description']
        comments    = properties['Comments']
        keywords    = properties['Keyword']
        metaData = clip.GetMetadata()
        print( 'Clip: [' + name + '], \tUsage: [' + str(usage) + '], \tOptimized: [' + optimized + '],  \tDescription: [' + description + '], \tComments: [' + comments + '],\tKeywords: [' + keywords + ']' )

    subFolders = folder.GetSubFolderList()
    for sub in subFolders:
        iterateFolder( sub )



resolve = getResolveObj()
projectManager = resolve.GetProjectManager()
project = projectManager.GetCurrentProject()
mediaPool = project.GetMediaPool()
rootFolder = mediaPool.GetRootFolder()

iterateFolder( rootFolder )

#!/usr/bin/env python
from setupEnv import getResolveObj
import sys

def iterateFolder( folder ):
    clips = folder.GetClipList()
    for clip in clips :
        properties = clip.GetClipProperty()
        #name      = properties['Clip Name']
        #optimized = properties['Optimized Media']
        #clipType  = properties['Type']
        #usage     = int(properties['Usage'])
        comments = properties['Comments']
        keywords    = properties['Keyword']

        metaData = clip.GetMetadata()
        if ( 'Comments' in metaData and (len(metaData['Comments'].strip()) > 0)):
            comments = metaData[ 'Comments' ].strip()
            if ( 'Keywords' in metaData  and (len(metaData['Keywords'].strip().strip(",")) > 0)):
                keywords = metaData[ 'Keywords' ].strip()
                print( 'Appending comments (' + comments + ') to keywords (' + keywords + ')' )
                clip.SetMetadata( 'Keywords', keywords + ',' + comments )
            else:
                print( 'Copying comments (' + comments + ') to keywords' )
                clip.SetMetadata( 'Keywords',  comments )
                clip.SetMetadata( 'Comments', '' )

    subFolders = folder.GetSubFolderList()
    for sub in subFolders:
        iterateFolder( sub )



resolve = getResolveObj()
projectManager = resolve.GetProjectManager()
project = projectManager.GetCurrentProject()
mediaPool = project.GetMediaPool()
rootFolder = mediaPool.GetRootFolder()
iterateFolder( rootFolder )


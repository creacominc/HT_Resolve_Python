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
    # move description to keyword (adding to existing keyword)
    if ( len( description ) > 0 ):
        print( 'Clip: ' + name ) 
        #print( 'Keywords: ' + keywords )
        #print( 'Description: ' + description )
        if ( len( keywords ) > 0 ):
            print( 'Appending description (' + description + ') to keywords (' + keywords + ')' )
            keywords = keywords + ',' + description
        else:
            print( 'Copying description (' + description + ') to keywords' )
            keywords = description
        rv = clip.SetClipProperty( 'Keyword', str(keywords) )
        print( rv )
        rv = clip.SetClipProperty( 'Description', str(description) )
        print( rv )
        print( clip.SetClipProperty('Take', 'Take Test') )
        print( clip.GetClipProperty( 'Take' ) )

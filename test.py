#!/usr/bin/env python
from setupEnv import getResolveObj
import sys

resolve = getResolveObj()
projectManager = resolve.GetProjectManager()
print( sys.version )

project = projectManager.GetCurrentProject()
mediaPool = project.GetMediaPool()
rootFolder = mediaPool.GetRootFolder()

clips = rootFolder.GetClipList()
for clip in clips :
    properties = clip.GetClipProperty()
    #print( properties )
    name      = properties['Clip Name']
    optimized = properties['Optimized Media']
    clipType  = properties['Type']
    usage     = int(properties['Usage'])
    if ( clipType != 'Timeline' ):
        print( 'Name=' + name + ',  optimized=' + optimized + ',  type=' + clipType + ',  usage=' + str(usage) )
        if ( usage > 0 ):
            print( 'to be optimized: ' + name )
            print( dir( clip ) )



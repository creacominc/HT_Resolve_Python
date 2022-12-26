#!/usr/bin/env python
from setupEnv import getResolveObj
import sys


def iterateFolder( folder ):
    clips = folder.GetClipList()
    for clip in clips :
        properties = clip.GetClipProperty()
        #print( f'{properties}' )
        # {'Alpha mode': 'None', 'Angle': '', 'Audio Bit Depth': '24', 'Audio Ch': '2', 'Audio Codec': 'Linear PCM', 'Audio Offset': '', 'Bit Depth': '16', 'Camera #': 'A', 'Clip Color': '', 'Clip Name': 'A208_11071937_C007.braw', 'Comments': '', 'Data Level': 'Auto', 'Date Added': 'Sun Nov 7 2021 20:39:59', 'Date Created': 'Sun Nov 7 2021 19:37:31', 'Date Modified': 'Sun Nov  7 19:37:31 2021', 'Description': '', 'Drop frame': '0', 'Duration': '00:00:10:15', 'Enable Deinterlacing': '0', 'End': '254', 'End TC': '19:37:42:07', 'FPS': 24.0, 'Field Dominance': 'Auto', 'File Name': 'A208_11071937_C007.braw', 'File Path': '/Volumes/VideoScratch/VideoProjects/LensTest/A208_11071937_C007.braw', 'Flags': '', 'Format': 'BRAW', 'Frames': '255', 'Good Take': 'false', 'H-FLIP': 'Off', 'IDT': '', 'In': '', 'Input Color Space': 'Blackmagic Design Film Gen 1', 'Input LUT': '', 'Input Sizing Preset': 'None', 'Keyword': '', 'Noise Reduction': '', 'Offline Reference': '', 'Online Status': 'Online', 'Out': '', 'PAR': 'Square', 'Proxy': 'None', 'Proxy Media Path': '', 'Reel Name': '', 'Resolution': '6144x3456', 'Roll/Card': '', 'S3D Sync': '', 'Sample Rate': '48000', 'Scene': '1', 'Sharpness': '', 'Shot': '', 'Slate TC': '19:37:31:16', 'Start': '0', 'Start KeyKode': '', 'Start TC': '19:37:31:16', 'Synced Audio': '', 'Take': '16', 'Type': 'Video + Audio', 'Usage': '2', 'V-FLIP': 'Off', 'Video Codec': 'Blackmagic RAW', 'Super Scale': 1}
        name      = properties['Clip Name']
        #optimized = properties['Optimized Media']
        #clipType  = properties['Type']
        usage     = properties['Usage']
        description = properties['Description']
        comments    = properties['Comments']
        file_path   = properties['File Path']
        keywords    = properties['Keyword']
        #metaData = clip.GetMetadata()
        clip.setMetadata( 'Keywords', keywords + ',' + file_path )
        print( 'Clip: [' + name + '], \tUsage: [' + usage 
                # + '], \tOptimized: [' + optimized 
                + '],  \tDescription: [' + description + '], \tComments: [' + comments 
                + '],\tPath: [' + file_path 
                + '],\tKeywords: [' + keywords 
                + ']' )

    subFolders = folder.GetSubFolderList()
    for sub in subFolders:
        iterateFolder( sub )



resolve = getResolveObj()
projectManager = resolve.GetProjectManager()
project = projectManager.GetCurrentProject()
mediaPool = project.GetMediaPool()
rootFolder = mediaPool.GetRootFolder()

iterateFolder( rootFolder )

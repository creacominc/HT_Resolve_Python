#!/usr/bin/env python

import sys
import imp

def getResolveObj():
        try:
                import DaVinciResolveScript as bmd
                
        except ImportError:
                try:
                        MODULE="/Library/Application Support/Blackmagic Design/DaVinci Resolve/Developer/Scripting/Modules/DaVinciResolveScript.py"
                        bmd = imp.load_source('DaVinciResolveScript',MODULE)

                except ImportError as err:
                        print( 'Failed to load resolve script: ' + MODULE )
                        print( err )
                        sys.exit()

        return bmd.scriptapp("Resolve")


if __name__ == "__main__":
        # copy the files to the Comp folder
        import glob
        from shutil import copyfile
        COMP="/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Scripts/Comp/"
        files = glob.glob("*.py")
        for file in files:
                print( file )
                copyfile( file, COMP + file )

        

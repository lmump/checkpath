# /usr/bin/python2.6

import os
import shutil
import sys
#import zip

def getargs():
    "Args for command-line mode"
    try:
        path1, path2 = sys.argv[1:]   # 2 command-line args
    except:
        print('Usage: checkpath.py path1 path2')
        print('path1 = source directroy path')
        print('path2 = destination directroy path')

        sys.exit(1)
    else:
        return (path1, path2)

def getpath(ospath, basedir):

    #
    #   get the OS version and platform name from the path
    #
    #
    # return the directory name of where we placed the ddk
    #
    return finalRestingPlace

if __name__ == '__main__':

    srcpath, destpath = getargs()

    print('\n')
    # print(sys.argv,len(sys.argv))
    print('argv[0] =', sys.argv[0])
    print('argv[1] =', sys.argv[1])
    print('argv[2] =', sys.argv[2])
    print('len of argv =', len(sys.argv))
    print('')

#  Must delete the destpath as the shutil.copytree will kick an error if
#  the destination directory already exist !!!

    if os.path.isdir(destpath):
        shutil.rmtree(destpath)
        print("Deleteing Directory -->",destpath)

    print("Creating Directroy --> ",destpath)
    print(" and Copying all the files under to  > ")
    shutil.copytree(srcpath, destpath)

    print '\nDone:'


# end if

import os
import shutil
import sys
import zip


def prep(ospath, basedir):

    #
    #   get the OS version and platform name from the path
    #
    ospathSplit = ospath.split('\\')
    version = ospathSplit[-2]
    platform = ospathSplit[-3]
    #print version, platform

    finalRestingPlace = ''

    #
    # try to find the ddk zip file.  It should start with 'Ddk'
    #
    files = os.listdir(ospath)

    found = False
    for x in files:
        if x.lower().startswith('ddk'):
            #print '\nFound =>', x
            found = True
        # end if
    # end for

    if not found:
        print "Can't find a filename starting with 'ddk'"
        quit()

    else:

        #
        # ddk found, create directory based on the platform and version
        #
        dest = basedir + '/' + platform + '/' + version + '/' + 'ptv-dual-ddk/'


        if not os.path.isdir(dest):
            os.makedirs(dest)
        finalRestingPlace = basedir + '/' + platform + '/' + version


        #
        # todo: give warning if ddk already exists
        #


        #
        # copy the ddk zip to the ptv-dual-ddk directory and unzip it
        #
        src = ospath + '/' + x
        destdir = dest;
        dest = dest + x

        #print 'Copying file to %s' % dest
        # end if
        print '\ncopying to ', dest
        shutil.copyfile(src, dest)

        os.chdir(destdir)
        print 'Unzipping file...'
        # end if
        zip.unzip('', x)


        #
        # move ddk.zip file out of ptv-dual.ddk
        #
        shutil.move(x, '../')

        #
        # was the DDK created with an extra directory layer?  If there's only one
        # file and it's a directory, move everything from THERE to HERE.
        #
        if len([f for f in os.listdir('.')]) == 1:


            for root, dir, files in os.walk(f):
                for file in files:
                    os.chmod(root + '/' + file, 0777)


            for x in os.listdir(f):

                if os.path.isdir(f + '/' + x):
                    shutil.copytree(f + '/' + x, './' + x)
                else:
                    shutil.copy(f + '/' + x, '.')

            shutil.rmtree(f)


        #
        # create new ptv-dual-ddk.zip
        #
        #print 'Zipping ptv-dual-ddk'
        # end if
        os.chdir('../')
        print 'Re-zipping file...'
        zip.zipdir('ptv-dual-ddk')
    # end if

    #
    # return the directory name of where we placed the ddk
    #
    return finalRestingPlace
# end def prepOsDdk




if __name__ == '__main__':

    args = sys.argv[1:]

    if os.path.isdir('c:/sdsz'):
        myDest = 'c:/src/ptv-os'
    else:
        myDest = ''

    if len(myDest) == 0:
        neededArgs = 2
    else:
        neededArgs = 1

    if len(args) != neededArgs:
        print 'usage  :  prepOsDdk <ddk source location> <ddk destination>'
        print 'example:  prepOsDdk \\Sausatltct01.corp.sa.net\sauscupfnp01.corp.sa.net\CupSCM\Test\SA\E1850\OS6261_4\compressed c:\src\ptv-os'
        sys.exit(1)
    # end if

    if len(args) == 2:
        myDest = args[1]

    ddkLoc = prep(args[0], myDest)

    print '\nDone:', ddkLoc


# end if



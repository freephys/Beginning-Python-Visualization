import os
def get_all_files(srchpath):
    """Get the names, paths and sizes of all the files in a directory."""
    allfiles = []

    for root, dirs, files in os.walk(srchpath):
        for file in files:
            pathname = os.path.join(root, file)
            filesize = os.path.getsize(pathname)
            allfiles.append([file, pathname, filesize])
    return allfiles

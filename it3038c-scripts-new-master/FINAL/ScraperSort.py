import shutil, os
#I learned how to use shutil to move stuff around
#If this path exists, ignore this, otherwise make this folder
if not os.path.exists('./sounds/'):
    os.mkdir('./sounds/')

#If the filename ends in these extensions, move them to sounds to become more organized
for filename in os.listdir():
    if filename.endswith('.mp3') or filename.endswith('.m4a') or filename.endswith('.FLAC'):
        shutil.move(filename, './sounds/')

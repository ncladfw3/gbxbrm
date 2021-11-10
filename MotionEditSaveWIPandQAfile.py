#Brian Mckee (brian1_nc@yahoo.com) Gearbox March 2020
#New tool to plot rigs and save out file after motion editing is done on a scene
from pyfbsdk import *
from pyfbsdk_additions import *
import sys, os, glob, shutil

#make sure framerate is 30fps
FBPlayerControl().SnapMode = FBTransportSnapMode.kFBTransportSnapModeSnapAndPlayOnFrames
FBPlayerControl().SetTransportFps(FBTimeMode.kFBTimeMode30Frames)

lSystem = FBSystem()
lApp = FBApplication()
fileName = lApp.FBXFileName
#get just the current file name
FileNameStart = fileName.rfind('\\')
FileNameOnly = fileName[int(FileNameStart) + 1:]
if FileNameOnly.endswith('.fbx'):
    FileNameOnly = FileNameOnly[:-4]

#get just the current path
Path = fileName[0:int(FileNameStart) + 1]

#get project name
tokenPath = Path.split('\\')
ProjectName = tokenPath[5]

#get rig name and actor initials
token = FileNameOnly.split('_')
#check for underscore in rig name
if len(token) == 4:
    AssetName = token[0] + '_' + token[1]
    ActorInitials = token[2]
    print AssetName
else:
    AssetName = token[0]
    ActorInitials = token[1]
    print AssetName

#set save options        
lApplication = FBApplication()
lOptions = FBFbxOptions(False)
lOptions.SaveSelectedModelsOnly = False
lSystem = FBSystem()
lOriginalTake = lSystem.CurrentTake
#build save file name
NewFileName = lOriginalTake.Name[:-4] + '_' + ActorInitials + '_' + AssetName + '_' + ProjectName + '_WIP_QA'

# Iterate the list of takes.
for lTake in lSystem.Scene.Takes:

    # Switch the current take to the one we want to save.
    lSystem.CurrentTake = lTake
    # Go through the list of takes to export to tag only
    # the correct take. All the other are disregarded.
    for index in range(lOptions.GetTakeCount()): ## take index
        if lOptions.GetTakeName(index) == lTake.Name:
            lOptions.SetTakeSelect(index, True)
        else:
            lOptions.SetTakeSelect(index, False)
    #lApplication.FileSave( outputFile, lOptions )
    lApplication.FileSave( Path + NewFileName, lOptions )


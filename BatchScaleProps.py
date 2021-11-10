#Brian Mckee
#Gearbox Oct 2016
from pyfbsdk import *
from pyfbsdk_additions import *
import sys, os, glob

lApp = FBApplication()
lSystem = FBSystem()

#get path thru message box
result = FBMessageBoxGetUserValue ("Batch scale props","Paste the path of the folder with the props.", str,FBPopupInputType.kFBPopupString, "Enter Path")
path = result[1] + "\\"

scaleValue = FBMessageBoxGetUserValue ("Batch scale props","Enter scale value. (Format .913)", str,FBPopupInputType.kFBPopupString, "Enter scale value")
scaleValue = float(scaleValue[1])

#this gets all fbx files in that folder
fbxList = glob.glob(result[1] + "\\" + "\\*.fbx")
for fbx in fbxList:
    
    lApp.FileOpen(fbx,False)
    lNull = FBModelNull('propScaleNull')
    lNull.SetVector( FBVector3d( scaleValue, scaleValue, scaleValue ), FBModelTransformationType.kModelScaling )
    lNull.Visible = True
    lNull.Show = True
    rootBone = FBFindObjectByFullName('Model::root')
    rootBone.Parent = lNull
    #select rootbone
    rootBone.Selected = True
    #set the plot options.
    myPlotOptions = FBPlotOptions()
    myPlotOptions.PlotAllTakes = True
    myPlotOptions.PlotOnFrame = True
    myPlotOptions.PlotPeriod = FBTime(0,0,0,1)
    myPlotOptions.PlotTranslationOnRootOnly  = False #if set to True, this can cause a big problem - the biped motion gets floaty and bouncy.
    myPlotOptions.PreciseTimeContinuities = False
    myPlotOptions.RotationFilterToApply = FBRotationFilter.kFBRotationFilterUnroll
    myPlotOptions.UseConstantKeyReducer = False
    myPlotOptions.ConstantKeyReducerKeepOneKey = True
    FBPlayerControl().SetTransportFps(FBTimeMode.kFBTimeMode30Frames)
    #plot the selection
    lTake = FBSystem().CurrentTake
    lTake.PlotTakeOnSelected(myPlotOptions)
    lOptions = FBFbxOptions(False)
    lApp.FileSave( fbx, lOptions )
   
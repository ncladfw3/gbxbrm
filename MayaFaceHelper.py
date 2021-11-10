#Gearbox mocap Feb 2015
import maya.cmds as cmds

lMarkers = ['L_LowerMiddleEyelid_CNT_mkr', 'L_LowerInsideEyelid_CNT_mkr', 'L_UpperInsideEyelid_CNT_mkr', 'L_UpperMiddleEyelid_CNT_mkr', 'L_UpperOutsideEyelid_CNT_mkr', 'L_LowerOutsideEyelid_CNT_mkr', 'R_LowerInsideEyelid_CNT_mkr', 'R_LowerMiddleEyelid_CNT_mkr', 'R_LowerOutsideEyelid_CNT_mkr', 'R_UpperOutsideEyelid_CNT_mkr', 'R_UpperMiddleEyelid_CNT_mkr', 'R_UpperInsideEyelid_CNT_mkr', 'R_MouthCorner_CNT_mkr', 'R_UpperLipCorner_CNT_mkr', 'R_UpperLip_CNT_mkr', 'Upperlip_CNT_mkr', 'L_UpperLip_CNT_mkr', 'L_UpperLipCorner_CNT_mkr', 'L_MouthCorner_CNT_mkr', 'L_LowerLipCorner_CNT_mkr', 'L_LowerLip_CNT_mkr', 'LowerLip_CNT_mkr', 'R_LowerLip_CNT_mkr', 'R_LowerLipCorner_CNT_mkr', 'UpperLipFold_CNT_mkr', 'L_Sneer_CNT_mkr', 'L_LowerLabiFold_CNT_mkr', 'L_LowerMouthFold_CNT_mkr', 'LowerLipFold_CNT_mkr', 'R_LowerMouthFold_CNT_mkr', 'R_LowerLabiFold_CNT_mkr', 'R_Sneer_CNT_mkr', 'Nose_CNT_mkr', 'R_NasalFlare_CNT_mkr', 'L_NasalFlare_CNT_mkr', 'R_OuterBrow_CNT_mkr', 'R_Brow_CNT_mkr', 'R_InnerBrow_CNT_mkr', 'L_InnerBrow_CNT_mkr', 'L_Brow_CNT_mkr', 'L_OuterBrow_CNT_mkr','R_CheekBone_CNT_mkr', 'R_Cheek_CNT_mkr', 'R_NasalLabiaFold_CNT_mkr', 'L_NasalLabiaFold_CNT_mkr', 'L_Cheek_CNT_mkr','L_CheekBone_CNT_mkr']
lControls = ['L_LowerMiddleEyelid_CNT', 'L_LowerInsideEyelid_CNT', 'L_UpperInsideEyelid_CNT', 'L_UpperMiddleEyelid_CNT', 'L_UpperOutsideEyelid_CNT', 'L_LowerOutsideEyelid_CNT', 'R_LowerInsideEyelid_CNT', 'R_LowerMiddleEyelid_CNT', 'R_LowerOutsideEyelid_CNT', 'R_UpperOutsideEyelid_CNT', 'R_UpperMiddleEyelid_CNT', 'R_UpperInsideEyelid_CNT', 'R_MouthCorner_CNT', 'R_UpperLipCorner_CNT', 'R_UpperLip_CNT', 'Upperlip_CNT', 'L_UpperLip_CNT', 'L_UpperLipCorner_CNT', 'L_MouthCorner_CNT', 'L_LowerLipCorner_CNT', 'L_LowerLip_CNT', 'LowerLip_CNT', 'R_LowerLip_CNT', 'R_LowerLipCorner_CNT', 'UpperLipFold_CNT', 'L_Sneer_CNT', 'L_LowerLabiFold_CNT', 'L_LowerMouthFold_CNT', 'LowerLipFold_CNT', 'R_LowerMouthFold_CNT', 'R_LowerLabiFold_CNT', 'R_Sneer_CNT', 'Nose_CNT', 'R_NasalFlare_CNT', 'L_NasalFlare_CNT', 'R_OuterBrow_CNT', 'R_Brow_CNT', 'R_InnerBrow_CNT', 'L_InnerBrow_CNT', 'L_Brow_CNT', 'L_OuterBrow_CNT', 'R_CheekBone_CNT', 'R_Cheek_CNT', 'R_NasalLabiaFold_CNT', 'L_NasalLabiaFold_CNT', 'L_Cheek_CNT', 'L_CheekBone_CNT']

def getNameSpace(*args):
    nSpace = cmds.textField(nameSpace,query=True,text=True)
    return nSpace
    
def scaleMarkers(*args):
    for mar in lMarkers:
        try:
            cmds.cutKey( mar, time=(0,500), attribute='scale', option="keys" )
            cmds.scale( .15, .15, .15, mar )
            cmds.setKeyframe(mar)
        except: 
            pass
            print mar + ' missing'
    #piv = cmds.xform ('Nose_CNT', piv=True, q=True, ws=True)
    #cmds.move( piv[0], piv[1], piv[2], 'FaceBaseBoneFBXASC0321', ws=True )
    #cmds.rotate(0, '90deg', 0, 'FaceBaseBoneFBXASC0321' )    
        
def selectBase(*args):
    try:
        cmds.select( 'FaceBaseBone_mkr' )
    except: 
        pass
        print 'FaceBaseBone_mkr' + ' is missing'
        
def aimConst(*args):
    nSpace = cmds.textField(nameSpace,query=True,text=True)
    try:
        cmds.aimConstraint( 'Jaw_CNT_mkr', nSpace + ':Jaw_CNT', mo = True )
    except: 
        pass
        print 'Jaw_CNT_mkr or ' + nSpace + ':Jaw_CNT' + ' is missing'
        
def markerConstraints(*args):
    nSpace = cmds.textField(nameSpace,query=True,text=True)
    i = 0 
    for ctrl in lControls:
        try:
            cmds.parentConstraint( lMarkers[i], nSpace + ':' + ctrl, maintainOffset = True, sr=["x","y","z"] )
        except: 
            pass
            print lMarkers[i] + ' or ' +  nSpace + ':' + ctrl + 'is missing from the scene.'
        i = i + 1     
   
def selectMarkers(*args):
    cmds.select( deselect = True )
    for mar in lMarkers:
        try:
            cmds.select(mar, add = True)
        except: 
            pass
            print mar + ' missing'
                
def selectControls(*args):
    nSpace = cmds.textField(nameSpace,query=True,text=True)
    cmds.select( deselect = True )
    for ctrl in lControls:
        try:
            cmds.select(nSpace + ':' + ctrl, add = True)
        except: 
            pass
            print ctrl + ' missing'
       
cmds.window( title="Maya Face Mocap Helper", width = 275 )
cmds.columnLayout( adjustableColumn=True )
cmds.text( label='***Enter Face Controls NameSpace First***' )
nameSpace = cmds.textField()
cmds.button( label='Scale Down Markers', command=scaleMarkers )
cmds.button( label='Select Face Base Bone', command = selectBase )
cmds.button( label='Set Jaw Aim Constraint', command = aimConst )
cmds.button( label='Create Marker/Controller Constraints', command = markerConstraints )
cmds.button( label='Select Markers', command = selectMarkers )
cmds.button( label='Select Face Controls', command = selectControls )
cmds.showWindow()



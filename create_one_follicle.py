import pymel.core as pm

def create_follicle(oNurbs, uPos=0.0, vPos=0.0):
    # manually place and connect a follicle onto a nurbs surface.
    if oNurbs.type() == 'transform':
        oNurbs = oNurbs.getShape()
    elif oNurbs.type() == 'nurbsSurface':
        pass
    else:
        'Warning: Input must be a nurbs surface.'
        return False

    # create a name with frame padding
    pName = '_'.join((oNurbs.name(),'follicle','#'.zfill(2)))

    oFoll = pm.createNode('follicle', name=pName)
    oNurbs.local.connect(oFoll.inputSurface)
    # if using a polygon mesh, use this line instead.
    # (The polygons will need to have UVs in order to work.)
    #oMesh.outMesh.connect(oFoll.inMesh)

    oNurbs.worldMatrix[0].connect(oFoll.inputWorldMatrix)
    oFoll.outRotate.connect(oFoll.getParent().rotate)
    oFoll.outTranslate.connect(oFoll.getParent().translate)
    oFoll.parameterU.set(uPos)
    oFoll.parameterV.set(vPos)
    oFoll.getParent().t.lock()
    oFoll.getParent().r.lock()

    return oFoll

oFoll = create_follicle(pm.selected()[0], 0.5, 0.5)

myObject = pm.selected()[0]
howManyFollicles =
for i in range(0,howManyFollicles):
    oFoll = create_follicle(myObject, 1, i/(howManyFollicles-1.00))

selection = cmds.ls(sl=True)
for i, jnt in enumerate(selection):
    j = i+355
    par = cmds.ls('nurbsPlane1Deformed2DeformedDeformedDeformed_follicle_0'+str(j))
    cmds.parentConstraint(jnt, par)

selection = cmds.ls(sl=True)
for i, jnt in enumerate(selection):
    j = i+360
    par = cmds.ls('joint'+str(j))
    print par
    print jnt
    cmds.parentConstraint(jnt, par)

for uvVal in uvValues:
    oFoll = create_follicle(myObject, uvVal[0], uvVal[1])
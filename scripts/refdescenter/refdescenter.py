#!/usr/bin/env python

from pcbnew import *
pcb = GetBoard()
moduleCount = 0
for aModule in pcb.GetModules():
	modbb = aModule.GetBoundingBox()
	modrot = aModule.GetOrientation()
	refrot = aModule.Reference().GetDrawRotation()
	aModule.Reference().Rotate(aModule.Reference().GetPosition(),-refrot+modrot)
	aModule.Reference().SetPosition(aModule.GetPosition())
	aModule.Reference().SetHeight(500000)
	aModule.Reference().SetWidth(500000)
	aModule.Reference().SetThickness(125000)
	aModule.Reference().SetVisible(True)
	moduleCount = moduleCount + 1

mc_str = str(moduleCount)
print('RefDesCenter script updated the text of '+mc_str+' Modules.')
print('[Board: '+pcb.GetFileName()+']')

# Usage:
# load board, then open kicad python console, change directory
# to the script direcory or add it to the path
# import refdescenter
# refdescenter

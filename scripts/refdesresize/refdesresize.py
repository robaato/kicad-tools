#!/usr/bin/env python

from pcbnew import *
pcb = GetBoard()
for aModule in pcb.GetModules():
	aModule.Reference().SetHeight(650000)
	aModule.Reference().SetWidth(650000)
	aModule.Reference().SetThickness(95000)
	aModule.Reference().SetVisible(True)

print('[Board: '+pcb.GetFileName()+']')

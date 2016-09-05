#!/usr/bin/env python

from pcbnew import *
pcb = GetBoard()
for aModule in pcb.GetModules():
	aModule.Value().SetVisible(False)

print('[Board: '+pcb.GetFileName()+']')

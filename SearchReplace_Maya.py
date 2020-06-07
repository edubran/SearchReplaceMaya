##script by Eduardo Brandao - eduardo@bosonpost.com.br

import os
import sys
import glob
import pickle
import maya.cmds as cmds

if cmds.window('UI',ex=True):
    cmds.deleteUI('UI')

myWin=cmds.window('UI',title="Search Replace All",sizeable=True, resizeToFitChildren=True)
main=cmds.columnLayout(adjustableColumn=True )

cmds.flowLayout(parent=main)
cmds.text("Folder Path",w=75,h=25)
path=cmds.textField("pathImput",w=300,h=25)
loadBtn=cmds.button(w=50,h=25,label="Path",c="selectDir()")
cmds.separator(h=30,style = "none")

cmds.rowColumnLayout(nc=4,parent=main)
cmds.text(w=75, label = "Search")
cmds.textField("searchImput", w=300,h=25)
cmds.separator(h=10,style = "none")
cmds.separator(h=10, style = "none")

cmds.text(label = "Replace")
cmds.textField("replaceImput", w=300,h=25)
cmds.separator(h=10,style = "none")
cmds.separator(h=10, style = "none")
cmds.separator(h=10, style = "none")

cmds.rowColumnLayout(nc=3,parent=main)
cmds.separator(w=75,h=10, style = "none")
cmds.separator(h=10, style = "none")
cmds.button(w=50, label = "execute", command = "searchReplace()")

cmds.showWindow(myWin)

def selectDir():
    folder=cmds.fileDialog2(cap="Folder Path",fm=3)
    cmds.textField(path, edit=True,text=folder[0])


def searchReplace():

    folder = cmds.textField("pathImput", q = True, text = True)
    find1 = cmds.textField("searchImput", q = True, text = True)
    replace1 = cmds.textField("replaceImput", q = True, text = True)

    f = glob.glob(folder+"/"+"*.ma")

    print (folder)

    for i in f:
        dataOpen = open(i,"rb")
        conteudo = "".join(dataOpen)
        dataOpen.close()

        conteudo = conteudo.replace(find1, replace1)
                            
        dataWrite = open(i, "wt")
        dataWrite.write(conteudo)
        dataWrite.close()

#!/usr/bin/env python3
from pathlib import Path
out_folder = Path("page/")

#var inputs
pageid = input("Füge die ID dieser Seite ein: ") + ".html"
opt1id = input("Füge die ID des linken Button ein: ") + ".html"
opt2id = input("Füge die ID des rechten Button ein: ") + ".html"
pageco = input("Füge den Inhalt des Textfeldes ein: ")
opt1co = input("Füge den Inhalt des linken Button ein: ")
opt2co = input("Füge den Inhalt des rechten Button ein: ")

#import source files
f      = open("sample.html", 'r')
eini   = f.read()
f.close()

#replace text
temp1  =  eini.replace("__CONTENT__", pageco)
temp2  = temp1.replace("__BUTTON1__", opt1co)
temp3  = temp2.replace("__BUTTON2__", opt2co)
temp4  = temp3.replace("__BUTTON1LINK__", opt1id)
output = temp4.replace("__BUTTON2LINK__", opt2id)

#write output
f      = open(out_folder / pageid, 'w')
f.write(output)
f.close()
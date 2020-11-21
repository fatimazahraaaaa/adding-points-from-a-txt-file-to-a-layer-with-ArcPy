from arcpy import *
import os
txt_in=GetParameterAsText(0)
couche_path=GetParameterAsText(1)
separateur=GetParameterAsText(2)
noms_champs=GetParameter(3)
champ_X=GetParameterAsText(4)
champ_Y=GetParameterAsText(5)
champ_Z=GetParameterAsText(6)
SCR=GetParameterAsText(7)
CreateFeatureclass_management (os.path.dirname(couche_path),os.path.basename(couche_path), "POINT", spatial_reference=SCR)
def insererDansCouchefromtxt(couche,txt):
    with open(txt,"r") as f:
        ligne=f.readlines()[1]
        A=Array()
    if noms_champs==0:
        if (ligne.count(separateur))==1:
            with open(txt,"r") as f:
                for ligne1 in f.readlines():
                    X,Y=ligne1.split(separateur)
                    if champ_X=='X' and champ_Y=='Y':
                        A.append(Point(X,Y))
                    if champ_X=='Y' and champ_Y=='X':
                        A.append(Point(Y,X))
                    if champ_X==champ_Y=='X':
                        A.append(Point(X,X))
                    if champ_X==champ_Y=='Y':
                        A.append(Point(Y,Y))
            with da.InsertCursor(couche,["Shape@"])as cursor:
                for pt in A:
                    cursor.insertRow([PointGeometry(pt)])
            AddField_management(couche, "X", "LONG")
            AddField_management(couche, "Y", "LONG")
            with da.UpdateCursor(couche,["X", "Shape@XY", "Y"]) as cursor:
                for row in cursor:
                    row[0]=row[1][0]
                    row[2]=row[1][1]
                    cursor.updateRow(row)
        elif (ligne.count(separateur))==2:
            with open(txt,"r") as f:
                for ligne2 in f.readlines():
                    X,Y,Z=ligne2.split(separateur)
                    if champ_X=='X' and champ_Y=='Y' and champ_Z=='Z':
                        A.append(Point(X,Y,Z))
                    if champ_X=='Y' and champ_Y=='X' and champ_Z=='Z':
                        A.append(Point(Y,X,Z))
                    if champ_X==champ_Y==champ_Z=='X':
                        A.append(Point(X,X,X))
                    if champ_X==champ_Y==champ_Z=='Y':
                        A.append(Point(Y,Y,Y))
                    if champ_X=='X' and champ_Y=='Z' and champ_Z=='Y':
                        A.append(Point(X,Z,Y))
                    if champ_X=='Z' and champ_Y=='Y' and champ_Z=='X':
                        A.append(Point(Z,Y,X))
                    if champ_X=='Z' and champ_Y=='X' and champ_Z=='Y':
                        A.append(Point(Z,X,Y))
                    if champ_X=='Y' and champ_Y=='Z' and champ_Z=='X':
                        A.append(Point(Y,Z,X))
                    if champ_X==champ_Y==champ_Z=='Z':
                        A.append(Point(Z,Z,Z))
                    if champ_X==champ_Y=="X" and champ_Z=='Y':
                        A.append(Point(X,X,Y))
                    if champ_X==champ_Y=="X" and champ_Z=='Z':
                        A.append(Point(X,X,Z))
                    if champ_X==champ_Y=="Y" and champ_Z=='Z':
                        A.append(Point(Y,Y,Z))
                    if champ_X==champ_Y=="Y" and champ_Z=='Z':
                        A.append(Point(Y,Y,Z))
                    if champ_X==champ_Y=="Z" and champ_Z=='X':
                        A.append(Point(Z,Z,X))
                    if champ_X==champ_Y=="Z" and champ_Z=='Y':
                        A.append(Point(Z,Z,Y))
                    if champ_X=='X' and champ_Y==champ_Z=="Z":
                        A.append(Point(X,Z,Z))
                    if champ_X=='X' and champ_Y==champ_Z=="Y":
                        A.append(Point(X,Y,Y))
                    if champ_X=='Y' and champ_Y==champ_Z=="Z":
                        A.append(Point(Y,Z,Z))
                    if champ_X=='Y' and champ_Y==champ_Z=="X":
                        A.append(Point(Y,X,X))
                    if champ_X=='Z' and champ_Y==champ_Z=="X":
                        A.append(Point(Z,X,X))
                    if champ_X=='Z' and champ_Y==champ_Z=="Y":
                        A.append(Point(Z,Y,Y))
                    if champ_Y=='X' and champ_X==champ_Z=="Y":
                        A.append(Point(Y,X,Y))
                    if champ_Y=='X' and champ_X==champ_Z=="Z":
                        A.append(Point(Z,X,Z))
                    if champ_Y=='Y' and champ_X==champ_Z=="X":
                        A.append(Point(X,Y,X))
                    if champ_Y=='Y' and champ_X==champ_Z=="Z":
                        A.append(Point(Z,Y,Z))
                    if champ_Y=='Z' and champ_X==champ_Z=="X":
                        A.append(Point(X,Z,X))
                    if champ_Y=='Z' and champ_X==champ_Z=="Y":
                        A.append(Point(Y,Z,Y))
            AddField_management(couche, "Z", "LONG")
            with da.InsertCursor(couche,["Shape@","Z"])as cursor:
                for pt in A:
                    cursor.insertRow([PointGeometry(pt),pt.Z])
            AddField_management(couche, "X", "LONG")
            AddField_management(couche, "Y", "LONG")
            with da.UpdateCursor(couche,["X", "Shape@XY", "Y"]) as cursor:
                for row in cursor:
                    row[0]=row[1][0]
                    row[2]=row[1][1]                
                    cursor.updateRow(row)
    elif noms_champs==1:
        if (ligne.count(separateur))==1:
            with open(txt,"r") as f:
                B=f.readlines()
                del B[0]
                for ligne1 in B:
                    X,Y=ligne1.split(separateur)
                    if champ_X=='X' and champ_Y=='Y':
                        A.append(Point(X,Y))
                    if champ_X=='Y' and champ_Y=='X':
                        A.append(Point(Y,X))
                    if champ_X==champ_Y=='X':
                        A.append(Point(X,X))
                    if champ_X==champ_Y=='Y':
                        A.append(Point(Y,Y))
            with da.InsertCursor(couche,["Shape@"])as cursor:
                for pt in A:
                    cursor.insertRow([PointGeometry(pt)])
            AddField_management(couche, "X", "LONG")
            AddField_management(couche, "Y", "LONG")
            with da.UpdateCursor(couche,["X", "Shape@XY", "Y"]) as cursor:
                for row in cursor:
                    row[0]=row[1][0]
                    row[2]=row[1][1]
                    cursor.updateRow(row)
        elif (ligne.count(separateur))==2:
            with open(txt,"r") as f:
                B=f.readlines()
                del B[0]
                for ligne2 in B:
                    X,Y,Z=ligne2.split(separateur)
                    if champ_X=='X' and champ_Y=='Y' and champ_Z=='Z':
                        A.append(Point(X,Y,Z))
                    if champ_X=='Y' and champ_Y=='X' and champ_Z=='Z':
                        A.append(Point(Y,X,Z))
                    if champ_X==champ_Y==champ_Z=='X':
                        A.append(Point(X,X,X))
                    if champ_X==champ_Y==champ_Z=='Y':
                        A.append(Point(Y,Y,Y))
                    if champ_X=='X' and champ_Y=='Z' and champ_Z=='Y':
                        A.append(Point(X,Z,Y))
                    if champ_X=='Z' and champ_Y=='Y' and champ_Z=='X':
                        A.append(Point(Z,Y,X))
                    if champ_X=='Z' and champ_Y=='X' and champ_Z=='Y':
                        A.append(Point(Z,X,Y))
                    if champ_X=='Y' and champ_Y=='Z' and champ_Z=='X':
                        A.append(Point(Y,Z,X))
                    if champ_X==champ_Y==champ_Z=='Z':
                        A.append(Point(Z,Z,Z))
                    if champ_X==champ_Y=="X" and champ_Z=='Y':
                        A.append(Point(X,X,Y))
                    if champ_X==champ_Y=="X" and champ_Z=='Z':
                        A.append(Point(X,X,Z))
                    if champ_X==champ_Y=="Y" and champ_Z=='Z':
                        A.append(Point(Y,Y,Z))
                    if champ_X==champ_Y=="Y" and champ_Z=='Z':
                        A.append(Point(Y,Y,Z))
                    if champ_X==champ_Y=="Z" and champ_Z=='X':
                        A.append(Point(Z,Z,X))
                    if champ_X==champ_Y=="Z" and champ_Z=='Y':
                        A.append(Point(Z,Z,Y))
                    if champ_X=='X' and champ_Y==champ_Z=="Z":
                        A.append(Point(X,Z,Z))
                    if champ_X=='X' and champ_Y==champ_Z=="Y":
                        A.append(Point(X,Y,Y))
                    if champ_X=='Y' and champ_Y==champ_Z=="Z":
                        A.append(Point(Y,Z,Z))
                    if champ_X=='Y' and champ_Y==champ_Z=="X":
                        A.append(Point(Y,X,X))
                    if champ_X=='Z' and champ_Y==champ_Z=="X":
                        A.append(Point(Z,X,X))
                    if champ_X=='Z' and champ_Y==champ_Z=="Y":
                        A.append(Point(Z,Y,Y))
                    if champ_Y=='X' and champ_X==champ_Z=="Y":
                        A.append(Point(Y,X,Y))
                    if champ_Y=='X' and champ_X==champ_Z=="Z":
                        A.append(Point(Z,X,Z))
                    if champ_Y=='Y' and champ_X==champ_Z=="X":
                        A.append(Point(X,Y,X))
                    if champ_Y=='Y' and champ_X==champ_Z=="Z":
                        A.append(Point(Z,Y,Z))
                    if champ_Y=='Z' and champ_X==champ_Z=="X":
                        A.append(Point(X,Z,X))
                    if champ_Y=='Z' and champ_X==champ_Z=="Y":
                        A.append(Point(Y,Z,Y))
            AddField_management(couche, "Z", "LONG")
            with da.InsertCursor(couche,["Shape@","Z"])as cursor:
                for pt in A:
                    cursor.insertRow([PointGeometry(pt),pt.Z])
            AddField_management(couche, "X", "LONG")
            AddField_management(couche, "Y", "LONG")
            with da.UpdateCursor(couche,["X", "Shape@XY", "Y"]) as cursor:
                for row in cursor:
                    row[0]=row[1][0]
                    row[2]=row[1][1]                
                    cursor.updateRow(row)                
insererDansCouchefromtxt(couche_path,txt_in)

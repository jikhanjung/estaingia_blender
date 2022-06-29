import bpy
import math
sel_objs = [obj for obj in bpy.context.selected_objects if obj.type == 'MESH']

i=1

f = open("d:/estaingia_rotation.txt", "w")

for obj in sel_objs:
    
    x,y,z = [str(math.degrees(val)%360) for val in obj.rotation_euler]
    print(i,":", x,y,z)
    f.write("\t".join((x,y,z,"\n")))
    i+=1
    
f.close()
    

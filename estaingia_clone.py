import math
import bpy

import mathutils
import random

def duplicate(obj, data=True, actions=True, collection=None):
    obj_copy = obj.copy()
    if data:
        obj_copy.data = obj.data.copy()
#    if actions and obj.animation_data:
#        obj_copy.animation_data.action = obj.animation_data.action.copy()
    collection.objects.link(obj_copy)
    return obj_copy

for i in range(5):
    for j in range(5):
        obj_copy = duplicate(
                obj=bpy.context.active_object,
                data=True,
                actions=True,
                collection=bpy.context.view_layer.active_layer_collection.collection
            )
        x = random.uniform(0,360)
        y = random.uniform(0,360)
        z = random.uniform(0,360)
        obj_copy.rotation_euler[0] = math.radians(x)
        obj_copy.rotation_euler[1] = math.radians(y)
        obj_copy.rotation_euler[2] = math.radians(z)
        obj_copy.location=obj_copy.location + mathutils.Vector((5*(i+1),5*j,0))

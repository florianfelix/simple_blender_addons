bl_info = {
    "name": "Simple Light Power Buttons",
    "author": "florianfelix",
    "version": (0, 1),
    "blender": (3, 0, 0),
    "location": "Properties -> Top of Light Panel",
    "description": "Double / Half Light Power Buttons",
    "warning": "",
    "doc_url": "",
    "category": "Lighting",
}


import bpy
from bpy.types import Operator
from bpy.props import FloatProperty

class OBJECT_OT_double_light_intensity(Operator):
    """Double Light intensity"""
    bl_idname = "object.double_light_intensity"
    bl_label = "Power * 2"
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = "Shift: *= 1.1, ctrl: *= 5"
    
    multiplier : FloatProperty(
        name="multiplier",
        description="multiplier",
        default=2.0)

    @classmethod
    def poll(self, context):
        if context.active_object.type == 'LIGHT':
            return True
        return False

    def execute(self, context):
        context.active_object.data.energy *= self.multiplier
        return {'FINISHED'}
    
    def invoke(self, context, event):
        if event.ctrl:
            self.multiplier = 5
        if event.shift:
            self.multiplier = 1.1
        self.execute(context)
        return {'FINISHED'}

class OBJECT_OT_half_light_intensity(Operator):
    """Half Light intensity"""
    bl_idname = "object.half_light_intensity"
    bl_label = "Power / 2"
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = "Shift: /= 1.1, ctrl: /= 5"

    divider : FloatProperty(
        name="multiplier",
        description="multiplier",
        default=2.0)
        
    @classmethod
    def poll(self, context):
        if context.active_object.type == 'LIGHT':
            return True
        return False

    def execute(self, context):
        context.active_object.data.energy /= self.divider
        return {'FINISHED'}

    def invoke(self, context, event):
        if event.ctrl:
            self.divider = 5
        if event.shift:
            self.divider = 1.1
        self.execute(context)
        return {'FINISHED'}

# Registration
def intensity_buttons(self, context):
    row = self.layout.row()
    row.operator(
        OBJECT_OT_double_light_intensity.bl_idname,
        icon='SORT_DESC')
    row.operator(
        OBJECT_OT_half_light_intensity.bl_idname,
        icon='SORT_ASC')

def register():
    bpy.utils.register_class(OBJECT_OT_double_light_intensity)
    bpy.utils.register_class(OBJECT_OT_half_light_intensity)
    bpy.types.CYCLES_LIGHT_PT_light.prepend(intensity_buttons)
    bpy.types.DATA_PT_EEVEE_light.prepend(intensity_buttons)


def unregister():
    bpy.utils.unregister_class(OBJECT_OT_double_light_intensity)
    bpy.utils.unregister_class(OBJECT_OT_half_light_intensity)
    bpy.types.CYCLES_LIGHT_PT_light.remove(intensity_buttons)
    bpy.types.DATA_PT_EEVEE_light.remove(intensity_buttons)

if __name__ == "__main__":
    register()

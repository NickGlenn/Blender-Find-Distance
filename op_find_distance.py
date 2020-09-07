from bpy.types import Operator, Context
from bpy.props import EnumProperty
from mathutils import Matrix


class FindDistance:

    def get_distance(self, context: Context, a: Matrix, b: Matrix):
        a_loc, a_rot, _ = a.decompose()
        b_loc, b_rot, _ = b.decompose()

        offset = (b_loc - a_loc)

        result = "LOCATION ({}, {}, {})".format(offset[0], offset[1], offset[2])

        result += "    ROTATION ({}, {}, {})".format()

        self.report({"INFO"}, result)
        context.window_manager.clipboard = result


class FindDistanceFromCursor(Operator, FindDistance):
    bl_idname = "view3d.find_distance_from_cursor"
    bl_label = "Find Distance from Cursor"
    bl_description = "Finds the distance between the active object and the 3D cursor and copies the result to the clipboard"

    @classmethod
    def poll(cls, context):
        return (
                (context.mode == "OBJECT" and context.active_object is not None) or
                (context.mode == "EDIT_ARMATURE" and len(context.selected_bones) == 1) or
                (context.mode == "POSE" and len(context.selected_pose_bones) == 1)
        )

    def execute(self, context):

        obj = context.active_object
        cursor = context.scene.cursor

        self.get_distance(context, cursor.matrix, obj.matrix_world)

        return {"FINISHED"}

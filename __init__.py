import bpy
from bpy.types import UILayout

from .op_find_distance import FindDistanceFromCursor

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name": "Find Distance",
    "author": "Nick Glenn",
    "description": "Small utility for finding the location or rotation offset between two transforms",
    "version": (2020, 1, 0),
    "blender": (2, 80, 0),
    "url": "https://github.com/nickglenn/blender-find-distance",
    "location": "View3D",
    "support": "COMMUNITY",
    "warning": "",
    "category": "Generic"
}

classes = (
    FindDistanceFromCursor,
)

def register():
    for c in classes:
        bpy.utils.register_class(c)

def unregister():
    for c in classes[::-1]:
        bpy.utils.unregister_class(c)

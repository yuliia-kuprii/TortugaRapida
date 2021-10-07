"""
Loads all the fx !
Usage:
import moviepy.video.fx.all as vfx
clip = vfx.resize(some_clip, width=400)
clip = vfx.mirror_x(some_clip)
"""

import pkgutil
import moviepy.video.fx as fx
from moviepy.video.fx.crop import crop
from moviepy.video.fx.fadein import fadein
from moviepy.video.fx.fadeout import fadeout
from moviepy.video.fx.resize import resize
from moviepy.video.fx.invert_colors import invert_colors
from moviepy.video.fx.loop import loop
from moviepy.video.fx.margin import margin
from moviepy.video.fx.mask_and import mask_and
from moviepy.video.fx.mask_or import mask_or
from moviepy.video.fx.rotate import rotate
from moviepy.video.fx.speedx import speedx
# __all__ = [name for _, name, _ in pkgutil.iter_modules(
#     fx.__path__) if name != "all"]
#
# for name in __all__:
#     exec("from ..%s import %s" % (name, name))
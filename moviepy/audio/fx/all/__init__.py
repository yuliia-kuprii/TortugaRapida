"""
Loads all the fx !
Usage:
import moviepy.audio.fx.all as afx
audio_clip = afx.volume_x(some_clip, .5)
"""

import pkgutil
import moviepy.audio.fx as fx
from moviepy.audio.fx.audio_fadein import audio_fadein
from moviepy.audio.fx.audio_fadeout import audio_fadeout
from moviepy.audio.fx.audio_left_right import audio_left_right
from moviepy.audio.fx.audio_loop import audio_loop
from moviepy.audio.fx.audio_normalize import audio_normalize
from moviepy.audio.fx.volumex import volumex
# __all__ = [name for _, name, _ in pkgutil.iter_modules(
#     fx.__path__) if name != "all"]
# 
# for name in __all__:
#     exec("from ..%s import %s" % (name, name))
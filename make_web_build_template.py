import os
from update_emsdk import update_emsdk

update_emsdk()

os.system('\
    .\emsdk\emsdk_env.bat && scons platform=web \
    target="template_release" \
    profile=../custom.py \
    -C godot')
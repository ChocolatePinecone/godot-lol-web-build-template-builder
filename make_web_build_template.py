import os
import certifi

cert_location = certifi.where()
os.environ['SSL_CERT_FILE'] = cert_location
os.system('.\emsdk\emsdk.bat install latest')
os.system('.\emsdk\emsdk.bat activate latest')

os.system('\
    .\emsdk\emsdk_env.bat && scons platform=web \
    target="template_release" \
    profile=../custom.py \
    -C godot')
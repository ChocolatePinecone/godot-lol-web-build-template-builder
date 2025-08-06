import os
import certifi

def update_emsdk():
    cert_location = certifi.where()
    os.environ['SSL_CERT_FILE'] = cert_location
    os.system('.\emsdk\emsdk.bat install latest')
    os.system('.\emsdk\emsdk.bat activate latest')
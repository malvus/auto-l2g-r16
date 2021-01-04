import time
import os
from .log import log

class FixTif():
    
    def __init__(self, logger):
        self.logger = logger
    
    @log
    def do(self, file_in, file_out):
        name = 'fix_tif'
        try:
            cmd = 'gdal_fillnodata.py "'+file_in+'" "'+file_out+'"'
            out = os.system(cmd)
            return name, cmd, out
        except Exception as err:
            print(err) 

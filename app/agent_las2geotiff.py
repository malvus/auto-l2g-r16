import os
import time
import traceback
from datetime import datetime as dt
from .agent_logger import AgentLogger
from .pipe_gen import PipeGen
from .pipe_cmd import PipeCmd
from .util import Util
from .before import Before
from .fix_tif import FixTif


class AgentLas2Geotiff():
    
    def __init__(self):
        self.dir = '.'
        self.spc = '    '
        self.file_pipe_merge_project = 'pipe_merge_proj.json'
        self.file_pipe_convert = 'pipe_convert.json'
        self.file_las = 'output.las'
        self.file_tif = 'output.tif'
        self.resolution = '1.0'
        mydt = dt.now()
        self.id = mydt.strftime('%y%m%d_%H%M%S')
        self.logger = AgentLogger(self.id)
        self.pipe_gen = PipeGen()
        self.util = Util()
        self.pipe_cmd = PipeCmd(self.logger)
        #self.proj = 'EPSG:4326'
        self.proj = 'EPSG:32647'
        self.path_las = ''
    
    
    def merge_project_las(self, path):
        name = 'merge_project_las'
        try:
            if os.path.exists(path):
                self.path_las = path
                size = '~'+str(round(self.util.get_total_size(path),2))+'Gb'
                filename = os.path.join(self.dir,self.file_las)
                pipe = self.pipe_gen.get_merge_project(path, filename)
                file_pipe = os.path.join(self.dir,self.file_pipe_merge_project)
                self.pipe_cmd.save(pipe, file_pipe)
                name, cmd, out = self.pipe_cmd.run(file_pipe, name, {'size':size})
                return out
            else:
                raise Exception('dir not found : '+path)
        except:
            self.logger.log(traceback.format_exc()) 
            
            
    def convert_las_to_geotiff(self):
        name = 'convert_las_to_geotiff'
        try:
            file_las = os.path.join(self.dir,self.file_las)
            file_tif = os.path.join(self.dir,self.file_tif)
            pipe = self.pipe_gen.get_convert(file_las, file_tif, self.resolution)
            file_pipe = os.path.join(self.dir,self.file_pipe_convert)
            self.pipe_cmd.save(pipe, file_pipe)            
            name, cmd, out = self.pipe_cmd.run(file_pipe, name, {})
            return out
        except:
            self.logger.log(traceback.format_exc()) 
            

    def get_before(self, cont):
        b4 = []
        try:
            before = Before(self.logger)
            b4 = before.get_before(cont)
        except:
            self.logger.log(traceback.format_exc()) 
        return b4

 
    def clean_up(self):
        try:
            filename = os.path.join(self.dir, self.file_pipe_merge_project)
            if os.path.exists(filename):
                os.remove(filename) 
            filename = os.path.join(self.dir, self.file_pipe_convert)
            if os.path.exists(filename):
                os.remove(filename) 
            filename = os.path.join(self.dir, self.file_las)
            if os.path.exists(filename):
                os.remove(filename) 
            filename = os.path.join(self.dir, self.file_tif)
            if os.path.exists(filename):
                os.remove(filename) 	
        except:
            self.logger.log(traceback.format_exc()) 
            
         
    def do(self, path, cont=''):
        try:
            mydirs = self.util.get_las_dirs(path)
            b4 = []
            if len(cont)>0:
                b4 = self.get_before(cont)
            fix_tif = FixTif(self.logger)
            for mydir in mydirs:
                if mydir not in b4:
                    outs = []
                    self.path_las = mydir
                    self.dir = os.path.dirname(mydir)
                    self.logger.log_dir(self.path_las)
                    out = self.merge_project_las(mydir)
                    outs.append(out)
                    out = self.convert_las_to_geotiff()
                    outs.append(out)
                    file_tif = os.path.join(self.dir,self.file_tif)
                    idx = file_tif.rfind('.')
                    file_tif_fixed = file_tif[:idx]+'_fixed.tif'
                    name, cmd, out = fix_tif.do(file_tif, file_tif_fixed)
                    outs.append(out)
                    self.logger.log_overall(outs, mydir)
                    self.clean_up()
                    print('testing .. break')
                    break
                else:
                    self.logger.log(mydir+' (is in b4. skipping ...)')
                self.logger.log('')
        except:
            self.logger.log(traceback.format_exc()) 


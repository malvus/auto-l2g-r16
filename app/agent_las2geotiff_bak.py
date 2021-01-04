import os
import time
import subprocess as spc
from .agent_logger import AgentLogger
from .pipe_gen import PipeGen
from .pipe_cmd import PipeCmd
from .util import Util

class AgentLas2Geotiff():
    
    def __init__(self):
        self.path_las = 'dat-dsm-las'
        self.dir = '.'
        self.spc = '    '
        self.file_pipe_merge = 'pipe_merge.json'
        self.file_pipe_convert = 'pipe_convert.json'
        self.file_las = 'output.las'
        self.file_tif = 'output.tif'
        self.resolution = '1.0'
        self.logger = AgentLogger()
        self.pipe_gen = PipeGen()
        self.util = Util()
        self.pipe_cmd = PipeCmd(self.logger)
    
    '''
    def walk(self, top, maxdepth):
        dirs, nondirs = [], []
        for name in os.listdir(top):
            (dirs if os.path.isdir(os.path.join(top, name)) else nondirs).append(name)
        yield top, dirs, nondirs
        if maxdepth > 1:
            for name in dirs:
                for x in self.walk(os.path.join(top, name), maxdepth-1):
                    yield x
                
                
    def get_las_dirs(self, path):
        mydirs = []
        for x in self.walk(path, 10):
            files = x[2]
            if len(files) > 0:
                #print('files=',x[2])
                for myfile in files:
                    if myfile.endswith('.las') and myfile != 'output.las' :
                        #print('myfile =', myfile)
                        mydir = x[0]
                        #print('mydir =', mydir)
                        #print('')
                        if mydir not in mydirs:
                            mydirs.append(mydir)
        return mydirs
    
    
    def get_total_size(self, path):
        total = 0
        for myfile in os.listdir(path):
            #print('path',path,'  myfile =', myfile,' size =',os.path.getsize(myfile))
            total += os.path.getsize(os.path.join(path,myfile))
        return total/1073741824
    '''
        
    def merge_las(self, path):
        try:
            if os.path.exists(path):
                self.path_las = path
                size = self.util.get_total_size(path)
                print('size = ~'+str(round(size,2))+'Gb\n')
                self.logger.log('size = ~'+str(round(size,2))+'Gb\n')
                filename = os.path.join(self.dir,self.file_las)
                pipe = self.pipe_gen.get_merge(path, filename)
                file_pipe = os.path.join(self.dir,self.file_pipe_merge)
                self.pipe_cmd.save(pipe, file_pipe)
                self.pipe_cmd.run(file_pipe)
            else:
                raise Exception('dir not found : '+path)
        except Exception as err:
            print('err :',err)
            self.logger.log('err :',err)
        else:
            print('ok\n')
            self.logger.log('ok\n')
    
    
    def convert_las_to_geotiff(self):
        print('convert_las_to_geotiff')
        try:
            file_las = os.path.join(self.dir,self.file_las)
            file_tif = os.path.join(self.dir,self.file_tif)
            pipe = self.pipe_gen.get_convert(file_las, file_tif, self.resolution)
            file_pipe = os.path.join(self.dir,self.file_pipe_convert)
            self.pipe_cmd.save(pipe, file_pipe)            
            self.pipe_cmd.run(file_pipe)
        except Exception as err:
            print('err :', err)
            self.logger.log('err :',err)
        else:
            print('ok')
            self.logger.log('ok\n')
    
    '''
    def save_pipe(self, pipe, filename):
        try:
            with open(filename,'w') as fw:
                for p in pipe:
                    fw.write(p+'\n')
        except Exception as err:
            print(err)
            self.logger.log('err :',err)
    '''
            
    '''
    def gen_pipe_merge(self, path):
        self.path_las = path
        spc = self.spc
        pipe = []
        pipe.append('{')
        pipe.append(spc+'"pipeline" : [')
        for myfile in sorted(os.listdir(path)):
            pipe.append(spc+spc+'"'+os.path.join(path, myfile)+'",')
        pipe.append(spc+spc+'{')
        pipe.append(spc+spc+spc+'"type" : "filters.merge"')
        pipe.append(spc+spc+'},')
        pipe.append(spc+spc+'"'+os.path.join(self.dir,self.file_las)+'"')
        pipe.append(spc+']')
        pipe.append('}')
        return pipe
    
    
    def gen_pipe_convert(self):
        spc = self.spc
        pipe = []
        pipe.append('{')
        pipe.append(spc+'"pipeline" : [')
        pipe.append(spc+spc+'"'+os.path.join(self.dir,self.file_las)+'",')
        pipe.append(spc+spc+'{')
        pipe.append(spc+spc+spc+'"type" : "writers.gdal",')
        pipe.append(spc+spc+spc+'"filename" : "'+os.path.join(self.dir,self.file_tif)+'",')
        pipe.append(spc+spc+spc+'"resolution" : "'+str(self.resolution)+'",')
        pipe.append(spc+spc+spc+'"output_type" : "max"')
        pipe.append(spc+spc+'}')
        pipe.append(spc+']')
        pipe.append('}')
        return pipe
    '''
    ''' 
    def run_pipe(self, filename):
        try:
            cmd = 'pdal pipeline --stream "'+filename+'"'
            print('run pipe')
            print(cmd)
            self.logger.log('run pipe')
            self.logger.log(cmd)
            start = time.time()
            out = os.system(cmd)
            duration = time.time() - start
            print('\nduration = '+str(round(duration))+'s')
            print('')
            self.logger.log('duration = '+str(round(duration))+'s')
            self.logger.log('')
            #out = spc.call([cmd])
            if out:
                print(out)
                self.logger.log(out)
        except Exception as err:
            print(err)
            self.logger.log(err)
    
          
    def print_pipe(self, pipe):
        for p in pipe:
            print(p)
    '''
    
    def do(self, path):
        mydirs = self.util.get_las_dirs(path)
        for mydir in mydirs:
            self.path_las = mydir
            self.dir = os.path.dirname(mydir)
            #print(self.dir)
            print(self.path_las)
            print('')
            self.logger.log(self.path_las)
            self.logger.log('')
            
            self.merge_las(mydir)
            self.convert_las_to_geotiff()
            print('______________________________\n')
            self.logger.log('______________________________\n')




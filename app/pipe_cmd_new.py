import os
import time
from .agent_logger import AgentLogger

class PipeCmd():

    def __init__(self, logger):
        self.logger = logger
    
    
    def save(self, pipe, filename):
        try:
            with open(filename,'w') as fw:
                for p in pipe:
                    fw.write(p+'\n')
        except Exception as err:
            self.logger.log('err :',err)
    
            
    def run_base(self, cmd):
        try:
            self.logger.log('run pipe'.upper())
            self.logger.log(cmd)
            self.logger.log('')
            start = time.time()
            out = os.system(cmd)
            duration = time.time() - start
            self.logger.log('duration = '+str(round(duration))+'s')
            self.logger.log('')
            if out:
                self.logger.log(out)
            return out, duration
        except Exception as err:
            self.logger.log(err)

    
    def run(self, filename):
         cmd = 'pdal pipeline --stream "'+filename+'"'
         return self.run_base(cmd)

  
    def run_no_stream(self, filename):
         cmd = 'pdal pipeline "'+filename+'"'
         return self.run_base(cmd)
       
            
    def print(self, pipe):
        for p in pipe:
            print(p)

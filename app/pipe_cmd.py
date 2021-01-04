import os
import time
from .agent_logger import AgentLogger
from .log import log

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


    @log
    def run(self, filename, name, mydict):
        try:
            cmd = 'pdal pipeline --stream "'+filename+'"'
            out = os.system(cmd)
            return name, cmd, out
        except Exception as err:
            self.logger.log(err)
    
    
    def print(self, pipe):
        for p in pipe:
            print(p)

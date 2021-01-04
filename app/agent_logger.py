import os
import logging as lgg
from datetime import datetime as dt

class AgentLogger():

    def __init__(self, myid='', dir_root='log'):
        mydt = dt.now()
        if  len(myid) == 0:
            self.id = mydt.strftime('%y%m%d_%H%M%S')
        else:
            self.id = myid	
        self.dir_root = dir_root
        self.dir = self.create_dir(self.id)
        self.loggers = dict()
        self.create_loggers()
        
        self.log('')
        self.log(self.id)
        self.log('')
        self.log('LOG')
        if os.path.exists(self.dir):
            self.log(self.dir+' true')
        else:
            self.log(self.dir+' false')
        self.log('')
    
    def create_loggers(self):
        name = 'base'
        fmt_str = '%(message)s'
        self.loggers[name] = self.create_logger(name, fmt_str)
        name = 'sum'
        fmt_str = '%(message)s'
        self.loggers[name] = self.create_logger(name, fmt_str)
    
        
    def create_logger(self, name, fmt_str):
        lgr = lgg.getLogger(self.id+'_'+name)
        lgr.setLevel(lgg.INFO)
        myfile = os.path.join(self.dir, name+'.log')
        hnd = lgg.FileHandler(myfile)
        fmt = lgg.Formatter(fmt_str)
        hnd.setFormatter(fmt)
        lgr.addHandler(hnd)
        
        if name == 'base':
            hnd = lgg.StreamHandler()
            fmt = lgg.Formatter('%(message)s')
            hnd.setFormatter(fmt)
            lgr.addHandler(hnd)
        
        return lgr
    
       
    def create_dir(self, myid):
        mydir = self.dir_root+'/'+myid
        if not os.path.exists(mydir):
            os.makedirs(mydir)
        return mydir
        

    def log(self, msg='', name='base'):
        if name in self.loggers.keys():
            self.loggers[name].info(msg)
     
    def log_dir(self, mydir):
        self.log('DIR')
        self.log(mydir)
        self.log('')
    
    
    def all_zeroes(self, outs):
        result = True
        for out in outs:
            if out != 0:
                result = False
                break
        return result	
   
            
    def log_overall(self, outs, mydir):
        self.log(outs)
        self.log('overall = ok') if self.all_zeroes(outs) else self.log('overall = err') 
        self.log(mydir+', ok', 'sum') if self.all_zeroes(outs) else self.log(mydir+', err', 'sum') 
        self.log('______________________________')
        self.log('')
                         

        

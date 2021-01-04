import os
import sys
import traceback

class Before():

    def __init__(self, logger):
        self.logger = logger
        self.dirs = []
        try:
            mydirs = sorted(os.listdir('log'))
            if mydirs:
                self.dirs.extend(mydirs)
        except:
            self.logger.log(traceback.format_exc())
    
    def get_before(self, cont):
        try:
            self.logger.log('BEFORE')
            self.logger.log('')
            self.logger.log('type = '+str(type(cont)))
            if type(cont) is str:
                if cont == 'before':
                    b4 = self.get_before_by_prev_dir()
                elif cont == 'before_all':
                    b4 = self.get_before_by_prev_dir_all()
                elif cont[0].isdigit():
                    b4 = self.get_before_by_date(cont)
            elif type(cont) is list:
                b4 = self.get_before_by_dates(cont)
                
            #self.logger.log('')
        except Exception as err:
            self.logger.log(err)
            
        self.logger.log('b4')
        if len(b4)>0:
            for b in b4:
                self.logger.log(b)
        else:
            self.logger.log('empty')
        self.logger.log('')
        
        return b4
        
    def get_before_by_prev_dir_all(self):
        self.logger.log('get_before_by_prev_dir_all')
        try:
            b4s = []
            self.logger.log('len(self.dirs) = '+str(len(self.dirs)))
            if len(self.dirs) > 1:
                mydirs = self.dirs[:-1]
                for mydir in mydirs:
                    b4 = self.get_before_by_date(mydir)
                    b4s.extend(b4)
            b4s = list(dict.fromkeys(b4s))
            return b4s
        except:
            self.logger.log(traceback.format_exc()) 
 

    def get_before_by_prev_dir(self):
        self.logger.log('get_before_by_prev_dir')
        try:
            b4 = []
            self.logger.log('len(self.dirs) = '+str(len(self.dirs)))
            if len(self.dirs) > 1:
                
                mydir = self.dirs[-2]
                self.logger.log(mydir)
                b4 = self.get_before_by_date(mydir)
            return b4
        except:
            self.logger.log(traceback.format_exc()) 
                
        
    def get_before_by_dates(self, mydates):
        self.logger.log('get_before_by_dates')
        b4s = []
        try:
            for mydate in mydates:
                b4 = self.get_before_by_date(mydate)
                b4s.extend(b4)
            b4s = list(dict.fromkeys(b4s))
            return b4s
        except:
            self.logger.log(traceback.format_exc())
            
            
    def get_before_by_date(self, mydate):
        self.logger.log('get_before_by_date')
        b4 = []
        try:
            filename = os.path.join('log',mydate, 'sum.log')
            self.logger.log('filename = '+filename)
            if os.path.exists(filename):
                self.logger.log('filename = '+filename+' exists')
                self.logger.log('')
                with open(filename) as f:
                    lines = f.readlines()
                    for line in lines:
                        #print(line)
                        items = line.split(',')
                        if items[1].strip() == 'ok':
                            b4.append(items[0])
            return b4
        except:
            self.logger.log(traceback.format_exc())
        

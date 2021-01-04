import os

class Util():

    def __init__(self):
        self.exclude = ['output.las', 'output_merge.las']
    
    
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
                    if myfile.endswith('.las') and myfile not in self.exclude:
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
        

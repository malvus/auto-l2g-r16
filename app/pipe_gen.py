import os

class PipeGen():
    
    def __init__(self):
        self.spc = '    '
        
    def get_merge(self, path, filename):
        spc = self.spc
        pipe = []
        try:
            pipe.append('{')
            pipe.append(spc+'"pipeline" : [')
            for myfile in sorted(os.listdir(path)):
                pipe.append(spc+spc+'"'+os.path.join(path, myfile)+'",')
            pipe.append(spc+spc+'{')
            pipe.append(spc+spc+spc+'"type" : "filters.merge"')
            pipe.append(spc+spc+'},')
            pipe.append(spc+spc+'"'+filename+'"')
            pipe.append(spc+']')
            pipe.append('}')
        except Exception as err:
            print(__name__+' : err : '+str(err))
            pipe = []
            raise Exception(__name__+' : err : empty pipe')
        return pipe
    
    
    def get_convert(self, file_las, file_tif, resolution=1.0):
        spc = self.spc
        pipe = []
        try:
            pipe.append('{')
            pipe.append(spc+'"pipeline" : [')
            pipe.append(spc+spc+'"'+file_las+'",')
            pipe.append(spc+spc+'{')
            pipe.append(spc+spc+spc+'"type" : "writers.gdal",')
            pipe.append(spc+spc+spc+'"filename" : "'+file_tif+'",')
            pipe.append(spc+spc+spc+'"resolution" : "'+str(resolution)+'",')
            pipe.append(spc+spc+spc+'"output_type" : "max"')
            pipe.append(spc+spc+'}')
            pipe.append(spc+']')
            pipe.append('}')
        except Exception as err:
            print(__name__+' : err : '+str(err))
            pipe = []
            raise Exception(__name__+' : err : empty pipe')
        return pipe
        
        
    def get_project(self, proj, file_in, file_out):
        spc = self.spc
        pipe = []
        try:
            pipe.append('{')
            pipe.append(spc+'"pipeline" : [')
            pipe.append(spc+spc+'{')
            pipe.append(spc+spc+spc+'"type" : "readers.las",')
            pipe.append(spc+spc+spc+'"filename" : "'+file_in+'"')
            pipe.append(spc+spc+'},')
            pipe.append(spc+spc+'{')
            pipe.append(spc+spc+spc+'"type" : "writers.las",')
            pipe.append(spc+spc+spc+'"a_srs" : "'+proj+'",')
            pipe.append(spc+spc+spc+'"filename" : "'+file_out+'"')
            pipe.append(spc+spc+'}')
            pipe.append(spc+']')
            pipe.append('}')
        except Exception as err:
            print(__name__+' : err : '+str(err))
            pipe = []
            raise Exception(__name__+' : err : empty pipe')
        return pipe


    def get_merge_project(self, path, filename, proj='EPSG:32647'):
        spc = self.spc
        pipe = []
        try:
            pipe.append('{')
            pipe.append(spc+'"pipeline" : [')
            for myfile in sorted(os.listdir(path)):
                pipe.append(spc+spc+'"'+os.path.join(path, myfile)+'",')
            pipe.append(spc+spc+'{')
            pipe.append(spc+spc+spc+'"type" : "filters.merge"')
            pipe.append(spc+spc+'},')
            pipe.append(spc+spc+'{')
            pipe.append(spc+spc+spc+'"type" : "writers.las",')
            pipe.append(spc+spc+spc+'"a_srs" : "'+proj+'",')
            pipe.append(spc+spc+spc+'"filename" : "'+filename+'"')
            pipe.append(spc+spc+'}')
            pipe.append(spc+']')
            pipe.append('}')
        except Exception as err:
            print(__name__+' : err : '+str(err))
            pipe = []
            raise Exception(__name__+' : err : empty pipe')
        return pipe


    def get_tri_convert(self, file_in, file_out, resolution=1):
        spc = self.spc
        pipe = []
        try:
            pipe.append('{')
            pipe.append(spc+'"pipeline" : [')
            pipe.append(spc+spc+'"'+file_in+'",')
            pipe.append(spc+spc+'{')
            pipe.append(spc+spc+spc+'"type" : "filters.delaunay"')
            pipe.append(spc+spc+'},')
            pipe.append(spc+spc+'{')
            pipe.append(spc+spc+spc+'"type" : "filters.faceraster",')
            pipe.append(spc+spc+spc+'"resolution" : '+resolution)
            pipe.append(spc+spc+'},')
            pipe.append(spc+spc+'{')
            pipe.append(spc+spc+spc+'"type" : "writers.raster",')
            pipe.append(spc+spc+spc+'"filename" : "'+file_out+'"')
            pipe.append(spc+spc+'}')
            pipe.append(spc+']')
            pipe.append('}')
        except Exception as err:
            print(__name__+' : err : '+str(err))
            pipe = []
            raise Exception(__name__+' : err : empty pipe')
        return pipe

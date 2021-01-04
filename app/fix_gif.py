


class FixGif():

    def __init__(self):
        pass

    def do(self, file_in, file_out):
        out = os.system('gdal_fillnodata '+file_in+' '+file_out)
        print(out)

import sys
import os
from app.agent_las2geotiff import AgentLas2Geotiff

agt = AgentLas2Geotiff()
path = '/home/mac/my/prj_new/auto/las2geotiff/dat_test'
agt.do(path)
#agt.do(path,'before')
#agt.do(path,'before_all')
#agt.do(path,'201230_084912')
#agt.do(path, ['201230_114328','201230_115857'])

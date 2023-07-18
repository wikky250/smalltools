import geomeas as gm
import numpy as np

Oab = np.array([-533.4, 256, 43.8])
Pxb = np.array([-19.59820338, 139.58818292, 45.55380309])
Pyb = np.array([-38.23270656, 157.3130709, 59.86810327])

print(gm.Pose().calPoseFrom3Points(Oab, Pxb, Pyb))
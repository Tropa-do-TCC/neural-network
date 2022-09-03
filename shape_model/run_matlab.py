from oct2py import Oct2Py
from scipy.io import savemat


oc = Oct2Py()

script = ""

with open("shape_model/CreateShapeModel.m") as script_file:
    script = script_file.read()
with open("shape_model/myScript.m", "w+") as f:
    f.write(script)

oc.myScript(7)


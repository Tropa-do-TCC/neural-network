from oct2py import Oct2Py
<<<<<<< HEAD
=======
from scipy.io import savemat
>>>>>>> cdb79294ffe076500f17eb0046fcf639bdeeb3c7

oc = Oct2Py()

script = ""

with open("CreateShapeModelCopy.m") as script_file:
    script = script_file.read()
with open("myScript.m", "w+") as f:
    f.write(script)

<<<<<<< HEAD
oc.myScript(7)
=======
savemat("shape_model/ShapeModelTesteCt9landmarks.mat", oc.myScript(7))
>>>>>>> cdb79294ffe076500f17eb0046fcf639bdeeb3c7

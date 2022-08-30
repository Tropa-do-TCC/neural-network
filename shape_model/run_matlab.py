from oct2py import Oct2Py

oc = Oct2Py()

script = ""

with open("CreateShapeModelCopy.m") as script_file:
    script = script_file.read()
with open("myScript.m", "w+") as f:
    f.write(script)

oc.myScript(7)

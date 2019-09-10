#JEmPy - Java Embedder for Python

import os
import subprocess

def create_function(params, returnType, code, imports=[]):
    if "embedded" not in os.listdir("."):
        os.makedirs("embedded")
    folders = os.listdir("embedded")
    emCount = len(folders)
    fullCode = """{imports}

public class Program {{
    public static void main(String[] args){{
        if (args.length != {argCount}) {{
            System.err.println("Expected {argCount} arguments; got "+args.length);
            System.exit(1);
        }} else {{
{enumerateArgs}
            {code}
        }}
    }}
}}"""
    importString = "\n".join(["import {};".format(i) for i in imports])
    casters = {"String": "{val}",
               "float": "Float.parseFloat({val})",
               "int": "Integer.parseInt({val})",
               "boolean": "Boolean.parseBoolean({val})",
               "char": "{val}.charAt(0)"}
    
    enumerateArgs = ""
    for i, arg in enumerate(params):
        caster = casters[arg[0]].format(val="args[{i}]".format(i=i))
        enumerateArgs += "            {type} {arg} = {caster};\n".format(type=arg[0],
                                                                         arg=arg[1],
                                                                         caster=caster)
    code = code.replace("\n", "\n            ")
    fullCode = fullCode.format(imports=importString,
                               argCount=len(params),
                               enumerateArgs=enumerateArgs,
                               code=code)
    path = "embedded\\{i}\\".format(i=emCount)
    for i in folders:
        with open("embedded\\{i}\\Program.java".format(i=i)) as em:
            if em.read() == fullCode:
                path = "embedded\\{i}\\".format(i=i)
                break
    else:
        os.makedirs("embedded\\{i}".format(i=emCount))
        with open("{path}Program.java".format(path=path), "w") as src:
            src.write(fullCode)
        os.system("javac {path}Program.java".format(path=path))
    args = ", ".join(i[1] for i in params)
    argString = " {}" * len(params)
    cmdString = """lambda {args}: {ret}(subprocess.check_output("java -classpath {path} Program{argString}".format({args}), shell=True))""".format(path=os.path.abspath(path).replace("\\", "\\\\"),
                                                                                                                                                   args=args,
                                                                                                                                                   argString=argString,
                                                                                                                                                   ret=returnType.__name__)
    pythonFunc = eval(cmdString)
    return pythonFunc

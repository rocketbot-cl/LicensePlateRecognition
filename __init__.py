# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""

import os
import sys

base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'LicensePlateRecognition' + os.sep + 'libs' + os.sep
if cur_path not in sys.path:
    sys.path.append(cur_path)

from licensePlateRecognitionObj import LicensePlateRecognitionObj

global licensePlateRecognition_I

module = GetParams("module")

try:

    if (module == "recognizeLicensePlate"):

        secretKey = GetParams("secretKey")
        pathToLicense = GetParams("pathToLicense")
        country = GetParams("country")
        
        licensePlateRecognition_I = LicensePlateRecognitionObj(secretKey)

        resultRecognition = licensePlateRecognition_I.recognizeLicensePlate(pathToLicense, country)

        whereToStore = GetParams("whereToStore")
        SetVar(whereToStore, resultRecognition)

except Exception as e:
    print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
    PrintException()
    raise e
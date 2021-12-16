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
from plateRecognitionObj import PlateRecognitionObj

global plateRecognition_I
global licensePlateRecognition_I

module = GetParams("module")

try:

    if (module == "connectToCarCheck"):

        secretKey = GetParams("secretKey")

        resultConnection = False
        
        licensePlateRecognition_I = LicensePlateRecognitionObj(secretKey)
        
        if licensePlateRecognition_I.secretKey:
            resultConnection = True
    
        whereToStore = GetParams("whereToStore")
        SetVar(whereToStore, resultConnection)

    if (module == "recognizeLicensePlate"):

        pathToLicense = GetParams("pathToLicense")
        country = GetParams("country")

        resultRecognition = licensePlateRecognition_I.licensePlateData(pathToLicense, country)

        whereToStore = GetParams("whereToStore")
        SetVar(whereToStore, resultRecognition)

    if (module == "sendLicensePlate"):
        
        apiToken = GetParams("apiToken")
        pathToFile = GetParams("pathToFile")
        nameToUpload = GetParams("nameToUpload")

        plateRecognition_I = PlateRecognitionObj(apiToken)

        resultRecognition = plateRecognition_I.sendLicensePlate(pathToFile, nameToUpload)

        whereToStore = GetParams("whereToStore")
        SetVar(whereToStore, resultRecognition)


except Exception as e:
    print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
    PrintException()
    raise e
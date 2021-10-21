import requests
import base64
import json

class LicensePlateRecognitionObj:

    def __init__(self, secretKey):
        self.secretKey = secretKey

    def recognizeLicensePlate(self, pathToLicense, country):
        with open(pathToLicense, 'rb') as imageFile:
            imgBase64 = base64.b64encode(imageFile.read())
        
        url = f"https://api.openalpr.com/v3/recognize_bytes?recognize_vehicle=1&country={country}&secret_key={self.secretKey}"
        
        r = requests.post(url, data = imgBase64)
        a = r.json()["results"]
        
        dataReturned = {'License Plate' : a[0]["plate"],
                        'Vehicle Color' : a[0]["vehicle"]["color"][0]["name"],
                        'Vehicle Type' : a[0]["vehicle"]["body_type"][0]["name"],
                        'Vehicle Year' : a[0]["vehicle"]["year"][0]["name"]}
        
        return(dataReturned)

    def licensePlateData(self, pathToLicense, country):

        with open(pathToLicense, 'rb') as imageFile:
            imgBase64 = base64.b64encode(imageFile.read())

        url = f"https://api.openalpr.com/v3/recognize_bytes?recognize_vehicle=1&country={country}&secret_key={self.secretKey}"

        r = requests.post(url, data = imgBase64)
        a = r.json()

        return(a)

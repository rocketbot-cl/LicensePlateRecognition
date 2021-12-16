import requests

class PlateRecognitionObj:

    def __init__(self, token):
        self.token = token

    def sendLicensePlate(self, pathToFile, nameToUpload):
        
        headers = {
            "Authorization": f"Token {self.token}",
        }

        files = {
            "upload": (f"{nameToUpload}.jpg", open(pathToFile, "rb"))
        }
        
        params = {
            "regions": ("br"),
            "mmc" : True
        }

        response = requests.post("https://api.platerecognizer.com/v1/plate-reader", headers=headers, files=files, params=params)

        return response.json()

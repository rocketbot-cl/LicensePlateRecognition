



# License Plate Recognition
  
Analiza patentes y obtiene los datos de vehículo.  
  
![banner](imgs/Banner_LicensePlateRecognition.png)
## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de rocketbot.  




## Como usar este módulo
Para usar este módulo, tienes que conectarte a tu cuenta de CarCheck o usar tu cuenta de 
Plate Recognizer.

https://www.openalpr.com/software/carcheck
https://app.platerecognizer.com/

## Descripción de los comandos

### Conectar a CarCheck
  
Conecta a CarCheck para interactuar con la API.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|secretKey|Secret Key de la API obtenida en la página.|sk_72bd683k3e20rs2eb4b5e7c4|
|Asignar resultado a variable|Variable donde asignar el resultado.|Variable|

### CarCheck | Subir imagen para analizar
  
Sube una imagen para analizar la patente y obtener los datos del vehiculo desde CarCheck.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Pais|Siglas del país que se desea consultar.|br, us, eu, etc. (uno solo a la vez).|
|Ruta donde está la imagen de la patente|Ruta a la imagen de la cual se requiere analizar.|C:/Usuario/Documentos|
|Asignar resultado a variable|Variable donde asignar el resultado.|Variable|

### Plate Recognizer | Subir imagen para analizar
  
Subir una imagen para analizar en Plate Recognizer
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Token|Token de la API asignado a la cuenta.|3a0effff73919f898b69ac65a32dc12347769564|
|Nombre con el cual subir|Nombre con el cual sera agregado al nombre en el panel de Plate Recognizer.|nombre.jpg|
|Seleccionar un archivo|Ruta al archivo que se desea analizar.|C:/Usuario/Documentos|
|Asignar resultado a variable|Token de la API asignado a la cuenta.|Variable|

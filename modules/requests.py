import requests
def server_requests(is_admin = False):
  # Definir la URL a la cual deseas hacer la solicitud POST
  if is_admin:
    url = 'https://ejemplo.com/api/post_endpoint'
  else:
    url = 'https://ejemplo.com/api/post_endpoint'


  # Definir los datos que deseas enviar en la solicitud POST (pueden ser diccionarios)
  datos = {'clave1': 'valor1', 'clave2': 'valor2'}

  # Realizar la solicitud POST
  respuesta = requests.post(url, data=datos)

  # Verificar si la solicitud fue exitosa
  if respuesta.status_code == 200:
    print('Solicitud POST exitosa. Respuesta:')
    print(respuesta.text)
  else:
    print('La solicitud POST falló. Código de estado:', respuesta.status_code)

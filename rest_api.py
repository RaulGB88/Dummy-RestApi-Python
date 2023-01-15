import json
import time
import urllib.request

API_BASE = 'https://dummy.restapiexample.com/api/v1/'
ID_EMPLEADO = 1

def muestra_respuesta(res, metodo):
    print(metodo, "URL:", res.url)
    print(metodo, "status:", res.status)
    print(metodo, "cabeza:\n", res.headers)
    print(metodo, "cuerpo:\n", res.read())
    print()

def main():
    req_get = urllib.request.Request(API_BASE + 'employee/' + str(ID_EMPLEADO))
    with urllib.request.urlopen(req_get) as res_get:
        muestra_respuesta(res_get, 'GET')

    time.sleep(1)

    json_put = json.dumps({
        "employee_id": ID_EMPLEADO,
        "employee_age": 42}).encode('utf-8')
    req_put = urllib.request.Request(API_BASE + 'update/' + str(ID_EMPLEADO),
                                     method='PUT',
                                     data=json_put, headers={'Content-Type': 'application/json'})
    req_put.add_header('User-Agent', 'curl')
    with urllib.request.urlopen(req_put) as res_put:
        muestra_respuesta(res_put, 'PUT')

    time.sleep(1)

    req_delete = urllib.request.Request(API_BASE + 'delete/' + str(ID_EMPLEADO),
                                        method='DELETE')
    req_delete.add_header('User-Agent', 'curl')
    with urllib.request.urlopen(req_delete) as res_delete:
        muestra_respuesta(res_delete, 'DELETE')

    time.sleep(1)

    json_post = json.dumps({
        "employee_name": "Fulanito",
        "employee_age": 42}).encode('utf-8')
    req_post = urllib.request.Request(API_BASE + 'create',
                                      method='POST',
                                      data=json_post, headers={'Content-Type': 'application/json'})
    req_post.add_header('User-Agent', 'curl')
    with urllib.request.urlopen(req_post) as res_post:
        muestra_respuesta(res_post, 'POST')

if __name__ == '__main__':
    main()

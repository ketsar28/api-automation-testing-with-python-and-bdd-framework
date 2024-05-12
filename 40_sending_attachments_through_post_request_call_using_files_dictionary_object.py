import requests

url = "https://petstore.swagger.io/v2/pet/12322/uploadImage"
files = {'file': open('C:\\Users\\Devi\\Downloads\\selling\\image.png', 'rb')}

res_multipart_ef = requests.post(url, files=files)

print(res_multipart_ef.status_code)
print(res_multipart_ef.json())

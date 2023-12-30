import urllib.request
import json
response = urllib.request.urlopen("https://raw.githubusercontent.com/Shaikst/hashing/main/Hashing_dictionary.json")
html_content = json.loads(response.read().decode('utf-8'))
response = urllib.request.urlopen("https://raw.githubusercontent.com/Shaikst/hashing/main/info.txt")
hash_type = int(response.read().decode('utf-8').split("\n")[1])
print("██████╗░███████╗██╗░░░██╗░░░░░██╗███████╗██████╗░\n██╔══██╗██╔════╝██║░░░██║░░░░░██║██╔════╝██╔══██╗\n██║░░██║█████╗░░╚██╗░██╔╝░░░░░██║█████╗░░██████╦╝\n██║░░██║██╔══╝░░░╚████╔╝░██╗░░██║██╔══╝░░██╔══██╗\n██████╔╝███████╗░░╚██╔╝░░╚█████╔╝███████╗██████╦╝\n╚═════╝░╚══════╝░░░╚═╝░░░░╚════╝░╚══════╝╚═════╝░")
print("Разработанно DevJeb, используется "+hash_type+"-ая система")
a=input('Введите хэшированные данные: ')
b=[a[i:i+hash_type] for i in range(0, len(a), hash_type)]
result=""
for s in b:
    for v,h in html_content.items():
        if h==s:
            break
    result+=v
print('Ваш текст:\n\n\n' + result)

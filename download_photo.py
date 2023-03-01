import requests

def save_photo(name,url):
    img = requests.get(url)
    img_option = open ("photo/"+ name + '.jpg','wb')
    img_option.write(img.content)
    img_option.close()
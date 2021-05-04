from PIL import Image

path = input("Image name: ")
img =   Image.open(path).convert('RGB')

compressed = open(path+".txt","w+",encoding='utf-8')

pix = img.load()

dict = {

}
for y in range(300):
    for x in range(400):
        r = pix[x,y][0]
        g = pix[x,y][1]
        b = pix[x,y][2]
        # compressed.write(str(r) + "," + str(g) + "," + str(b) + "\r\n")
        key = chr(r + 32) + "," + chr(g + 32) + "," + chr(b + 32)
        if(key in dict):
            list = dict[key]
            list.append(str(x) + ":" + str(y))
            dict[key] = list
        else:
            dict[key] = [str(x) + ":" + str(y)]

for key, value in dict.items():
    compressed.write(key + "=" + str(value).replace(" ", "").replace(",", "").replace("''", "'") + "\r\n")

compressed.close()

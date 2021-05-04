from PIL import Image

path = input("Image name: ")
img =   Image.open(path).convert('RGB')

compressed = open(path+".txt","w+")

pix = img.load()

dict = {

}
for y in range(300):
    for x in range(400):
        r = round(pix[x,y][0] / 2)
        g = round(pix[x,y][1] / 2)
        b = round(pix[x,y][2] / 2)

        if(r == g == b):
            key = str(r)
        else:
            key = str(r) + "," + str(g) + "," + str(b)
        if(key in dict):
            list = dict[key]
            if(x==y):
                list.append(str(x))
            else:
                list.append(str(x) + ":" + str(y))
            dict[key] = list
        else:
            if(x==y):
                dict[key] = [str(x)]
            else:
                dict[key] = [str(x) + ":" + str(y)]

for key, value in dict.items():
    compressed.write(key + "=" + str(value).replace(" ", "").replace(",", "").replace("''", "'").replace("]", "").replace("[", "") + "\r\n")

compressed.close()

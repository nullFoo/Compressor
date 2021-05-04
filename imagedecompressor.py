from PIL import Image

path = input("Compressed file name: ")

compressed = open(path,"r")

img = Image.new(mode="RGB", size=(1000,1000), color=0)
pix = img.load()

for rgb in compressed:
  line = rgb.split("=")
  pixel = line[0].replace("[", "")
  for loc in line[1].split("'"):
      pos = loc.split(":")
      if(len(pos) == 2):
        color = pixel.split(",")
        pix[int(pos[0]), int(pos[1])] = (ord(color[0]), ord(color[1]), ord(color[2]))

img.show()

compressed.close()

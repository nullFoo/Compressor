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
        if(len(color) == 1):
            pix[int(pos[0]), int(pos[1])] = (int(color[0]) * 2, int(color[0]) * 2, int(color[0]) * 2)
        else:
            pix[int(pos[0]), int(pos[1])] = (int(color[0]) * 2, int(color[1]) * 2, int(color[2]) * 2)
      elif(len(pos) == 1):
          try:
              color = pixel.split(",")
              if(len(color) == 1):
                  pix[int(pos[0]), int(pos[0])] = (int(color[0]) * 2, int(color[0]) * 2, int(color[0]) * 2)
              else:
                  pix[int(pos[0]), int(pos[0])] = (int(color[0]) * 2, int(color[1]) * 2, int(color[2]) * 2)
          except:
              continue

img.show()

compressed.close()

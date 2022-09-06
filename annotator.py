
# import OS module
from fileinput import close
import os
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw as D
 
# Get the list of all files and directories
path = "C://Users//purpl//OneDrive//Documents//William_and_Mary//Software_Engineering//CS435IntroAssignment//Programming-Assignment-Data//"
files_list = os.listdir(path)
 
print("Files and directories in '", path, "' :")
 
# prints all files
print(files_list)

for i in range(len(files_list)):
    if files_list[i].endswith(".xml"):
        cur_xml = files_list[i]
        counter = i+1
        cur_image = cur_xml[0:-3] + "png"

        
        #cur_image = files_list[0]
        file = os.path.join(path, cur_xml)
        image_file = os.path.join(path, cur_image)


        with open(file, 'r', encoding = 'UTF-8') as f:
            xml_file = f.read()

            # print(lines)
        soup = BeautifulSoup(xml_file, "xml")

        nodes = soup.find_all('node')

        img = Image.open(image_file)
        for n in nodes:
            if(len(n.contents) == 0):
                bounds_str = n["bounds"]
                comma = bounds_str.index(",")
                closedBracket = bounds_str.index("]")
                x1 = bounds_str[1:comma]
                y1 = bounds_str[comma+1:closedBracket]
                comma = bounds_str.index(",", closedBracket)
                x2 = bounds_str[closedBracket+2:comma]
                y2 = bounds_str[comma+1:(len(bounds_str)-1)]
          
                draw=D.Draw(img)
                draw.rectangle([(int(x1),int(y1)),(int(x2),int(y2))],outline="yellow", width = 5)
        img.show()
        img = img.save(cur_xml[0:-4] + "Annotated.png")

    



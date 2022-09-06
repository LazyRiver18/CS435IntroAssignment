
import os
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw as D
 
# Get the list of all files and directories from the user
path = input("Please enter the path of the set of xml/png files: ")
files_list = os.listdir(path)

#for each xml file, sets the corresponding png file to annotate
for i in range(len(files_list)):
    if files_list[i].endswith(".xml"):
        cur_xml = files_list[i]
        counter = i+1
        cur_image = cur_xml[0:-3] + "png"

        #retreiving the files from the user's path
        file = os.path.join(path, cur_xml)
        image_file = os.path.join(path, cur_image)


        with open(file, 'r', encoding = 'UTF-8') as f:
            xml_file = f.read()

        #parses the xml file for an easier to manipulate hierarchy
        soup = BeautifulSoup(xml_file, "xml")

        #puts all the node tags into a list
        nodes = soup.find_all('node')

        img = Image.open(image_file)
        for n in nodes:

            #finds and puts boxes around the nodes with no children (involves parsing the bounds attribute string)
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

        # used for debugging purposes
        # img.show() 

        #saves each annotated png file
        img = img.save(cur_xml[0:-4] + "Annotated.png")

    



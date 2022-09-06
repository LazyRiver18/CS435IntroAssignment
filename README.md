# CS435IntroAssignment

This is the take-home programming assignment for the Software Engineering Course

I have imported os, Pillow, and BeautifulSoup for use in this project, but the code should compile as is. To run the code, when prompted, the user should input the path to the directory with the set of xml/png files.

input example:
"C://Users//purpl//OneDrive//Documents//William_and_Mary//Software_Engineering//CS435IntroAssignment//Programming-Assignment-Data//"

Program Description:

My program takes as input the user's path to the directory with the needed xml/png file pairs. It then goes through each file, and for each xml file, it retrieves the corresponding png filename and then both file names are appended to the path so the files can be opened and used. The xml file is then opened, read, and then organized and parsed into nodes using BeautifulSoup. I then open the image file before iterating through each node. For each node that has 0 children, I retrive the bounds attribute. I then parse the string into 4 numbers to use as the coordiates to draw a yellow rectangle using Pillow. Finally, after drawing a rectangle around each node with no children, I save the final image to the repository.

I open the image before iterating through each node (rather than open in the loop) in order to ensure each rectangle is drawn on the same image, and the original file is not reopened for each node. I used a for loop for the files so that every xml file is opened and I store the current xml file name to extract the name of the png file (without having to search through all the files for the same name). Lastly, I used the index function when parsing the bounds to find "waypoints" (the comma and closing bracket) in the attribute string that would help me find where a number started and ended more easily.

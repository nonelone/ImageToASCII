from PIL import Image
import sys

def convertImage(path, scale):
    # first we open image from path
    image = Image.open(path)
    # then we get it's new size by dividing current sizes by "scale" variable
    (sizeX, sizeY) = image.size
    sizeX = int( sizeX / scale )
    sizeY = int( sizeY / scale )
    # next we resize and convert image to grayscale
    # note: since Image is unmutalble it must be reasigned every time!
    image = image.resize((sizeX,sizeY))
    image = image.convert("L")
    # at last, we return Image object that is both resized and converted to greyscale and it's dimensions
    return [image, sizeX, sizeY]

def generateASCIIText(imageData):
    # we extract usefull variables from "imageData" table
    image = imageData[0]
    sizeX = imageData[1]
    sizeY = imageData[2]
    # we create our output variable
    output = ""
    # for every pixel in the image
    for y in range(sizeY):
        for x in range(sizeX):
            # we read it's color and get % of color strength
            percentage = int( image.getpixel( (x,y) ) / 255 * 100 )
            # and at last we assign every pixel ASCII sybol depending on it's color strength
            if percentage >= 0 and percentage < 20: output = output + "."
            if percentage >= 20 and percentage < 40: output = output + ":"
            if percentage >= 40 and percentage < 60: output = output + "o"
            if percentage >= 60 and percentage < 80: output = output + "0"
            if percentage >= 80: output = output + "#"
            # if it's last pixel in row, we also include EOL to make the image 2D
            if x == (sizeX - 1): output = output + "\n"

    # after both loops are finished, all pixels have been converted to letters and are stored in our "output" variable
    # we return "output" string variable
    return output

if __name__ == "__main__":
    # first we check if input is correct
    if len(sys.argv) == 3:
        # if so, we get path and desired scale from arguments
        path = sys.argv[1]
        scale = int(sys.argv[2])
        # after that we open, resize and convert to grayscale image from "path"
        resizedImageData = convertImage(path, scale)
        # next we convert the resized, grayscale image to ASCII text
        text = generateASCIIText(resizedImageData)
        # at last, we put it in output.txt file
        with open("output.txt", "w") as file: file.write(text)
        # note: the image will look thiner than it is supposed to do
        # this is caused by differences in height and width of ASCII symbols used in conversion
        # a quick, but not recommended solution is:
        # instead of scaling the image evenly (that is dividing both sizes by the same variable)
        # we divide "sizeY" by scale, but "sizeX" by 1/2 of scale, thus making the image 2 times wider
        # in code:
        """
        sizeX = int( sizeX / (scale / 2) )
        sizeY = int( sizeY / scale )

        """

from modules import steg

def combine (message, imgFile, new1):
    imageFilename = "../img_pass/" + imgFile + ".jpg"
    newImageFilename = "./img_pass/" + new1

    steg.encodeLSB(message, imageFilename, newImageFilename)
    steg.decodeLSB(imgFile)
    return 1

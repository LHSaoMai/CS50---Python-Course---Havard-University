from PIL import Image
from PIL import ImageOps

import sys

def shirt():
    length = len(sys.argv)
    if length < 3:
        sys.exit('Too few command-line arguments')
    elif length >3:
        sys.exit('Too many command-line arguments')

    try:
        file1_name, ext1= sys.argv[1].split('.')
        file2_name, ext2 = sys.argv[2].split('.')

        if (ext1=='jpg' or ext1=='jpeg' or ext1=='png') and (ext2=='jpg' or ext2=='jpeg' or ext2=='png'):
            if ext1 == ext2:
                shirt = Image.open("shirt.png")
                humain = Image.open(sys.argv[1])
                size=shirt.size
                humain_size=ImageOps.fit(humain,size)
                humain_size.paste(shirt, (0, 0), shirt)
                humain_size.save(sys.argv[2])
            else:
                sys.exit('Input and output have different extensions')


        else:
            sys.exit('Invalid output')


    except FileNotFoundError:
         sys.exit('File does not exist')

shirt()

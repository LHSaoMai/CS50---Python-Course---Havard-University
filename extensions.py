import mimetypes
afile = input("Give your file name, please ").strip()
extension, other = mimetypes.guess_type(afile)

if extension == None:
    print('application/octet-stream')
else:
    print(extension)

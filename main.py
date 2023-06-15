import os      #IMPORTING OS MODULE FOR OPERATING SYSTEM

def create_if_not_present(folder):       #The function ensures that a folder of the names passed as argument in it is formed.
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(foldername, files):            #The function enables movement of files with different extensions in specified folders.
    for file in files:
        os.replace(file, f"{foldername}/{file}")

if __name__ == "__main__" :

    files = os.listdir()
    files.remove("main.py")

    create_if_not_present("Images")
    create_if_not_present("Documents")
    create_if_not_present("Medias")
    create_if_not_present("Others")

    imagext = [".png", ".jpg", "jpeg"]              #the list is about the extensions considered as images.
    images = [file for file in files if os.path.splitext(file)[1].lower() in imagext]

    docext = [".txt", ".docx", ".doc", ".pdf"]      #the list is about the extensions considered as documents.
    documents = [file for file in files if os.path.splitext(file)[1].lower() in docext]

    mediext = [".mp4", ".flv", ".mp3"]              #the list is about the extensions considered as medias.
    medias = [file for file in files if os.path.splitext(file)[1].lower() in mediext]

    others = []
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if(ext not in imagext) and (ext not in docext) and (ext not in mediext):
            others.append(file)                                                         #The block of code prepares a list of those files which
                                                                                        # don't lie in any of the three categories given above.

    #The move functions with arguments are responsible for movement of files in folder, considering the extension.

    move("Images", images)
    move("Documents", documents)
    move("Medias", medias)
    move("Others", others)

import os
import numpy as np
from PIL import Image, ImageTk
from tkinter import *
from tkinter import ttk
import PIL.Image
if not hasattr(PIL.Image, "ANTIALIAS"):
    PIL.Image.ANTIALIAS = PIL.Image.Resampling.LANCZOS
from tkinter import messagebox
import mysql.connector
import cv2
class Train:
    def __init__(self,root):
        self.root=root
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        win_w = min(1530, screen_w)
        win_h = min(790, max(650, screen_h - 60))
        self.root.geometry(f"{win_w}x{win_h}+0+0")
        self,root.title("Train Dataset")

        title_lbl = Label(self.root, text="TRAIN DATASET",
                          font=("times new roman", 25, "bold"), bg="darkblue", fg="white")
        title_lbl.place(x=0, y=0, width=win_w, height=45)

        img4 = PIL.Image.open(r"ImageFaceDetect\sv2.jpg")
        img4 = img4.resize((win_w, 325), PIL.Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        f_lbl = Label(self.root, image=self.photoimg4)
        f_lbl.place(x=0, y=55, width=win_w, height=325)

        #Btn Train
        b1_1 = Button(self.root, text="TRAIN DATA", cursor="hand2", command=self.train_classifier,
                      font=("times new roman", 25, "bold"), bg="RED", fg="white")
        b1_1.place(x=0, y=380, width=win_w, height=60)


        img5 = PIL.Image.open(r"ImageFaceDetect\sv2.jpg")
        img5 = img5.resize((win_w, 325), PIL.Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        f_lbl = Label(self.root, image=self.photoimg5)
        f_lbl.place(x=0, y=440, width=win_w, height=325)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]
        for image in path:
            img=PIL.Image.open(image).convert('L')
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #=================Train data classifier and save============
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Kết quả","Training dataset Completed")




if __name__=="__main__":
    root=Tk() #khoi tao cua so va gan root vao
    obj=Train(root)
    root.mainloop()# cua so hien len
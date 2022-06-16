from tkinter import *
from tkinter.ttk import *
from PIL import Image,ImageTk


def loadingfun():

        root5 = Tk()
        root5.geometry("770x150+230+200")

        root5.wait_visibility()     #wait while root window is visible

        busicon = ImageTk.PhotoImage(file="template.png")
        l1 = Label(root5,image=busicon).place(x=40,y=10,width=700,height=100)


        loading = Frame(root5).place(x=40,y=120,width=700,height=20)

        progress = Progressbar(loading, orient = HORIZONTAL,length = 700, mode = 'determinate')
        progress.place(x=40,y=125)


        def bar():
            import time

            for i in range(52):
                progress['value'] = i*2
                root5.update_idletasks()
                time.sleep(.02)
            root5.destroy()

        bar()      #calling loading function
        root5.mainloop()


if  __name__=='__main__' :
   loadingfun()

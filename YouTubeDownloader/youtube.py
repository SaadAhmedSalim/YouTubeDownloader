from tkinter import*
class Youtube_app:
    def __init__(self,root):
        self.root = root
        self.root.title("YouTube Downloader 2021")
        self.root.geometry("500x420+300+500")
        self.root.resizable(False, False)
        self.root.config(bg='white')

        title = Label(self.root, text="            YouTube Downloader [Developed By Saad]",
                        font=("Times new roman", 16), bg="#262626",
                            fg='white', anchor='w').pack(side=TOP, fill=X)

        lbl_url = Label(self.root, text="Video URL",
                        font=("Times new roman", 15), bg="white").place(x=10, y=50)

        txt_url = Entry(self.root,
                        font=("Times new roman", 13), bg="lightyellow").place(x=120, y=50, width=350)

        lbl_filetype = Label(self.root, text="File Type",
                        font=("Times new roman", 15,), bg="white").place(x=10, y=90)

        self.var_fileType=StringVar()
        self.var_fileType.set('Video')
        video_radio = Radiobutton(self.root, text="Video", variable=self.var_fileType, value="Video",
                        font=("Times new roman", 15), bg="white", activebackground='white').place(x=120, y=90)

        audio_radio = Radiobutton(self.root, text="Audio", variable=self.var_fileType, value="Audio",
                        font=("Times new roman", 15), bg="white", activebackground='white').place(x=220, y=90)

        btn_search=Button(self.root, text="Search",
                        font=('Times, new roman',15), bg='red', fg='white').place(x=350, y=90, height=30, width=120)


        frame1=Frame(self.root, bd=2, relief=RIDGE, bg='lightyellow')
        frame1.place(x=10, y=130, width=480, height=180)

        self.video_title = Label(frame1, text="Video Title Here",
                                font=("Times new roman", 12), bg="lightgrey", anchor='w')
        self.video_title.place(x=0, y=0, relwidth=1)

        self.video_image = Label(frame1, text="Video \nImage",
                                font=("Times new roman", 15), bg="lightgrey", bd=2, relief=RIDGE)
        self.video_image.place(x=5, y=30, width=180, height=140)

        lbl_desc = Label(frame1, text="Description",
                                font=("Times new roman", 15), bg="lightyellow").place(x=190, y=30)






root = Tk()
obj = Youtube_app(root)
root.mainloop()

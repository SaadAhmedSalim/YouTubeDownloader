from tkinter import*
from tkinter import ttk
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

        # select the type of the download file
        self.var_fileType=StringVar()
        # Default activated video radio button
        self.var_fileType.set('Video')
        video_radio = Radiobutton(self.root, text="Video", variable=self.var_fileType, value="Video",
                        font=("Times new roman", 15), bg="white", activebackground='white').place(x=120, y=90)

        audio_radio = Radiobutton(self.root, text="Audio", variable=self.var_fileType, value="Audio",
                        font=("Times new roman", 15), bg="white", activebackground='white').place(x=220, y=90)

        # Button for Search link
        btn_search=Button(self.root, text="Search",
                        font=('Times, new roman',15), bg='red', fg='white').place(x=350, y=90, height=30, width=120)


        # Frame Created
        frame1=Frame(self.root, bd=2, relief=RIDGE, bg='lightyellow')
        frame1.place(x=10, y=130, width=480, height=180)

        # Inside Frame
        self.video_title = Label(frame1, text="Video Title Here",
                                font=("Times new roman", 12), bg="lightgrey", anchor='w')
        self.video_title.place(x=0, y=0, relwidth=1)

        self.video_image = Label(frame1, text="Video \nImage",
                                font=("Times new roman", 15), bg="lightgrey", bd=2, relief=RIDGE)
        self.video_image.place(x=5, y=30, width=180, height=140)

        lbl_desc = Label(frame1, text="Description",
                                font=("Times new roman", 15), bg="lightyellow").place(x=190, y=30)
        self.video_desc = Text(frame1,
                                font=("Times new roman", 12), bg="lightyellow")
        self.video_desc.place(x=190, y=60, width=280, height=110)
        # Frame Ended

        # Total Size will be shown
        self.lbl_size = Label(self.root, text="Total Size: MB",
                                font=("Times new roman", 13))
        self.lbl_size.place(x=10, y=320)

        # Downloading percentage will be shown
        self.lbl_percentage = Label(self.root, text="Downloading: 0%",
                                        font=("Times new roman", 13), bg='white')
        self.lbl_percentage.place(x=170, y=320)


        # Button for clear the link
        btn_clear=Button(self.root, text="Clear",
                        font=('Times, new roman',13), bg='grey', fg='white').place(x=320, y=320, height=25, width=70)
        # Button for download the link
        btn_clear=Button(self.root, text="Clear",
                        font=('Times, new roman',13), bg='green', fg='white').place(x=400, y=320, height=25, width=90)

        # Call the ttk
        self.prog = ttk.Progressbar(self.root, orient=HORIZONTAL, length=590, mode='determinate')
        self.prog.place(x=10, y=360, width=485, height=20)

        # Downloading percentage will be shown
        self.lbl_message = Label(self.root, text="Error Messages",
                                font=("Times new roman", 13), bg='white')
        self.lbl_message.place(x=0, y=385, relwidth=1)




root = Tk()
obj = Youtube_app(root)
root.mainloop()

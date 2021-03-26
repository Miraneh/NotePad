import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *


class NotePad:
    __root = Tk()

    __width = 300
    __height = 300
    __thisTextArea = Text(__root)
    __thisMenuBar = Menu(__root)
    __thisFileMenu = Menu(__thisMenuBar, tearoff=0)
    __thisEditMenu = Menu(__thisMenuBar, tearoff=0)
    __thisHelpMenu = Menu(__thisMenuBar, tearoff=0)

    __thisScrollBar = Scrollbar(__thisTextArea)
    __file = None

    def __init__(self, **kwargs):
        try:
            self.__root.wm_iconbitmap("Notepad.ico")
        except:
            pass

        try:
            self.__width = kwargs['width']
        except KeyError:
            pass

        try:
            self.__height = kwargs['height']
        except KeyError:
            pass

        self.__root.title("untitled - notepad")

        screenWidth = self.__root.winfo_width()
        screenHeight = self.__root.winfo_height()

        left = (screenWidth / 2) - (self.__width / 2)
        top = (screenHeight / 2) - (self.__height / 2)

        self.__root.grid_rowconfigure(0 , weight = 1)
        self.__root.grid_columnconfigure(0, weight = 1)

        self.__thisTextArea.grid(sticky = N + E + S + W)

        self.__thisFileMenu.add_command(label = "New", command = self.__newFile)

        self.__thisFileMenu.add_command(label="Open", command=self.__openFile)

        self.__thisFileMenu.add_command(label="Save", command=self.__saveFile)


        self.__thisFileMenu.add_separator()
        self.__thisFileMenu.add_command(label="Exit", command=self.__quitApplication)
        self.__thisMenuBar.add_cascade(label="File", menu=self.__thisFileMenu)

        self.__thisEditMenu.add_command(label="Cut", command=self.__cut)

        self.__thisEditMenu.add_command(label="Copy", command=self.__copy)

        self.__thisEditMenu.add_command(label="Paste", command=self.__paste)

        self.__thisMenuBar.add_cascade(label="Edit", menu=self.__thisEditMenu)

        self.__thisHelpMenu.add_command(label="About Notepad", command=self.__showAbout)
        self.__thisMenuBar.add_cascade(label="Help", menu=self.__thisHelpMenu)

        self.__root.config(menu=self.__thisMenuBar)

        self.__thisScrollBar.pack(side=RIGHT, fill=Y)

        self.__thisScrollBar.config(command=self.__thisTextArea.yview)
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)

    def __quitApplication(self):
        self.__root.destroy()

    def __openFile(self):

        self.__file = askopenfilename(defaultextention = ".txt",
                                      filetypes = [("All Files", "*.*"),
                                                   ("Text Documents", "*.txt")])
        if self.__file == "":
            self.__file = None
        else:
            self.
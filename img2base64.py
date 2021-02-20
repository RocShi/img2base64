# -*- coding: utf-8 -*-
#
# @File          : img2base64.py
# @Version       : 1.1
# @Description   : This script is for converting image to base64 string which can
#                  be inserted into markdown document directly to display.
# @Environment   : Windows/Linux, Python 3
# @Author        : ShiPeng
# @Email         : RocShi@outlook.com
# @Created       : 2020-01-19
# @Last modified : 2021-02-20

import os
import time
import string
import base64
import pyperclip
import datetime

from tkinter import *
from tkinter import filedialog, messagebox


class img2base64(object):
    def __init__(self):
        # initate window
        self.window = Tk()
        self.window.title("img2base64 v1.1")
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()
        self.window_width = 800 if os.name == "posix" else 820
        self.window_height = 84 if os.name == "posix" else 100
        self.window.geometry(
            "%sx%s+%s+%s" %
            (self.window_width, self.window_height,
             int((self.screen_width - self.window_width) / 2),
             int((self.screen_height - self.window_height) / 2)))
        self.window.resizable(False, False)
        if os.name != "posix": self.AddIcon()

        # initiate single image related
        self.button_select_single = Button(
            self.window,
            width=15 if os.name == "posix" else 18,
            text="Select single image",
            command=self.SelectSingleImage)
        self.button_select_single.grid(row=0, column=0)

        self.button_convert_single = Button(
            self.window,
            width=15 if os.name == "posix" else 18,
            text="Convert & Copy",
            command=self.ConvertSingleImage)
        self.button_convert_single.grid(row=0, column=2)
        self.entry_path_single = Entry(self.window, width=62)
        self.entry_path_single.grid(row=0, column=1)

        # initiate several images related
        self.button_select_several = Button(
            self.window,
            width=15 if os.name == "posix" else 18,
            text="Select several images",
            command=self.SelectSeveralImage)
        self.button_select_several.grid(row=1, column=0)

        self.button_convert_several = Button(
            self.window,
            width=15 if os.name == "posix" else 18,
            text="Convert & Export",
            command=self.ConvertSeveralImage)
        self.button_convert_several.grid(row=1, column=2)
        self.entry_path_several = Entry(self.window, width=62)
        self.entry_path_several.grid(row=1, column=1)

        # progress bar related
        self.progressbar_label_left = Label(self.window,
                                            text="Progress:",
                                            width=18)
        self.progressbar_label_left.grid(row=2, column=0)
        self.progressbar_canvas_width = 498 if os.name == "posix" else 501
        self.progressbar_canvas_fillwidth = 500 if os.name == "posix" else 505
        self.progressbar_canvas = Canvas(self.window,
                                         width=self.progressbar_canvas_width,
                                         height=18,
                                         bg="white")
        self.progressbar_canvas.grid(row=2, column=1)
        self.progressbar_state = StringVar()
        self.ProgressBarSetState()
        self.progressbar_label_right = Label(
            self.window, textvariable=self.progressbar_state)
        self.progressbar_label_right.grid(row=2, column=2)

        # path related
        self.default_img_path = r"~"
        self.default_folder_path = r"~"
        self.image_path = r""
        self.folder_path = r""
        self.img_extension_names = [
            "webp", "bmp", "pcx", "tif", "gif", "jpeg", "tga", "exif", "fpx",
            "svg", "psd", "cdr", "pcd", "dxf", "ufo", "eps", "ai", "png",
            "hdri", "raw", "wmf", "flic", "emf", "ico", "jpg"
        ]
        self.imgs = []

    def AddIcon(self):
        from ico import ico
        self.icon = open(os.getcwd() + "/ico.ico", "wb+")
        self.icon.write(base64.b64decode(ico))
        self.icon.close()
        self.window.iconbitmap(os.getcwd() + "/ico.ico")
        os.remove(os.getcwd() + "/ico.ico")

    def SelectSingleImage(self):
        self.image_path = filedialog.askopenfilename(
            title="Select single image",
            initialdir=(os.path.expanduser(self.default_img_path)))

        # click cancell button while selecting an image
        if self.image_path == "": return

        try:
            if (self.image_path.split(".")[-1].lower()
                    in self.img_extension_names):
                self.entry_path_single.delete(0, END)
                self.entry_path_single.insert(0, self.image_path)
                self.ProgressBarClear(1)
            else:
                self.ProgressBarClear(0)
                messagebox.showerror("Error",
                                     "Please select an valid image file!")
        except:
            pass

    def ConvertSingleImage(self):
        try:
            img = open(self.entry_path_single.get(), 'rb')
            result = base64.b64encode(img.read())
            img.close()
            pyperclip.copy(str(result)[2:-1])
            self.ProgressBarFill()
            messagebox.showinfo(
                "Done",
                "Done, just paste the base64 string everywhere you want!")
        except:
            self.ProgressBarClear(0)
            messagebox.showerror("Error", "Please select an valid image file!")

    def SelectSeveralImage(self):
        self.image_path = filedialog.askdirectory(
            title="Select several images",
            initialdir=(os.path.expanduser(self.default_folder_path)))

        # click cancell button while selecting images' directory
        if self.image_path == "": return

        try:
            self.imgs = [
                (self.image_path + "/" + i)
                for i in os.listdir(self.image_path)
                if (os.path.isfile(os.path.join(self.image_path, i)) and (
                    i.split(".")[-1].lower() in self.img_extension_names))
            ]
            if len(self.imgs) == 0:
                self.ProgressBarClear(0)
                messagebox.showerror("Error",
                                     "No images exist in select directory!")
            else:
                self.entry_path_several.delete(0, END)
                self.entry_path_several.insert(0, self.image_path)
                self.ProgressBarClear(len(self.imgs))
        except:
            self.ProgressBarClear(0)
            messagebox.showerror("Error", "Please select an valid directory!")

    def ConvertSeveralImage(self):
        try:
            self.imgs = [
                (self.entry_path_several.get() + "/" + i)
                for i in os.listdir(self.entry_path_several.get())
                if (os.path.isfile(self.entry_path_several.get() + "/" + i))
                and (i.split(".")[-1].lower() in self.img_extension_names)
            ]
        except:
            self.ProgressBarClear(0)
            messagebox.showerror("Error",
                                 "Please select an valid image directory!")
            return
        try:
            if len(self.imgs) == 0:
                self.ProgressBarClear(0)
                messagebox.showerror("Error",
                                     "No images exist in select directory!")
            else:
                dt = datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")
                floder_name = "img2base64_" + self.entry_path_several.get(
                ).split("/")[-1] + "_" + dt
                self.folder_path = filedialog.askdirectory(
                    title="Select saved directory",
                    initialdir=(os.path.expanduser(self.default_folder_path)))

                # click cancell button while selecting saved directory
                if self.folder_path == "": return

                self.folder_path = self.folder_path + "/" + floder_name
                os.makedirs(self.folder_path)
                self.ProgressBarClear(len(self.imgs))

                for image in self.imgs:
                    img = open(image, 'rb')
                    result = base64.b64encode(img.read())
                    img.close()
                    file = open(
                        self.folder_path + "/" +
                        image.split("/")[-1].split(".")[0], "w")
                    file.write(str(result)[2:-1])
                    file.close()
                    self.ProgressBarFill(self.imgs.index(image),
                                         len(self.imgs))

                messagebox.showinfo(
                    "Done", "Done! Converted files are saved under {}.".format(
                        self.folder_path))
        except:
            raise

    def ProgressBarClear(self, fill_number=1):
        fill_line = self.progressbar_canvas.create_rectangle(1.5,
                                                             1.5,
                                                             0,
                                                             23,
                                                             width=0,
                                                             fill="white")
        self.progressbar_canvas.coords(
            fill_line, (0, 0, self.progressbar_canvas_fillwidth, 60))
        self.ProgressBarSetState(0, fill_number)
        self.window.update()

    def ProgressBarFill(self, current=0, fill_number=1):
        fill_line = self.progressbar_canvas.create_rectangle(1.5,
                                                             1.5,
                                                             0,
                                                             23,
                                                             width=0,
                                                             fill="green")
        self.progressbar_canvas.coords(
            fill_line, (0, 0, (current + 1) *
                        self.progressbar_canvas_fillwidth / fill_number, 60))
        self.ProgressBarSetState(current + 1, fill_number)
        self.window.update()

    def ProgressBarSetState(self, done=0, total=0):
        self.progressbar_state.set("%s/%s" % (done, total))

    def done(self):
        mainloop()


def main():
    obj = img2base64()
    obj.done()


if __name__ == "__main__":
    main()

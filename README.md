<p align="right">
  <a href="docs/README-CN.md">简体中文</a>
</p>

# PREFACE

* This tool is for converting image to base64 string which can be inserted into markdown document directly to display without upload the image to server.

* You can use the converted string like [demo.md](demo/demo.md) show.

* Tests of this tool were conducted only on **windows 7 / 10** and **ubuntu 14.04 / 16.04 / 18.04**.

# FEATURE

* Convert single image to base64 string and copy the string to clipboard automatically.

* Convert mutiple images to base64 strings which are stored in respective files.

* Converting progress display.

# DEPENDENCY

* Python 3.1 or newer version

* `pyperclip`

  ```bash
  pip install pyperclip
  ```

* `tkinter`

  For windows, `tkinter` is included with all standard Python distributions since Python 3.1. For ubuntu, install `tkinter` as follows.

  ```bash
  sudo apt-get install python3-tk
  ```

* `xclip`
  
  For ubuntu, you must install `xclip` before using this tool. 

  ```bash
  sudo apt-get install xclip
  ```

# USAGE

## Run the tool

```bash
python img2base64.py
```

## Single image convertion

* Click `Select single image` button first to select the image and then click `Convert & Copy` button to convert the image. Converted base64 string will be copied to clipboard automatically.

## Several images convertion

* Click `Select several images` button first to select the path which stored the images and then click `Convert & Export` button to convert every image under the path to a single file and select another path to save the result.


# EPILOGUE

You can use [`PyInstaller`](https://pypi.org/project/pyinstaller/) to package the tool script and all its dependencies into a single executable file.

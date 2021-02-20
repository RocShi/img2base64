<p align="right">
  <a href="../README.md">English</a>
</p>

# 前言

* 本工具用于将图像转换为 base64 字符串，转化得到的 base64 字符串可以直接插入到 markdown 文档中用于显示图像，而无需将图像传到服务器

* 您可以像 [demo.md](../demo/demo.md) 中那样使用转换得到的字符串

* 本工具仅在 **windows 7 / 10** 和 **ubuntu 14.04 / 16.04 / 18.04** 上进行了测试

# 特性

* 将单一图片转换为 base64 字符串，并将转换结果自动复制到剪贴板

* 将多图片转换为 base64 字符串，并将转换结果保存至各自的文本文件

* 转换进度显示

# 依赖

* Python 3.1 及更高版本

* `pyperclip`

  ```bash
  pip install pyperclip
  ```

* `tkinter`

  对于 windows 系统，自 Python 3.1 起，`tkinter` 默认包含于 Python 发行版。对于 ubuntu系统，需要执行下述命令安装 `tkinter`。

  ```bash
  sudo apt-get install python3-tk
  ```

* `xclip`
  
  对于 ubuntu 系统，在使用本工具前需要先安装 `xclip`。 

  ```bash
  sudo apt-get install xclip
  ```

# 用法

## 运行工具

```bash
python img2base64.py
```

## 单一图片转换

* 首先点击`Select single image`按钮选择目标图片，然后点击`Convert & Copy`按钮转换图片，转换得到的base64字符串会自动复制到剪贴板。

## 多图片转换

* 首先点击`Select several images`按钮选择目标图片的存放路径，然后点击`Convert & Export`按钮选择存放转换结果的路径，每张图片会被转换到各自对应的文件。

# 后记

可以使用 [`PyInstaller`](https://pypi.org/project/pyinstaller/) 将工具脚本及其所有依赖打包为一个单一可执行文件。

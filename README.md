# MarkdownPicPicker

## Introduce

 forked from kingname/MarkdownPicPicker
MarkdownPicPicker is an assistant which can help you add picture in Markdown. It will upload the image in your clipboard to web picture host and copy the Markdown-format link(\!\[\]\(url\)) to your clipboard or pasteboard. Now it supports Windows and Mac OS.

## Function


4. Picture will be saved to local first.
3. Copy the Markdown-format link to clipboard or pasteboard.
5. Easy to add your own uploader.

## How to use

### Mac OS
1. Install pngpaste: `brew install pngpaste`
2. Clone MarkdownPicPicker source code
3. Copy image into pasteboard
4. `python MarkdownPicPicker.py`
5. run command:`ln -s `pwd`/save_current_pwd.sh /usr/local/bin/save_current_pwd`
6. add command `save_current_pwd` to your `~/.bashrc` file or `~/.zshrc` file
7. create a workflow in Alfred: "command + ctrol + shift + v" -> run_mac.sh


#! /bin/bash
pushd `cat ~/pwd` >/dev/null
echo -n "pwd="
echo `pwd`
python ~/cool_tools/MarkdownPicPicker/MarkdownPicPicker.py -pic_path  ./img
popd > /dev/null

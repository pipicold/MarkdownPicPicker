from ImageGrab import ImageGrab
import sys
import os
try:
    from config import read_config
except Exception as _:
    #print('read config error, use default info.')
    read_config = None

__version__ = '1.1.0'
__author__ = 'kingname'


class MarkrdownPicPicker(object):

    def __init__(self, link_only=False, picture_folder='pic'):
	self.cwd = ''
	self.picture_folder = picture_folder
	self.picture_suffix = 'png'
	self.picture_host = ''
	self.uploader = None
	self.link_only = link_only
	self.config_path = ''
	self.uploader_info = {}
	self.imageGrab = None
	self.init_environment()

	self.upload_picture()

    def _write_markdown_picture_url(self, pic_url, link_only=False):
	if link_only:
	    markdown_picture_url = pic_url
	else:
	    markdown_picture_url = '![]({})'.format(pic_url)
	platform = sys.platform
	command = ''
	if platform == 'win32':
	    command = 'echo {} | clip'.format(markdown_picture_url)
	elif platform == 'darwin':
	    command = 'echo "{}" | pbcopy'.format(markdown_picture_url)
	os.system(command)
	print('%s copied!' % markdown_picture_url)

    def _to_string(self):
	"""
	To test if the config reading is ok
	:return: None
	"""
	print("folder", self.picture_folder)
	print("suffix", self.picture_suffix)
	print("picture_host", self.picture_host)

    def init_environment(self):
	if not os.path.exists(self.picture_folder):
	    print("new pic folder")
	    os.makedirs(self.picture_folder)
	self.imageGrab = ImageGrab(self.picture_folder, self.picture_suffix) if ImageGrab else None
	if not self.imageGrab:
	    print('can not find image grab, exit.')
	    exit()

    def upload_picture(self):
	picture_path = self.imageGrab.save_picture()
	if not picture_path:
	    return False
	else:
	    self._write_markdown_picture_url(picture_path);
	    return True

    def _find_uploader(self):
	uploader_folder = os.path.join(self.cwd, 'uploader')
	if os.path.isdir(uploader_folder):
	    uploader_list = [uploader_file.split('.')[0] for uploader_file in os.listdir(uploader_folder)]
	    if uploader_list:
		return uploader_list

	print('can not find the uploader folder.')
	exit()

if __name__ == '__main__':
    arg = sys.argv[-1]
    if sys.argv[1] == '-linkonly':
	MarkrdownPicPicker(link_only=True)
    elif sys.argv[1] == '-pic_path':
	MarkrdownPicPicker(picture_folder=sys.argv[2])
    else:
	MarkrdownPicPicker()

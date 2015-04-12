# -*- coding: utf-8 -*-
INSTALLED_APPS = add_to_tuple(INSTALLED_APPS, 'filebrowser', before="ckeditor")

# Directory to save image versions (and thumbnails). If no directory is given, 
# versions are stored at the same location as the original image
FILEBROWSER_VERSIONS_BASEDIR = '_uploads_versions'

# Max. Upload Size in Bytes
FILEBROWSER_MAX_UPLOAD_SIZE = 10*1024*1024 # 10 Mb

# True if you want to normalize filename on upload and remove all 
# non-alphanumeric characters (except for underscores, spaces & dashes)
FILEBROWSER_NORMALIZE_FILENAME = True

# Define the image versions that is image resizing, mostly used to make thumbnails
# You can let one of the size empty to let it free to resize and respecting the 
# ratio. Like if you let the 'height' empty, the resize will respect the ratio 
# according to the given 'width'.
FILEBROWSER_VERSIONS = {
    # Defaults, don't remove them, but you can edit their sizes
    # Also you can add other versions if you need
    'admin_thumbnail': {'verbose_name': 'Admin Thumbnail', 'width': 60, 'height': 60, 'opts': 'crop'},
    'thumbnail': {'verbose_name': 'Thumbnail (60x60)', 'width': 60, 'height': 60, 'opts': 'crop'},
    'small': {'verbose_name': 'Small (140xauto)', 'width': 140, 'height': '', 'opts': ''},
    'medium': {'verbose_name': 'Medium (300xauto)', 'width': 300, 'height': '', 'opts': ''},
    'big': {'verbose_name': 'Big (460xauto)', 'width': 460, 'height': '', 'opts': ''},
    'large': {'verbose_name': 'Large (8 col)', 'width': 680, 'height': '', 'opts': ''},
}
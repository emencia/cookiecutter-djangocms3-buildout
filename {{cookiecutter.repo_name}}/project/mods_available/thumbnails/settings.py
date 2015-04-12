INSTALLED_APPS = add_to_tuple(INSTALLED_APPS, 'easy_thumbnails')

# easy_thumbnails for django_filer
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

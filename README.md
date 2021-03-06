Django Simple News

============================

Installing:

pip install django_simple_news

In settings:

INSTALLED_APPS = (
	...
    'ckeditor',
    'new',
    ...
)

in urls.py
    url(r'^seo_name_for_news/', include('new.urls')),

Configure CKeditor

https://github.com/shaunsephton/django-ckeditor#installation

settings.py

# ckeditor config
CKEDITOR_UPLOAD_PATH = MEDIA_ROOT + '/editor'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [
                    [ 'Source','-','Save','-', 'Cut','Copy','Paste','PasteText','PasteFromWord','-','Undo','Redo', '-', 'Find','Replace','-','SelectAll'], 
                    [ 'Bold','Italic','Underline','Strike','Subscript','Superscript','-','RemoveFormat' ] ,'/',
                    [ 'NumberedList','BulletedList','-','Outdent','Indent','-','Blockquote','CreateDiv','-','JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock','-','BidiLtr','BidiRtl' ], 
                    [ 'Link','Unlink' ],
                    [ 'Image','Table','HorizontalRule','SpecialChar' ],
                    [ 'Format'],
                    [ 'TextColor','BGColor', '-', 'Styles','Format','FontSize' ],
                    [ 'Maximize', 'ShowBlocks','-','About' ],
                ],
        'format_tags': 'p;h1;h2;h3;h4;h5;h6;pre;address;div',
    },
}

Configure easy-thumbnails for each template

# easy-thumbnails config

https://pypi.python.org/pypi/easy-thumbnails/1.2

THUMBNAIL_ALIASES = {
    '': {
        'new_detail': {'size': (50, 50), 'crop': True},
        'new_list': {'size': (152, 152), 'crop': True},
        'new_index': {'size': (960, 1760), 'crop': False, 'upscale': True},
    },
}

You also can overwrite templates:

/templates/new/new_detail.html for new detail
/templates/new/news_index.html for a list of news
/templates/new/news_list.html to get a list of news without a context to get include in custom templates.

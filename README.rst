cmsplugin_blog to multilingual-news
===================================

This app adds datamigrations to switch from cmsplugin-blog_ to
django-multilingual-news_.

.. _cmsplugin-blog: https://github.com/fivethreeo/cmsplugin-blog
.. _django-multilingual-news: https://github.com/bitmazk/django-multilingual-news

It's designed to provide an alternative blog app when updating to django-cms 3
without you losing all your entries.

It will be constantly extended to take more and more addon-apps for
cmsplugin_blog into account.

Currently supported apps:

* cmsplugin-blog-language-publish_
* cmsplugin-blog-cagegories_
* cmsplugin-blog-seo-addons_

.. _cmsplugin-blog-language-publish: https://github.com/bitmazk/cmsplugin-blog-language-publish
.. _cmsplugin-blog-categories: https://github.com/bitmazk/cmsplugin-blog-categories
.. _cmsplugin-blog-seo-addons: https://github.com/bitmazk/cmsplugin-blog-seo-addons

Additional features:

* Automatically switch from `BlogApphook` to `MultilingualNewsApphook`
* Moving content and excerpt placeholders from `cmsplugin_blog.Entry` to
  `multilingual_news.NewsEntry` `excerpt` and `content` fields.
* Recognizes if `hero_slider` has a `Slideritem.content_object` set to a
  `cmsplugin_blog.Entry` and changes it accordingly.

Installation
------------

Before you install this app, make sure, that you have migrated
`cmsplugin_blog` to the latest migration
`0015_auto__add_field_latestentriesplug`, because the datamigration expects at
least this state. Also apply the latest migrations for the "supported apps".

To get the latest stable release from PyPi

.. code-block:: bash

    pip install cmsplugin-blog-to-multilingual-news

To get the latest commit from GitHub

.. code-block:: bash

    pip install -e git+git://github.com/bitmazk/cmsplugin-blog-to-multilingual-news.git#egg=cmsplugin_blog_to_multilingual_news

Add ``cmsplugin_blog_to_multilingual_news`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'cmsplugin_blog_to_multilingual_news',
    )

Remove `cmsplugin_blog` and all supported apps listed above from your
`INSTALLED_APPS`. Otherwise Model validation will probably fail.

Usage
-----

It is probably a good idea to test the migration on a local database first to
make sure, everything worked. You should not run this straight on your live db.

Once all requirements are installed and `INSTALLED_APPS` is properly set,
you just run the migrations.

.. code-block:: bash

    ./manage.py migrate


This would run all migrations for all apps[recommended]. If you only want to
run this app's migration, you should run the separate apps first and then this
one. So minimum would be:

.. code-block:: bash

    ./manage.py migrate cmsplugin_blog
    ./manage.py migrate multilingual_news
    ./manage.py migrate cmsplugin_blog_to_multilingual_news


Be careful when you make the datamigrations, there might not yet be a
backwards migration for some or even all things.


Contribute
----------

If you want to contribute to this project, please perform the following steps

.. code-block:: bash

    # Fork this repository
    # Clone your fork
    mkvirtualenv -p python2.7 cmsplugin-blog-to-multilingual-news
    make develop

    git co -b feature_branch master
    # Implement your feature and tests
    git add . && git commit
    git push -u origin feature_branch
    # Send us a pull request for your feature branch

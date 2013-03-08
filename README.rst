rapidsms-dummydata
==================

``rapidsms-dummydata`` is a simple RapidSMS application to generate data for testing.

Installation
------------

To install and setup ``rapidsms-dummydata``, follow these steps:

1. Use pip to install the application::

    pip install -e git+https://github.com/caktus/rapidsms-dummydata.git#egg=dummydata 

1. Add ``dummydata`` to ``INSTALLED_APPS`` in your settings file::

    INSTALLED_APPS = [
        "dummydata",
    ]

2. Add the ``dummydata`` urls to your urlconf somewhere::

    urlpatterns = patterns('',
        (r'^dummydata/', include('dummydata.urls')),
    )

3. If wanted, add a navigation item to your ``rapidsms/_nav_bar.html`` template::

    {% load url from future %}

    <li><a href="{% url 'generate-contacts' %}">Dummy Data</a></li>

License
-------

django-dummydata is released under the BSD License. See the 
`LICENSE <https://github.com/caktus/rapidsms-dummydata/blob/master/LICENSE>`_ file for more details.

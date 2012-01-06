-----
About
-----

Store an history of model url change

* a manager to register model to survey
* a middleware to intercept http404 and redirect to new url if exists.

------------
Installation
------------

To install the latest stable version::

	pip install -e git+https://github.com/oxys-net/django-historylink.git#egg=django-historylink


You will need to include ``historylink`` in your ``INSTALLED_APPS``::

	INSTALLED_APPS = (
	    ...
	    'historylink',            
	)

You will need to include ``historylink`` in your ``MIDDLEWARE_CLASSES``::

	MIDDLEWARE_CLASSES = (
	    ...
	    'historylink.middleware.HistoryLink',            
	)

-----
Usage
-----

In your models ::

	from historylink.manager import manager
	manager.register(model)
	manager.register([model1, model2])
	manager.register([model1, model2], MyModelManager) # where MyModelManager inherit from manager.ModelManager
	
--------------
Django command
--------------

The command below add HistoryLink object for your existing datas

	./manage.py historylink_sync
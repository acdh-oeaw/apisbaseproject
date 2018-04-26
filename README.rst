Readme
======


Purpose
------------

This project is based upon the APIS (branch dev_0.8_, commit_: ) project and should ease the process to set up and customize a new APIS instance.

Installation
------------

* clone the repo :code:`git clone https://github.com/acdh-oeaw/apisbaseproject.git <folder-name>`
* customize :code:`webpage.metadata`,
* recommended: create a virtual environment
* install requirements :code:`pip install -r requirements.txt`
* in :code:`webpage/static/webpage/libraries` run :code:`bower install`
* before you can run the inital migrations
    * first run :code:`python manage.py delete_migrate --settings=apis.settings.<custom settings file>` to delete any existing migration files.
    * :code:`python manage.py migrate --settings=apis.settings.<custom settings file>` this will create django's default database tables
    * :code:`python manage.py makemigrations --settings=apis.settings.<custom settings file>` this will cretae the migration files for the apis-specific applications.
    * :code:`python manage.py migrate --settings=apis.settings.<custom settings file>` and this will create the according data base tables
* in :code:`apis.urls` UNcomment the commentented the items in the code:`urlpatterns` list
* start the dev-server :code:`python manage.py runserver --settings=apis.settings.<custom settings file>`




original Readme
======

The APIS_ project intents to semantically annotate the Austrian Bibliography Lexicon (ÖBL_). To achieve this goal
we develop(ed) this web-app. It is based on a 5 entities (person, place, institution, event, work) data model.
All 5 entities are connected to each other. Entities, as well as relations between them, can be typed with vocabularies
similar to the Simple Knowledge Organization System (SKOS_).

APIS comes with a built in system of autocompletes that allows researchers to import meta-data of entities with just a
single click. Out of the box APIS supports Stanbol_ as a backend for the autocompletes, but the system is rather easy to
adapt to any Restfull API. APIS also supports the parsing of RDFs_ describing entities into an entity. The parsing is
configured in a settings file.

APIS comes also with a built in highlighter. The highlighter is configured via the built in admin backend and allows
to annotate texts with entities and/or relations between entities.

For a demo of the application please refer to apisdev_.


Installation
------------

The installation process is described in the apis-core docs_.


Licensing
---------

All code unless otherwise noted is licensed under the terms of the MIT License (MIT). Please refer to the file LICENSE in the root directory of this repository.

All documentation and images unless otherwise noted are licensed under the terms of Creative Commons Attribution-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/4.0/


.. _APIS: https://www.oeaw.ac.at/acdh/projects/apis/
.. _apisdev: https://apisdev.acdh.oeaw.ac.at
.. _ÖBL: http://www.biographien.ac.at
.. _SKOS: https://en.wikipedia.org/wiki/Simple_Knowledge_Organization_System
.. _Stanbol: https://stanbol.apache.org/
.. _RDFs: https://en.wikipedia.org/wiki/Resource_Description_Framework
.. _docs: https://acdh-oeaw.github.io/apis-core/
.. _dev_0.8: https://github.com/acdh-oeaw/apis-core/compare/dev_0.8
.. _commit: https://github.com/acdh-oeaw/apis-core/commit/3e026ca3ec187fc14c3f6492ca407d1a7d797026

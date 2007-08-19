pep8 :
	pep8.py --filename=*.py --repeat .

pylint :
	-pylint shotserver04 \
	| grep -v "/tests\.py:" \
	| grep -v "Invalid name \"urlpatterns\"" \
	| grep -v "\.Admin] Missing docstring" \
	| grep -v "\.Admin] Class has no __init__ method" \
	| grep -v "\.Admin] To few public methods" \
	| grep -v "\.Meta] Missing docstring" \
	| grep -v "\.Meta] Class has no __init__ method" \
	| grep -v "\.Meta] To few public methods" \
	| grep -v "Unused argument 'http_request'" \
	| grep -v "Access to a protected member _meta" \
	| grep -v "Undefined variable '_'" \
	| grep -v "E1101" \
	| grep -v "W0142"

docstrings :
	-pylint shotserver04 \
	| grep -v "/tests\.py:" \
	| grep -v "\.Admin] Missing docstring" \
	| grep -v "\.Meta] Missing docstring" \
	| grep "docstring"

doctest :
	grep -rl --include "*.py" "doctest.testmod()" . | xargs -n1 python

headers :
	find -name "*.py" \
	| xargs header.py shotserver04/__init__.py

properties :
	find -name "*.py" | xargs svn propset svn:keywords "Rev Date Author"
	find -name "*.py" | xargs svn propset svn:eol-style native

backup :
	pg_dump shotserver04 | bzip2 \
	> /tmp/shotserver04.`date +%y%m%d-%H%M%S`.sql.bz2

reset : backup
	echo DROP DATABASE shotserver04 | psql template1
	echo CREATE DATABASE shotserver04 | psql template1
	shotserver04/manage.py syncdb

customsql :
	./django_dump.py -p shotserver04 -s shotserver04 \
	Architecture Platform OperatingSystem \
	Javascript Java Flash Engine BrowserGroup

export :
	./django_dump.py -p shotserver04 -o export \
	User Sponsor Factory ScreenSize ColorDepth Browser
	tar -cjf shotserver04.`date +%y%m%d-%H%M%S`.export.tar.bz2 export

import :
	rm -rf export
	tar -xjf shotserver04.export.tar.bz2
	psql shotserver04 < export/auth/user.sql
	psql shotserver04 < export/sponsors/sponsor.sql
	psql shotserver04 < export/factories/factory.sql
	psql shotserver04 < export/factories/screensize.sql
	psql shotserver04 < export/factories/colordepth.sql
	psql shotserver04 < export/browsers/browser.sql

rosetta-import :
	rm -rf rosetta-shotserver
	tar xzvf rosetta-shotserver.tar.gz
	cp rosetta-shotserver/shotserver.pot \
	   shotserver04/locale/en/LC_MESSAGES/django.po
	ls rosetta-shotserver/*.po \
	| xargs -n1 basename | sed s/\\.po// \
	| xargs -iname bash -c " \
		mkdir -p shotserver04/locale/name/LC_MESSAGES ; \
		cp rosetta-shotserver/name.po \
		shotserver04/locale/name/LC_MESSAGES/django.po"

rosetta-export :
	rm -rf rosetta-shotserver
	mkdir rosetta-shotserver
	cp shotserver04/locale/en/LC_MESSAGES/django.po \
	   rosetta-shotserver/shotserver.pot
	ls shotserver04/locale/*/LC_MESSAGES/django.po \
	| grep -v /en/ | cut -d / -f 3 \
	| xargs -iname bash -c " \
		cp shotserver04/locale/name/LC_MESSAGES/django.po \
		rosetta-shotserver/name.po"
	rm rosetta-shotserver.tar.gz
	tar czvf rosetta-shotserver.tar.gz rosetta-shotserver
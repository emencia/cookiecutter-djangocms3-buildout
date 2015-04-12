
.PHONY: help install clean delpyc assets scss syncf5

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo
	@echo "  install -- install foundation5 sources (do not use this)"
	@echo "  update -- update foundation5 sources from the latest release"
	@echo
	@echo "  syncjquery -- update jquery to have correct sources uncompressed instead of foundation5 ones"
	@echo "  syncf5 -- to synchronize needed Javascript files from foundation5 sources dir to the project static files"
	@echo

install:
	cd ../
	foundation new foundation5
	cd foundation5
	
update:
	cd ../
	foundation new foundation5
	cd foundation5
	python fix_dotted_filename.py
	
syncjquery:
	# Remove sources from Foundation
	rm -Rf ./bower_components/jquery
	rm -f ./bower_components/foundation/js/vendor/jquery.js
	# Reinstall jquery sources
	# See ./bower_components/jquery/.bower.json to know what exact version is needed
	bower install jquery#2.1.1
	cp ./bower_components/jquery/dist/jquery.js ./bower_components/foundation/js/vendor/jquery.js

syncf5: syncjquery
	rm -Rf ../project/webapp_statics/js/foundation5
	cp -r ./bower_components/foundation/js ../project/webapp_statics/js/foundation5
	# Cleaning vendor libs
	rm -Rf ../project/webapp_statics/js/foundation5/vendor
	mkdir -p ../project/webapp_statics/js/foundation5/vendor
	# Getting the real sources for updated vendor libs
	cp ./bower_components/fastclick/lib/fastclick.js ../project/webapp_statics/js/foundation5/vendor/
	cp ./bower_components/foundation/js/vendor/jquery.js ../project/webapp_statics/js/foundation5/vendor/
	cp ./bower_components/jquery-placeholder/jquery.placeholder.js ../project/webapp_statics/js/foundation5/vendor/
	cp ./bower_components/jquery.cookie/jquery.cookie.js ../project/webapp_statics/js/foundation5/vendor/
	cp ./bower_components/modernizr/modernizr.js ../project/webapp_statics/js/foundation5/vendor/

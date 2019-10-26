install: install_venv
	install -Dm 755 src/*.py /opt/PopupTranslator/
	install -Dm 755 src/icon.png /opt/PopupTranslator/
	install -Dm 755 src/PopupTranslator.desktop /usr/share/applications/

uninstall:
	rm -rf /opt/PopupTranslator/
	rm -f /usr/share/applications/PopupTranslator.desktop

install_venv: requirements.txt
	mkdir -pv /opt/PopupTranslator/
	if [ ! -d /opt/PopupTranslator/venv/ ]; \
	then \
		python3 -m venv /opt/PopupTranslator/venv; \
	fi
	. /opt/PopupTranslator/venv/bin/activate
	/opt/PopupTranslator/venv/bin/pip install --upgrade pip
	/opt/PopupTranslator/venv/bin/pip install -r requirements.txt

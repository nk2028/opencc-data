update\:data:
	mkdir -p ./tmp && rm -Rf tmp/OpenCC-master
	wget https://github.com/BYVoid/OpenCC/archive/refs/heads/master.zip -O tmp/opencc.zip
	unzip tmp/opencc.zip -d tmp/
	cp tmp/OpenCC-master/data/dictionary/* data/
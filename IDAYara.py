# Use Yara without PySide
# Download IDAScope from http://pnx-tf.blogspot.com/2014/02/idascope-v11-yara-scanning.html
# Add this script into same directory with IDAScope.py
# Copy yara.pyd into \IDA\lib
# For Linux please refer to http://secshoggoth.blogspot.com/2014/02/installing-yara-into-ida-pro-64-bit.html

import yara

from idascope.core.YaraScanner import YaraScanner

def main():
	# Insert your own Yara path
	config = "C:\Yara"
	yara_scanner = YaraScanner(config)
	yara_scanner._load_recursive(config)
	yara_scanner.scan()
	
	
if __name__ == "__main__":
	main()

IDAYara
=======
* Using Yara Scan in IDA Pro without PySide
* Download IDAScope from http://pnx-tf.blogspot.com/2014/02/idascope-v11-yara-scanning.html
* Download and install yara-python from https://github.com/plusvic/yara/releases/tag/2.1.0
* Look for your yara library file, mostly located at C:\Python27\Lib\site-packages\yara.pyd and copy it into your IDA\lib folder
* For Linux please refer to http://secshoggoth.blogspot.com/2014/02/installing-yara-into-ida-pro-64-bit.html

-------------------------------------------------------------------------------------------------------------------------
* Get the IDAYara.py from https://github.com/SiowCY/IDAYara/blob/gh-pages/IDAYara.py
* Please ensure your IDAYara.py is same directory with IDAScope.py

-------------------------------------------------------------------------------------------------------------------------
* If you want to show the location of the successful detected address, you may download the edited version YaraScanner.py https://github.com/SiowCY/IDAYara/blob/gh-pages/YaraScanner.py
* The changes are made on _result_callback function. 
* Note the SetColor only are not failed to set color on .text



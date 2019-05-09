The GuideboxAPI library requires at least Python 2.7.9.
Ubuntu ships with Python 2.7.6.  The GuideboxAPI Library will still function, but it will present the error below:

/usr/local/lib/python2.7/dist-packages/urllib3/util/ssl_.py:355: 
SNIMissingWarning: An HTTPS request has been made, but the SNI (Server Name Indication) extension to TLS is not available on this platform. 
This may cause the server to present an incorrect TLS certificate, which can cause validation failures. 
You can upgrade to a newer version of Python to solve this. 
For more information, see https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
  
SNIMissingWarning
/usr/local/lib/python2.7/dist-packages/urllib3/util/ssl_.py:148: InsecurePlatformWarning: A true SSLContext object is not available. 
This prevents urllib3 from configuring SSL appropriately and may cause certain SSL connections to fail. You can upgrade to a newer version of Python to solve this. 
For more information, see https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
  InsecurePlatformWarning


In order to use the GuideBoxAPI without error install Python 2.7.9 or newer by copying and pasting the commands below:

sudo pip install --upgrade guidebox
sudo add-apt-repository ppa:jonathonf/python-2.7 -y
sudo apt-get update
sudo apt-get install python2.7 -y

To check Python version
python --version



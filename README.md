# SharpSpringPython
SharpSpringPython is a Python program that interacts with [SharpSpring's Open API](https://help.sharpspring.com/hc/en-us/articles/115001069228-Understanding-SharpSpring-Open-API-Overview) (RESTful API)

This initial release only makes use of the [getLeads](https://help.sharpspring.com/hc/en-us/articles/360034119252-Understanding-SharpSpring-Open-API-Methods#h_3584177a-f870-44da-aa5a-6bb5b3a7e0d7) Method using the *where* parameter and **emailAddress** type.

Future releases will provide for all SharpSpring API methods.

## Initial Release

In its first release, SharpSpringPython takes a comma-separated list of email addresses, pulls all lead information from your SharpSpring instance on each email address, and provides a CSV file with all of the lead information. Email addresses not found are skipped.  

## Setup

Python 3.x is required. Include pip for required package installation.

```console
$ sudo apt install python3-pip
```
Required non-native package: [pandas](https://pandas.pydata.org/docs/getting_started/install.html).

```console
$ python3 -m pip install pandas
```
## Configuration

Only three lines of configuration are needed:

```python
accountID = ""
secretKey = ""
email_addresses = ""
```
accountID and secretKey are both found in your SharpSpring account API settings.

email_addresses is a comma-separated list of email addresses.

## How to Run

After you've configured the file, run it with Python. After processed, you will find a new data.csv file in the same directory containing all leads.

```console
$ python3 ssp.py
```
```console
$ ls
data.csv  LICENSE  README.md  ssp.py
```
## TODOs

* Error handling
* Accept a csv file for data intake
* Expand Methods

# SharpSpringPython
SharpSpringPython is a Python program that interacts with [SharpSpring's Open API](https://help.sharpspring.com/hc/en-us/articles/115001069228-Understanding-SharpSpring-Open-API-Overview) (RESTful API)

This initial release only makes use of the [getLeads](https://help.sharpspring.com/hc/en-us/articles/360034119252-Understanding-SharpSpring-Open-API-Methods#h_3584177a-f870-44da-aa5a-6bb5b3a7e0d7) Method using the *where* parameter and **emailAddress** type.

Future releases will provide for all SharpSpring API methods.

## Initial Release

In its first release, SharpSpringPython takes a comma-separated list of email addresses, pulls all lead information from your SharpSpring instance on each email address, and provides a CSV file. Email addresses not found are skipped.  

## Setup

The following non-native packages are required: [requests](https://github.com/psf/requests) and [pandas](https://pandas.pydata.org/docs/getting_started/install.html).

The installation may differ depending on your environment.

**Requests**
```console
$ python -m pip install requests
```
**Pandas**
```console
$ pip install pandas
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

After you've configured the file, simply call the file with Python. After processed, you will find a data.csv file containing all leads.

```console
$ python ssp.py
```
```console
$ ls
data.csv    ssp.py
```
## TODOs

* Error handling
* Accept a csv file for data intake
* Expand Methods

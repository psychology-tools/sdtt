# Structed Data Testing Tool - Local CLI Bridge
A simple bridge for sending development (local only) webserver page contents to Google's *(soon to be Schema.org's)* [Structured Data Testing Tool](https://search.google.com/structured-data/testing-tool) via command line.

## What is Does
 - Downloads the contents of a given URL (from a regular/public or local host)
 - Posts the encoded contents as a "code snippet" to the [SDTT](https://search.google.com/structured-data/testing-tool#new-test-code-tab)
 - Parses and displays results
 
## Requirements
 - [requests](https://github.com/psf/requests.git) module *(install with `python -m pip install requests`)*

## Usage Example
`./sdtt.py` `"http://localhost:8888/page/to/test"`

## Example Output
By default the script just prints a summary of the number of structures found, warnings, and errors. It also loops through each warning and error in the list and prints out the section of the submitted page code that contains the error.

```
-----SUMMARY-----
Structures: 4
Errors: 1
Warnings: 0

-----ERROR (#0)-----
<meta itemprop="pmid" content="7080884" />
```

## Hacking On / Running Interactively
The full results are available as a dictionary object variable named `data` with the following structure:

```
'data': {
  'isRendered': (bool),
  'tripleGroups': (list of triple), 
  'numObjects': (int),
  'html': (string),
  'errors': (list of dicts),
  'totalNumErrors': (int),
  'totalNumWarnings': (int)
}
```

You can manipulate the `data` variable interactively by running `python3 -i ./sdtt.py "http://your.url/here"`, or dump the entire data response as JSON by commenting out the last line.


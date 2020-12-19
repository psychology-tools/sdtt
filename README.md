# Structed Data Testing Tool - CLI
A simple bridge for sending development (local only) webserver page contents to Google's *(soon to be Schema.org's)* [Structured Data Testing Tool](https://search.google.com/structured-data/testing-tool) via command line.

Both the Bash and Python versions perform the same tasks:
 - Download a given URL (from a regular/public or local host)
 - Post the encoded contents as a "code snippet" to the [SDTT](https://search.google.com/structured-data/testing-tool#new-test-code-tab)
 - Parse and display results as JSON or in a new browser tab
 
## Python Verison
 - **Requires:** the [requests](https://github.com/psf/requests.git) module (install with `python -m pip install requests`)
 - **Usage:** `./sdtt.py http://localhost:8888/page/to/test`

## Bash Version
 - **Requires:** [curl](https://github.com/curl/curl) binary *(see below for installing curl)*
 - **Usage:** `./sdtt.sh http://localhost:8888/page/to/test`
 
### Installing Curl
Your distribution probably already has `curl` on it, but if it doesn't you can install it with the following commands:
 - Debian and friends: `sudo apt-get install curl` 
 - Arch and Manjaro: `sudo pacman -S curl`
 - Redhat and CentOS: `sudo yum install curl`
 - MacOSX: *(should just be on there)*
 - Windows: *(idk, use the python verison)*
 
 

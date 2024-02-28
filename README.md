
OpenRedirect Checker is a tool for identifying potentially vulnerable URLs for open redirect attacks
## How it Works

The tool works by first fetching URLs from the  domain. It then sends HEAD requests to each URL and checks if any redirects to a specified malicious domain (e.g., 'evil.com') are present in the response headers.

## Setup


git clone https://github.com/abhinav066/openredirect.git
   
pip install -r requirements.txt

python openredirect.py


The tool will fetch URLs from the Wayback Machine and check each URL for potential vulnerabilities. Results will be displayed in the terminal.

Example
bash
Copy code
Enter a domain: example.com
Fetching URLs: 100%|██████████████████████████████████| 1000/1000 [00:05<00:00, 200.00URL/s]
Credits
This tool was created by Abhinav066  > Abhinav Nath.v
instagram @abhinav.ser
linkedin  www.linkedin.com/in/abhinavnathv

# Hound-Sniffer
<img width="766" src="https://github.com/user-attachments/assets/10de194d-7143-4946-9d91-455a63e54690">

# Overview
Hound-Sniffer is a username reconnaissance and OSINT tool designed to search for usernames across multiple platforms and perform search engine dorking. It generates HTML reports to display the results in an interactive and user-friendly format.

# Types of searches
* Platform Search: General search for usernames on platforms defined in platforms.txt.
* Dorking search:  Perform search engine queries on platforms like Google, Bing, and DuckDuckGo.

# Features
* Multi-threading: Quickly scans multiple platforms using threads for better performance.
* Customizable User-Agent Headers: Rotates through user agents to avoid detection or rate limiting.
* Customizable Platform searches with .txt file
* Professional HTML Reports
 
    
<img width="1440" src="https://github.com/user-attachments/assets/0f9e62c8-255e-4b14-a87b-6e1eb0bfa894">


# Prerequisites
pip install -r requirements.txt
* Python 3.6 or higher
* requests
* Colorama

# Customization:
* To add/remove platforms open the platforms.txt file. Each line should define a platform and its URL format:
e.x:
  - GitHub,https://github.com/{username}
  - Twitter,https://twitter.com/{username}
  - Reddit,https://www.reddit.com/user/{username}

# How To Run the script
Run the tool by executing the following command:
1. navigate to hound_sniffer.py directory
2. run 'python3 hound_sniffer.py'
3. Follow the on-screen prompts

# License
This tool is licensed under the MIT License. See the LICENSE file for details.

# Legal
Hound-Sniffer is for legal and ethical use only. It is the responsibility of the user to ensure compliance with all applicable laws and regulations. Misuse of this tool for illegal activities is strictly prohibited.


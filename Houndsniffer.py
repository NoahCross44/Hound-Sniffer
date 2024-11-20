import random
import requests
from colorama import Fore, Style, init
from threading import Thread, Lock

init(autoreset=True)

ascii_art = """
CAUTION.You are responsible for your actions. Developers assume no liability
++++;;;;;;;;::::::::::::::::::::::::::::::::::**:::::::::::::::::::::::;;;;;
+++++++;;;;;;;;;;:::;?%%%%+:;;;;::::;;::::::::;S%;:::;;;::::::::;;;:;;;;;;;;
;++;;;;;;;;;;;;::+S##@@@@@#+::::::::::::::::::::%S;::::::::::::::::::;;;;;;;
;;;;;;;;;;;;;;;:;S@@@@@@@@@+::::::::::::::::::::%#;::::::::::::;:;;;;;;;;;;;
;;;;;;;;;;;;;;:::::*SS@@@@@@#:,:::::::::::::::::::%S:::::::::::::::::::;;;;;
;;;;;;::::::::::::,,,;@@@@@@@S*;::;;;;;;;;;;;;;;;;*@:::::::::::::::::::;;;;;
;+;;;;;;;::::::::::::S@%#@@@@@@@#S%%??;;;;;;;;;::;#S::::::::::::::::::;;;;;;
;;;;;;;;:::::::::::::*?:%@@@@@@@@@@@@@@@@@@@@@@#S@#+::::::::::::::::::::;;;;
;;;;::::::::::::::::::::S@@@@@@@@@@@@@@@@@@@@@@@@@#:,,,,::::::::::::;:;;::;;
+++;;;;;;;;;;;::::;;;:::?@@@@@@@@@@@@@@@@@@@@@@@@@@S:::::::::;;;;:::::;;;;;;
;;;;;;;;;;;;;:;;:::::::::?@@@@@@@@@@@@@@@@@@@@@@@@@#:::::::::::::::;;;;;;;;;
;::::;;;;::::::::::::::,,,+@@@@@@@@@@#S%?**?@@@@@@@#:,,,,:::::::::::;;;;;;;;
;;;HOUND SNIFFER:::;:::::::%@@@@@@*+;;;:::::?#@@@@@@%::::::;;:::;;;;;;;;;;;;
;;;Author:NoahCross44::::::+@@S@@#::::::::,,,:%@@@@@@*,::::::::::::::::::;;;
;;;Version:0.0.1::::::::::::S@?#@%:::::::::::,,;%@@@@@?:,:::::::::::::::::;;
;;;;;;::::::::::::::::::::::?@*%@%:::::::::::::,,+#@SS@#+:::::::::::;;;;;;;;
;;:::::::::::::::::::::::::,*@**@?::::,,,,,,,,::::+@%:S@%::::::::::::::::::;
;;:::::::::::::::::::::::::,?@*%@?,:::::::,::::::::S@;:S#;:::::::::::::;;;;;
;;;;;;;;;:::::::::::::::::*%@@%@S::::::::::::::::;%#S;:S@%:::::::::;;;;;;;;;
;;;;;;::::::::::::::::::::++*%%?;:::::::::::::::,,:::,:*?+::::::::::::;;;;;;

"""

def print_welcome_screen():
    print(ascii_art)

class UsernameSearch:
    def __init__(self):
        self.Platform = self.load_platforms("platforms.txt")  # Always open "platforms.txt"
        self.UserAgents = [
    # Windows Browsers
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/116.0.5845.111 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:116.0) Gecko/20100101 Firefox/116.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Edge/18.18362 Safari/537.36",
    # macOS Browsers
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_2_1) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/116.0.5845.111 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13.2; rv:116.0) Gecko/20100101 Firefox/116.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_2_1) AppleWebKit/605.1.15 "
    "(KHTML, like Gecko) Version/16.3 Safari/605.1.15",
    # Linux Browsers
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/116.0.5845.111 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64; rv:116.0) Gecko/20100101 Firefox/116.0",
    # Mobile Browsers - Android
    "Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/116.0.5845.111 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 6) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/116.0.5845.111 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Mi 11) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/116.0.5845.111 Mobile Safari/537.36",
    # Mobile Browsers - iOS
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 "
    "(KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 16_6 like Mac OS X) AppleWebKit/605.1.15 "
    "(KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1",
    ]
        self.Lock = Lock()

    def load_platforms(self, file_path):
        platforms = {}
        try:
            with open(file_path, "r") as file:
                for line in file:
                    line = line.strip()
                    if not line or line.startswith("#"):
                        continue
                    platform, url = line.split(",", 1)
                    platforms[platform.strip()] = url.strip()
        except FileNotFoundError:
            print(f"{Fore.RED}Platform file '{file_path}' not found. Exiting.{Style.RESET_ALL}")
            exit(1)
        return platforms

    def get_headers(self):
        return {"User-Agent": random.choice(self.UserAgents)}

    def verify_url(self, url):
        try:
            response = requests.get(url, headers=self.get_headers(), timeout=5)
            return response.status_code == 200
        except requests.RequestException:
            return False

    def threaded_search(self, platform, base_url, username, valid_profiles):
        full_url = f"{base_url}{username}"
        print(f"{Fore.CYAN}Checking: {full_url}")
        if self.verify_url(full_url):
            with self.Lock:
                valid_profiles[platform] = full_url

    def perform_dorking(self, username):
        quoted_username = f'"{username}"'
        search_engines = {
            "Google": f"https://www.google.com/search?q={quoted_username}",
            "Bing": f"https://www.bing.com/search?q={quoted_username}",
            "DuckDuckGo": f"https://duckduckgo.com/?q={quoted_username}",
            "Yahoo": f"https://search.yahoo.com/search?p={quoted_username}",
            "Yandex": f"https://yandex.com/search/?text={quoted_username}",
        }
        results = {}
        print(f"{Fore.BLUE}\nPerforming dorking for username '{username}':{Style.RESET_ALL}")
        for engine, query_url in search_engines.items():
            print(f"{Fore.YELLOW}{engine}: {query_url}{Style.RESET_ALL}")
            results[engine] = query_url
        return results

    def generate_middle_variations(self, username):
        variations = set([username])
        length = len(username)
        middle = length // 2
        for i in range(max(1, middle - 2), min(length, middle + 2)):
            variations.add(username[:i] + "." + username[i:])
            variations.add(username[:i] + "_" + username[i:])
        return list(variations)

    def generate_leet_variations(self, username):
        leet_map = {
            'a': ['4', '@'],
            'e': ['3'],
            'i': ['1', '!'],
            'o': ['0'],
            's': ['$', '5'],
            't': ['7']
        }
        variations = set([username])
        for i, char in enumerate(username):
            if char.lower() in leet_map:
                for replacement in leet_map[char.lower()]:
                    variations.add(username[:i] + replacement + username[i + 1:])
        return list(variations)

    def search_user(self, username, include_variations=False, include_leet=False):
        threads = []
        valid_profiles = {}
        usernames_to_search = [username]

        if include_variations:
            usernames_to_search.extend(self.generate_middle_variations(username))
        if include_leet:
            usernames_to_search.extend(self.generate_leet_variations(username))
        
        usernames_to_search = list(set(usernames_to_search))

        # Perform threaded search across platforms
        for platform, base_url in self.Platform.items():
            for user in usernames_to_search:
                thread = Thread(target=self.threaded_search, args=(platform, base_url, user, valid_profiles))
                threads.append(thread)
                thread.start()

        # Wait for all threads to finish
        for thread in threads:
            thread.join()

        return valid_profiles  

    def save_to_html(self, username, results, dorking_results=None, variations=None, leet_variations=None):
        html_template = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Username Search Results for {username}</title>
            <!-- Google Fonts -->
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Open+Sans&display=swap" rel="stylesheet">
            <style>
                body {{
                    font-family: 'Open Sans', Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #f0f4f4;
                    color: #333;
                }}
                header {{
                    background-color: #ffffff;
                    padding: 20px;
                    text-align: center;
                    border-bottom: 2px solid #4caf50; /* Green accent */
                }}
                .ascii-art {{
                    font-family: monospace;
                    font-size: 10px;
                    line-height: 1;
                    white-space: pre;
                    display: inline-block;
                    margin: 0 auto;
                    color: #4caf50; /* Green color for ASCII art */
                }}
                .content {{
                    padding: 20px;
                    max-width: 800px;
                    margin: 0 auto;
                }}
                h1 {{
                    text-align: center;
                    color: #2e7d32; /* Darker green */
                    margin-bottom: 20px;
                }}
                h2 {{
                    color: #2e7d32; /* Darker green */
                    border-bottom: 2px solid #4caf50;
                    padding-bottom: 10px;
                }}
                ul {{
                    list-style: none;
                    padding: 0;
                }}
                li {{
                    margin-bottom: 10px;
                    font-size: 16px;
                }}
                a {{
                    color: #1E90FF;
                    text-decoration: none;
                }}
                a:hover {{
                    text-decoration: underline;
                }}
                table {{
                    width: 100%;
                    border-collapse: collapse;
                    margin-top: 20px;
                }}
                th, td {{
                    text-align: left;
                    padding: 12px;
                    border-bottom: 1px solid #ddd;
                }}
                th {{
                    background: #e8f5e9; /* Light green background */
                    font-weight: bold;
                }}
                tr:hover {{
                    background-color: #f1f1f1;
                }}
                footer {{
                    text-align: center;
                    padding: 10px;
                    background-color: #ffffff;
                    border-top: 2px solid #4caf50;
                    font-size: 12px;
                    color: #555;
                    position: fixed;
                    bottom: 0;
                    width: 100%;
                }}
            </style>
        </head>
        <body>
            <header>
                <div class="ascii-art">
{ascii_art}
                </div>
            </header>
            <div class="content">
                <h1>Search Results for '{username}'</h1>
                <div class="results">
            """

        if results:
            html_template += """
                    <h2>Platform Results</h2>
                    <table>
                        <thead>
                            <tr>
                                <th>Platform</th>
                                <th>URL</th>
                            </tr>
                        </thead>
                        <tbody>
            """
            for platform, url in results.items():
                html_template += f"<tr><td>{platform}</td><td><a href='{url}' target='_blank'>{url}</a></td></tr>"
            html_template += "</tbody></table>"

        if dorking_results:
            html_template += """
                    <h2>Dorking Results</h2>
                    <table>
                        <thead>
                            <tr>
                                <th>Search Engine</th>
                                <th>Query URL</th>
                            </tr>
                        </thead>
                        <tbody>
            """
            for engine, url in dorking_results.items():
                html_template += f"<tr><td>{engine}</td><td><a href='{url}' target='_blank'>{url}</a></td></tr>"
            html_template += "</tbody></table>"

        if variations:
            html_template += """
                    <h2>Generated Variations</h2>
                    <ul>
            """
            for var in variations:
                html_template += f"<li>{var}</li>"
            html_template += "</ul>"

        if leet_variations:
            html_template += """
                    <h2>Leet-Speak Variations</h2>
                    <ul>
            """
            for var in leet_variations:
                html_template += f"<li>{var}</li>"
            html_template += "</ul>"

        html_template += f"""
                </div>
            </div>
            <footer>
               You are responsible for your actions. Developers assume no liability and are not responsible for any misuse or damage. 
            </footer>
        </body>
        </html>
        """

        filename = f"{username}_results.html"
        with open(filename, "w") as file:
            file.write(html_template)
        print(f"{Fore.GREEN}Results saved to {filename}.")

def main():
    print_welcome_screen()
    username_search = UsernameSearch()

    username = input(f"{Fore.YELLOW}Enter username: {Style.RESET_ALL}").strip()
    include_variations = input(f"{Fore.YELLOW}Include variations? (y/n): {Style.RESET_ALL}").lower() == 'y'
    include_leet = input(f"{Fore.YELLOW}Include leet variations? (y/n): {Style.RESET_ALL}").lower() == 'y'
    perform_dorking = input(f"{Fore.YELLOW}Perform dorking? (y/n): {Style.RESET_ALL}").lower() == 'y'

    variations = username_search.generate_middle_variations(username) if include_variations else []
    leet_variations = username_search.generate_leet_variations(username) if include_leet else []
    results = username_search.search_user(username, include_variations, include_leet)
    dorking_results = username_search.perform_dorking(username) if perform_dorking else None

    username_search.save_to_html(username, results, dorking_results, variations, leet_variations)

if __name__ == "__main__":
    main()

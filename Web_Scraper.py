import requests
from bs4 import BeautifulSoup
import os

def scrape_url(url_or_ip, output_file):
    try:
        response = requests.get(url_or_ip)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')

        with open(output_file, 'w') as file:
            for link in links:
                file.write(link.get('href') + '\n')

        os.chmod(output_file, 0o666)
    
    except Exception as e:
        print(f'Error: {e}')

def main():
    
    url_or_ip = input("Enter your URL or IP :")
    output_file = input("Please enter the path to save the output (including the file name) :")
    
    
    
    scrape_url(url_or_ip, output_file)

if __name__ == '__main__':
    main()
import requests
from bs4 import BeautifulSoup
import os
# URL of the webpage to scrape
url = "https://www.screener.in/company/PIIND/consolidated/"
# Send an HTTP GET request to the URL
response = requests.get(url)
if response.status_code == 200:
    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.content, "html.parser")
    # Find the target div element
    target_div = soup.find("div", class_="documents concalls flex-column")
    # Find all the links to PPT files within the target div
    ppt_links = target_div.find_all("a", class_="concall-link")
    # Specify the directory where you want to save the downloaded PPT files
    download_dir = r"./"  # Replace with your desired local directory path
 # Replace with your desired directory path
    # Create the directory if it doesn't exist
    os.makedirs(download_dir, exist_ok=True)
    # Download the PPT files
    for link in ppt_links:
        if link.text.strip() == "PPT":
            ppt_url = link["href"]
            ppt_filename = ppt_url.split("/")[-1]
            ppt_filepath = os.path.join(download_dir, ppt_filename)
            ppt_response = requests.get(ppt_url)
            if ppt_response.status_code == 200:
                with open(ppt_filepath, "wb") as ppt_file:
                    ppt_file.write(ppt_response.content)
                print(f"Downloaded: {ppt_filepath}")
            else:
                print(f"Failed to download: {ppt_url}")
else:
    print("Failed to fetch the webpage")
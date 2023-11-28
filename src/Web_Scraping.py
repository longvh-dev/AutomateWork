# Extracting Data from a Website
def scrape_data(url):
    import requests
    from bs4 import BeautifulSoup
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')


# Downloading Images in Bulk
def download_images(url, save_directory):
    import requests
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Unable to get URL: {}".format(response.status_code))

    images = response.json()  # Assuming the API returns a JSON array of image URLs

    for index, image_url in enumerate(images):
        image_response = requests.get(image_url)
        if image_response.status_code != 200:
            raise Exception("Unable to download image: {}".format(image_response.status_code))

        with open(f"{save_directory}/image_{index}.jpg", "wb") as f:
            f.write(image_response.content)


# Automating Form Submissions
def submit_form(url, form_data):
    import requests
    response = requests.post(url, data = form_data)
    if response.status_code == 200:
        print("Form successfully submitted")
        # Do something with the response

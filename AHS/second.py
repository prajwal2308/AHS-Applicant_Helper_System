from flask import Blueprint, render_template
import requests

second = Blueprint("second", __name__, static_folder="static", template_folder="templates")


@second.route("/", methods=["POST", "GET"])
def scrape_google_jobs():
    #api_key = '' Replace with your Google Search API key
    #cx = ''  # Replace with your Custom Search Engine (CX) ID
    with open('static/uploads/Rskills.txt', 'r') as file:
        queries = file.readlines()

    job_links = []
    titles = []

    for query in queries:
        query = query.strip() + " job for freshers in India"

        try:
            # Prepare the API request URL
            url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q={query}&num=2"

            # Send a GET request to the API
            response = requests.get(url)
            response.raise_for_status()

            # Parse the JSON response
            data = response.json()

            # Extract job links from the response
            if 'items' in data:
                for item in data['items']:
                    title = item['title']
                    url = item['link']
                    job_links.append({'title': title, 'url': url})
                    titles.append(title)
        except:
            pass
   
    with open('static/uploads/job_data.txt', 'w') as outfile:
        for job in job_links:
            outfile.write(f"Title: {job['title']}\n")
            outfile.write(f"URL: {job['url']}\n\n")
    

    return render_template('scraped.html', titles=titles, links=job_links)

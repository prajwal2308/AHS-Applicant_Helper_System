

# AHS – Applicant Helper System

**AHS (Applicant Helper System)** is a Flask-based web application that simulates an Applicant Tracking System (ATS). It leverages Natural Language Processing (NLP) techniques to extract and analyze skills from resumes, compares them with job descriptions (JDs), and provides a match score to assist job-seekers and applicants in evaluating compatibility.

## Features

- **User Authentication**: Secure login and registration system for users.
- **Resume and JD Upload**: Upload resumes and job descriptions in various formats for analysis.
- **Skill Extraction**: Utilizes NLP to extract core and soft skills from uploaded documents.
- **Skill Comparison**: Compares extracted skills from resumes and JDs to calculate a match score.
- **Job Scraping**: Scrapes job listings based on extracted skills to provide relevant opportunities.
- **User-Friendly Interface**: Intuitive UI for easy navigation and interaction.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/prajwal2308/AHS-Applicant_Helper_System.git
   cd AHS-Applicant_Helper_System
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   flask run
   ```

   The application will be accessible at `http://127.0.0.1:5000/`.

## Usage

1. **Register/Login**: log in to access the application's features usn: admin and password: admin.
2. **Upload Documents**: Navigate to the upload page to submit your resume and job description.
3. **Analyze Skills**: The application will extract and display core and soft skills from both documents.
4. **View Match Score**: Compare the extracted skills to see how well the resume matches the job description.
5. **Explore Job Opportunities**: Use the job scraping feature to find relevant job listings based on your skills.(blocked)

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **NLP Libraries**: spaCy, NLTK
- **Web Scraping**: BeautifulSoup, Requests
- **Database**: SQLite [No Database included]

## Project Structure

```
AHS-Applicant_Helper_System/
├── main.py
├── second.py
├── third.py
├── templates/
│   ├── login.html
│   ├── upload.html
│   ├── display.html
│   └── scrape.html
├── static/
│   ├── css/
│   └── js/
├── models/
│   └── user.py
├── utils/
│   ├── skill_extractor.py
│   └── job_scraper.py
├── requirements.txt
└── README.md
```

## Contribution


## Acknowledgements

- Inspired by the need to automate and improve the recruitment process.
- Utilizes open-source libraries and tools for NLP and web development.

# ATS3

This is a checkpoint of project till the extraction of skills page and it is more accurate compared to many code.

1. Login Page/Register Page
	-Helps user to register and login

2. Home Page with only function of scan resume. (One page can be reduced and placed in homepage itself)
	-It just redirects the page to upload page with a button click.

3. Upload page (has both resume upload and JD upload)
	-It takes input of Resume and JD and onclick it function on extraction.

4. Display page (displays what skills found in resume and JD)
	-It display core skills
	-It displays Soft skills
	-It displays Text of Resume
	-It has other redirection for job scraping and Comparison.

5. Scrape page ( Scrapes link for keywords found in Resume)
	-It scrapes the links for the skills that are found in resume 

6. Compare JD and Resume ( Under development).
	- we need a pie chart for match Rate.
	-we need what needs to be updated in Resume
	-we need the only skills that are matched b/w them.
	-we need to find education match
	-we need to find experince match.
	-we need to extract contact details.



WHY US AHS:
1. We are Rapid. Compare website and speed of us . We are very quick in Extraction Skills.
2. We are Free to N number of resume scans. 
3. We are Open sourced.
4. Very User Friendly.
5. Wide range of skills extraction.
6. We got Pictorial Representation.
7. we suggest direct links for the particular job roles mentionded in resume.





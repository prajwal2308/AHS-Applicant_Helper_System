from flask import Blueprint, render_template
import io
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import re

third=Blueprint("third",__name__,static_folder="static",template_folder="templates")
@third.route("/",methods=["POST","GET"])

def common():
    file_list = ["static/uploads/Rmerged.txt", "static/uploads/JDmerged.txt"]
    resume_text = ""
    skills_set1 = set()

    for file_name in file_list:
        with open(file_name, 'r') as file:
            if file_name == "static/uploads/Rmerged.txt":
                resume_text = file.read()
            else:
                skills_list = [line.strip() for line in file.readlines()]
                pattern = re.compile("|".join(map(re.escape, skills_list)), re.IGNORECASE)
                matches = re.findall(pattern, resume_text.upper())
                skills_set1.update(matches)

    with open("static/uploads/Common.txt", "w") as f:
        for skill in skills_set1:
            f.write(skill + "\n")
    total_skills_file1 = len(set([line.strip() for line in open(file_list[0], 'r')]))
    match_rate = len(skills_set1) / total_skills_file1 * 100
    match_rate = round(match_rate)
    #total_skills = len(skills_set1)
    #match_rate = total_skills / len(file_list) * 100
    
    print(match_rate)
    with open('static/uploads/Common.txt','r') as f:
                    Cskills=f.read()
    
    sfile_list = ["static/uploads/Rsoftskills.txt", "static/uploads/Jsoftskills.txt"]
    sresume_text = ""
    sskills_set1 = set()

    for sfile_name in sfile_list:
        with open(sfile_name, 'r') as sfile:
            if sfile_name == "static/uploads/Rsoftskills.txt":
                sresume_text = sfile.read()
            else:
                sskills_list = [line.strip() for line in sfile.readlines()]
                spattern = re.compile("|".join(map(re.escape, sskills_list)), re.IGNORECASE)
                smatches = re.findall(spattern, sresume_text.upper())
                sskills_set1.update(smatches)
    print(sskills_set1)
    

    total_skills_file1 = len(set([line.strip() for line in open(sfile_list[0], 'r')]))
    smatch_rate = len(sskills_set1) / total_skills_file1 * 100
    smatch_rate = round(smatch_rate)
    
    #Hard skills rate
    
    hfile_list = ["static/uploads/Rskills.txt", "static/uploads/Jskills.txt"]
    hresume_text = ""
    hskills_set1 = set()

    for hfile_name in hfile_list:
        with open(hfile_name, 'r') as hfile:
            if hfile_name == "static/uploads/Rskills.txt":
                hresume_text = hfile.read()
            else:
                hskills_list = [line.strip() for line in hfile.readlines()]
                hpattern = re.compile("|".join(map(re.escape, hskills_list)), re.IGNORECASE)
                hmatches = re.findall(hpattern, hresume_text.upper())
                hskills_set1.update(hmatches)

    htotal_skills_file1 = len(set([line.strip() for line in open(hfile_list[0], 'r')]))
    hmatch_rate = len(hskills_set1) / htotal_skills_file1 * 100
    hmatch_rate = round(hmatch_rate)

    print("Match Rate: ", hmatch_rate)
    print("Extracted Skills: ", hskills_set1)

    resume_text = ""

# Read resume text from a text file
    file_path = 'static/uploads/Resumewords.txt'
    try:
        with open(file_path, 'r') as file:
            resume_text = file.read()
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        exit()

    phone_number = re.search(r'\d{10}', resume_text)
    email_match = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', resume_text)

    email = email_match.group(0) if email_match else None

    if phone_number:
        phone_number = phone_number.group(0)
        print("Phone number:", phone_number)
    else:
        print("Phone number not found in the resume.")

    if email:
    # Remove the trailing "Email" text from the email string
        email = email.replace("Email", "")
        print("Email:", email)
    else:
        print("Email not found in the resume.")

    
    with open("static/uploads/Rskills.txt", "r") as f:
        RSkills = f.read()
    with open('static/uploads/Jskills.txt','r') as f:
        JDtext11=f.read()
    with open('static/uploads/Jsoftskills.txt','r') as f:
        JDsoft=f.read() 
    with open('static/uploads/Rsoftskills.txt','r') as f:
        Rsoft=f.read()
        
    word_count = len(resume_text)
    patternL = r"\b(\d+)[+\s]*(?:years?|yrs?)\b"
    matchesL = re.findall(patternL, resume_text, re.IGNORECASE)

    if matchesL:
        print("Years of experience found in the resume:")
        for years in matchesL:
            print("- " + years)
            job_level_match= years+ "Experience"
    else:
        print("No years of experience found in the resume.")
        job_level_match = "Fresher"
    
    
    return render_template('compare.html',Cskills=Cskills,match_rate=match_rate,smatch_rate=smatch_rate,hmatch_rate=hmatch_rate,
                           Rskills=RSkills,JDskills=JDtext11,JDsoft=JDsoft,Rsoft=Rsoft,Phno=phone_number,email=email,wc=word_count,JLM=job_level_match)
'''
def softcommon():
    sfile_list = ["static/uploads/Rsoftskills.txt", "static/uploads/Jsoftskills.txt"]
    sresume_text = ""
    sskills_set1 = set()

    for sfile_name in sfile_list:
        with open(sfile_name, 'r') as sfile:
            if sfile_name == "static/uploads/Rsoftskills.txt":
                sresume_text = sfile.read()
            else:
                sskills_list = [line.strip() for line in sfile.readlines()]
                spattern = re.compile("|".join(map(re.escape, sskills_list)), re.IGNORECASE)
                smatches = re.findall(spattern, sresume_text.upper())
                sskills_set1.update(smatches)
    print(sskills_set1)
    print(smatch_rate)

    total_skills_file1 = len(set([line.strip() for line in open(sfile_list[0], 'r')]))
    smatch_rate = len(sskills_set1) / total_skills_file1 * 100
    smatch_rate = round(smatch_rate)
    
    return render_template('compare.html',smatch_rate=smatch_rate)
    
    '''
'''
def chart():
    with open('static/uploads/Rmerged.txt', 'r') as f1:
        lines1 = set(f1.readlines())

    # Read the contents of the second file
    with open('static/uploads/JDmerged.txt', 'r') as f2:
        lines2 = set(f2.readlines())

    # Find the matching lines
    matching_lines = lines1.intersection(lines2)

    # Print the matching lines
    print("Matching lines:")
    for line in matching_lines:
        print(line.strip())
    
    with open('static/uploads/Allcommon.txt', 'w') as out_file:
        for line in matching_lines:
            out_file.write(line)

    
    return render_template('compare.html')'''
'''

def common():
    file_list = ["static/uploads/Rmerged.txt", "static/uploads/JDmerged.txt"]
    with open("static/uploads/Common.txt", "w") as f:
        skills_set1 = set()
        resume_text = ""

    for file_name in file_list:
        with open(file_name, 'r') as file:
            if file_name == "static/uploads/JDmerged.txt":
                resume_text = file.read()
            else:
                skills_list = [line.strip() for line in file.readlines()]
                pattern = re.compile("|".join(map(re.escape, skills_list)), re.IGNORECASE)
                matches = re.findall(pattern, resume_text.lower())
                skills_set1.update(matches)

    print("Extracted Skills: ", skills_set1)
    with open("static/uploads/Common.txt", "w") as f:
        for skill in skills_set1:
            f.write(skill.upper() + "\n")
    return render_template('compare.html', comm=skills_set1)
def score():
    with open("Rskills.txt", "r") as f:
        resume_text = f.read()
    with open("jdskills.txt", 'r') as f:
        skills_list = [line.strip() for line in f.readlines()]
    pattern = re.compile("|".join(map(re.escape, skills_list)), re.IGNORECASE)
    matches = re.findall(pattern, resume_text.lower())
    skills_set = set(matches)
    print("#Common skills presnt in both of them: ", skills_set)
    lines1=0
    for line in skills_set:
        lines1+=1
    print(lines1)

    lines2=0
    for line in skills_list:
        lines2+=1
    print(lines2)

#percentage or ration
    c=(lines1/lines2)*100
    print(round(c))
    return render_template('compare.html',lines1=lines1,lines2=lines2)
    '''
from flask import Blueprint, render_template
import io
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import re
import os

third = Blueprint("third", __name__, static_folder="static", template_folder="templates")

@third.route("/", methods=["POST", "GET"])
def common():
    base_path = os.path.dirname(__file__)
    file_list = [
        os.path.join(base_path, "static", "uploads", "Rmerged.txt"),
        os.path.join(base_path, "static", "uploads", "JDmerged.txt")
    ]

    resume_text = ""
    skills_set1 = set()

    for file_name in file_list:
        with open(file_name, 'r') as file:
            if "Rmerged.txt" in file_name:
                resume_text = file.read()
            else:
                skills_list = [line.strip() for line in file.readlines()]
                pattern = re.compile("|".join(map(re.escape, skills_list)), re.IGNORECASE)
                matches = re.findall(pattern, resume_text.upper())
                skills_set1.update(matches)

    common_path = os.path.join(base_path, "static", "uploads", "Common.txt")
    with open(common_path, "w") as f:
        for skill in skills_set1:
            f.write(skill + "\n")

    total_skills_file1 = len(set([line.strip() for line in open(file_list[0], 'r')]))
    match_rate = round((len(skills_set1) / total_skills_file1) * 100)

    print("Match Rate:", match_rate)

    with open(common_path, 'r') as f:
        Cskills = f.read()

    # Soft skills comparison
    sfile_list = [
        os.path.join(base_path, "static", "uploads", "Rsoftskills.txt"),
        os.path.join(base_path, "static", "uploads", "Jsoftskills.txt")
    ]

    sresume_text = ""
    sskills_set1 = set()

    for sfile_name in sfile_list:
        with open(sfile_name, 'r') as sfile:
            if "Rsoftskills.txt" in sfile_name:
                sresume_text = sfile.read()
            else:
                sskills_list = [line.strip() for line in sfile.readlines()]
                spattern = re.compile("|".join(map(re.escape, sskills_list)), re.IGNORECASE)
                smatches = re.findall(spattern, sresume_text.upper())
                sskills_set1.update(smatches)

    common_soft_path = os.path.join(base_path, "static", "uploads", "Commonsoft.txt")
    with open(common_soft_path, "w") as f:
        for skill in sskills_set1:
            f.write(skill + "\n")

    total_skills_file2 = len(set([line.strip() for line in open(sfile_list[0], 'r')]))
    smatch_rate = round((len(sskills_set1) / total_skills_file2) * 100)

    with open(common_soft_path, 'r') as f:
        Csoftskills = f.read()

    # Visualization
    categories = ['Technical', 'Soft']
    values = [match_rate, smatch_rate]

    plt.figure(figsize=(6, 4))
    bars = plt.bar(categories, values)
    plt.ylim(0, 100)
    plt.ylabel('Match Percentage')
    plt.title('Skill Match Comparison')

    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2.0, height - 10, f'{height}%', ha='center', va='bottom', color='white')

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode()
    buffer.close()
    plt.close()

    return render_template('Common.html',
                           Cskills=Cskills,
                           Csoftskills=Csoftskills,
                           match_rate=match_rate,
                           smatch_rate=smatch_rate,
                           image=image_base64)

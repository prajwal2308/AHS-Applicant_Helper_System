from flask import Flask, render_template, request, redirect, url_for, session
from AHS.second import second
from AHS.Third import third
import re
import os
from datetime import datetime
from PyPDF2 import PdfReader

app = Flask(__name__)
app.secret_key = '1234'

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.register_blueprint(second, url_prefix="/scrapes")
app.register_blueprint(third, url_prefix="/compares")

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == "admin" and password == "admin":
            session['loggedin'] = True
            session['id'] = 1
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return render_template('index.html', msg="Incorrect username/password!")
    return render_template('index.html')

@app.route('/pythonlogin/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/pythonlogin/home')
def home():
    if 'loggedin' in session:
        return render_template('home.html', username=session['username'])
    return redirect(url_for('login'))

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf', 'txt'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/upload", methods=["POST", "GET"])
def upload():
    now = datetime.now()
    if request.method == 'POST':
        JDtext = request.form['text']
        files = request.files.getlist('files[]')

        for file in files:
            if file and allowed_file(file.filename):
                file.filename = "Resume.pdf"
                save_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                file.save(save_path)
                session['uploaded_img_file_path'] = save_path

                # Extract Resume text
                reader = PdfReader(save_path)
                page = reader.pages[0]
                Rtext1 = page.extract_text()

                resumewords_path = os.path.join(app.config['UPLOAD_FOLDER'], 'Resumewords.txt')
                with open(resumewords_path, 'w') as f:
                    f.write(Rtext1)

                with open(resumewords_path, 'r') as f:
                    resume_text = f.read()

                # Load skills list
                majorskills_path = os.path.join(app.config['UPLOAD_FOLDER'], 'majorskills2.txt')
                with open(majorskills_path, 'r') as f:
                    skills_list = [line.strip() for line in f.readlines()]

                pattern = re.compile("|".join(map(re.escape, skills_list)), re.IGNORECASE)
                matches = re.findall(pattern, resume_text.lower())
                skills_set = set(matches)
                print("Extracted Skills: ", skills_set)

                rskills_path = os.path.join(app.config['UPLOAD_FOLDER'], 'Rskills.txt')
                with open(rskills_path, "w") as f:
                    for skill in skills_set:
                        f.write(skill.upper() + "\n")

                # Load soft skills
                softskills_path = os.path.join(app.config['UPLOAD_FOLDER'], 'softskills.txt')
                with open(softskills_path, 'r') as s:
                    skills_list1 = [line.strip() for line in s.readlines()]

                pattern11 = re.compile("|".join(map(re.escape, skills_list1)), re.IGNORECASE)
                matches11 = re.findall(pattern11, resume_text.lower())
                skills_set11 = set(matches11)
                print("Extracted Soft Skills: ", skills_set11)

                rsoftskills_path = os.path.join(app.config['UPLOAD_FOLDER'], 'Rsoftskills.txt')
                with open(rsoftskills_path, "w") as f:
                    for skill in skills_set11:
                        f.write(skill.upper() + "\n")

                # Merge resume skills
                rmerged_path = os.path.join(app.config['UPLOAD_FOLDER'], 'Rmerged.txt')
                with open(rskills_path, 'r', encoding='utf-8') as file1, \
                     open(rsoftskills_path, 'r', encoding='utf-8') as file2, \
                     open(rmerged_path, 'w', encoding='utf-8') as merged_file:
                    merged_file.writelines(file1.readlines())
                    merged_file.writelines(file2.readlines())

                # Extract skills from JD
                with open(majorskills_path, 'r') as f:
                    skills_list = [line.strip() for line in f.readlines()]
                pattern1 = re.compile("|".join(map(re.escape, skills_list)), re.IGNORECASE)
                matches1 = re.findall(pattern1, JDtext.lower())
                JDtext1 = set(matches1)

                jskills_path = os.path.join(app.config['UPLOAD_FOLDER'], 'Jskills.txt')
                with open(jskills_path, "w") as f:
                    for skill in JDtext1:
                        f.write(skill.upper() + "\n")

                # Extract soft skills from JD
                with open(softskills_path, 'r') as f:
                    skills_list12 = [line.strip().lower() for line in f.readlines()]
                pattern12 = re.compile("|".join(map(re.escape, skills_list12)), re.IGNORECASE)
                matches12 = re.findall(pattern12, JDtext.lower())
                JDtext12 = set(matches12)

                jsoftskills_path = os.path.join(app.config['UPLOAD_FOLDER'], 'Jsoftskills.txt')
                with open(jsoftskills_path, "w") as f:
                    for skill in JDtext12:
                        f.write(skill.upper() + "\n")

                # Merge JD skills
                jdmerged_path = os.path.join(app.config['UPLOAD_FOLDER'], 'JDmerged.txt')
                with open(jskills_path, 'r', encoding='utf-8') as file1, \
                     open(jsoftskills_path, 'r', encoding='utf-8') as file2, \
                     open(jdmerged_path, 'w', encoding='utf-8') as merged_file:
                    merged_file.writelines(file1.readlines())
                    merged_file.writelines(file2.readlines())

                # Read back for rendering
                with open(jsoftskills_path, 'r') as f:
                    JDsoft = f.read()
                with open(rsoftskills_path, 'r') as f:
                    Rsoft = f.read()
                with open(jskills_path, 'r') as f:
                    JDtext11 = f.read()
                with open(rskills_path, 'r') as f:
                    filecontent = f.read()

                return render_template('display.html',
                                       content=filecontent,
                                       JDtext=JDtext11,
                                       Rtext=Rtext1,
                                       JDsoft=JDsoft,
                                       Rsoft=Rsoft)
    return render_template('upload.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)

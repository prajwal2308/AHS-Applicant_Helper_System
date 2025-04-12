from flask import Flask, render_template, request, redirect, url_for, session
# from flask_mysqldb import MySQL,MySQLdb
# import MySQLdb.cursors
from AHS.second import second
from AHS.Third import third
import re
import os
from datetime import datetime
from PyPDF2 import PdfReader



app = Flask(__name__)
app.secret_key = '1234'
UPLOAD_FOLDER = os.path.join('static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.register_blueprint(second
                       ,url_prefix="/scrapes")
app.register_blueprint(third,url_prefix="/compares")
#------------------------------------------------------------------------------------------------------------------
# Login without SQL database setup
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == "admin" and password == "admin":  # Dummy credentials
            session['loggedin'] = True
            session['id'] = 1
            session['username'] = username
            #return redirect(url_for('second.scrape'))
            return redirect(url_for('home'))
        else:
            return render_template('index.html', msg="Incorrect username/password!")
    return render_template('index.html')


#-----------------------------------------------------------------------------------------------------------------------

#LOGOUT-


@app.route('/pythonlogin/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   # Redirect to login page
   return redirect(url_for('login'))

#------------------------------------------------------------------------------------------------------------------
# REGISTER


# @app.route('/register', methods=['GET', 'POST'])
# def register():
   
#     msg = ''    
#     if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
#         # Create variables for easy access
#         username = request.form['username']
#         password = request.form['password']
#         email = request.form['email']
#                 # Check if account exists using MySQL
#         cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#         cursor.execute('SELECT * FROM userdata WHERE username = %s', (username,))
#         account = cursor.fetchone()
#         if account:
#             msg = 'Account already exists!'
#         elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
#             msg = 'Invalid email address!'
#         elif not re.match(r'[A-Za-z0-9]+', username):
#             msg = 'Username must contain only characters and numbers!'
#         elif not username or not password or not email:
#             msg = 'Please fill out the form!'
#         else:
#             #cursor.execute('INSERT INTO userdata VALUES (NULL, %s, %s, %s,NULL,NULL)', (id,username, password, email,))
#             cursor.execute("INSERT INTO userdata SET username = %s , password=%s , email = %s", 
#                (username,password,email,)) 
#             mysql.connection.commit()
#             msg = 'You have successfully registered!'
#     elif request.method == 'POST':       
#         msg = 'Please fill out the form!'   
#     return render_template('register.html', msg=msg)


#------------------------------------------------------------------------------------------------------------------
#HOME


@app.route('/pythonlogin/home')
def home():
    
    if 'loggedin' in session:      
        return render_template('home.html', username=session['username'])    
    return redirect(url_for('login'))

#------------------------------------------------------------------------------------------------------------------
#PROFILE


@app.route('/pythonlogin/profile')
def profile():
    # Check if user is loggedin
    if 'loggedin' in session:       
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM userdata WHERE id = %s', (session['id'],))
        account = cursor.fetchone()
        text1=account['Rskillcontent']
        try:
            text2=text1.decode()
            return render_template('profile.html', account=account,msg=text2)
        except:
            pass
        return render_template('profile.html', account=account)
    return redirect(url_for('login'))

#------------------------------------------------------------------------------------------------------------------
#UPLOAD


UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif','pdf','txt'])
  
def allowed_file(filename):
 return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
 
 
@app.route("/upload",methods=["POST","GET"])
def upload():
    
    # cursor = mysql.connection.cursor()
    # cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    now = datetime.now()
    if request.method == 'POST':
        JDtext = request.form['text']
        files = request.files.getlist('files[]')
        print(files)
        for file in files:
            if file and allowed_file(file.filename):
                file.filename="Resume.pdf"
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
                #convertedfile = convertToBinaryData(file.filename)                              
                file_path=session.get('uploaded_img_file_path', None)
                print(file_path)
                session['uploaded_img_file_path'] = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
               
               #Extracting text from Resume
                reader = PdfReader('static/uploads/Resume.pdf')
                print(len(reader.pages))
                page = reader.pages[0]
                Rtext1 = page.extract_text()
                with open('static/uploads/Resumewords.txt', 'w') as f:
                    f.write(Rtext1)
                    
               #Extracting skills from resume
                with open("static/uploads/Resumewords.txt", "r") as f:
                    resume_text = f.read()
                majorskills_path = os.path.join(os.path.dirname(__file__), 'static', 'uploads', 'majorskills2.txt')
                with open(majorskills_path, 'r') as f:
                    majorskills = f.read().splitlines()
                    skills_list = [line.strip() for line in f.readlines()]
                pattern = re.compile("|".join(map(re.escape, skills_list)), re.IGNORECASE)
                matches = re.findall(pattern, resume_text.lower())
                skills_set = set(matches)
                print("Extracted Skills: ", skills_set)
                with open("static/uploads/Rskills.txt", "w") as f:
                    for skill in skills_set:
                        f.write(skill.upper() + "\n")
                
                #Extracting Softskills from resume.
                with open("static/uploads/softskills.txt",'r') as s:
                    skills_list1 = [line.strip().lower() for line in s.readlines()]
                    
                pattern11 = re.compile("|".join(map(re.escape, skills_list1)), re.IGNORECASE)
                matches11 = re.findall(pattern11, resume_text.lower())
                skills_set11 = set(matches11)
                print("Extracted Skills: ", skills_set11)
                with open("static/uploads/Rsoftskills.txt", "w") as f:
                    for skill in skills_set11:
                        f.write(skill.upper() + "\n")
                        
            
                    #copying all Resume skills into one file
                with open('static/uploads/Rskills.txt', 'r', encoding='utf-8') as file1:
                    contents1 = file1.readlines()
                with open('static/uploads/Rsoftskills.txt', 'r', encoding='utf-8') as file2:
                    contents2 = file2.readlines()

                with open('static/uploads/Rmerged.txt', 'w', encoding='utf-8') as merged_file:
                    for line in contents1:
                        merged_file.write(line.rstrip() + '\n')
                    for line in contents2:
                         merged_file.write(line.rstrip() + '\n')               
               
               #Extracting skills from JD
                with open("static/uploads/majorskills2.txt", 'r') as f:
                        skills_list = [line.strip() for line in f.readlines()]
                pattern1 = re.compile("|".join(map(re.escape, skills_list)), re.IGNORECASE)
                matches1 = re.findall(pattern1, JDtext.lower())
                JDtext1 = set(matches1)
                with open("static/uploads/Jskills.txt", "w") as f:
                    for skill in JDtext1:
                        f.write(skill.upper() + "\n")
                
                 #Extracting softskills from JD
                with open("static/uploads/softskills.txt", 'r') as f:
                        skills_list12 = [line.strip().lower() for line in f.readlines()]
                        
                pattern12 = re.compile("|".join(map(re.escape, skills_list12)), re.IGNORECASE)
                matches12 = re.findall(pattern12, JDtext.lower())
                JDtext12 = set(matches12)
                with open("static/uploads/Jsoftskills.txt", "w") as f:
                    for skill in JDtext12:
                        f.write(skill.upper() + "\n")
                        
                    #copying all jd skills into one file
                with open('static/uploads/Jskills.txt', 'r', encoding='utf-8') as file1:
                    contents1 = file1.readlines()
                with open('static/uploads/Jsoftskills.txt', 'r', encoding='utf-8') as file2:
                    contents2 = file2.readlines()

                with open('static/uploads/JDmerged.txt', 'w', encoding='utf-8') as merged_file:
                    for line in contents1:
                        merged_file.write(line.rstrip() + '\n')
                    for line in contents2:
                         merged_file.write(line.rstrip() + '\n')
                        
                with open('static/uploads/Jsoftskills.txt','r') as f:
                    JDsoft=f.read() 
                with open('static/uploads/Rsoftskills.txt','r') as f:
                    Rsoft=f.read()     
                with open('static/uploads/Jskills.txt','r') as f:
                    JDtext11=f.read()                     
                with open('static/uploads/Rskills.txt','r') as f:
                    filecontent=f.read()
                #cur.execute(" INTO userdata (Rskillfname,Rskillcontent, uploaded_on) VALUES (%s,%s, %s)",[file.filename,filecontent, now])
                # cur.execute("UPDATE userdata SET Rskillfname = %s, Rskillcontent = %s , uploaded_on=%s WHERE id = %s", 
               #(file.filename, filecontent, now,session['id'],))                                         
               # mysql.connection.commit()
           
       # cur.close()     
        with open("static/uploads/Rskills.txt", "r") as f:
            content = f.read()
            print('\n'.join(JDtext1))
            return render_template('display.html',content=content,JDtext=JDtext11,Rtext=Rtext1,JDsoft=JDsoft,Rsoft=Rsoft)
    return render_template('upload.html')

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)

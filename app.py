from flask import Flask, render_template,request,redirect,flash,url_for,send_from_directory
from flask_mail import Mail,Message
import os
app=Flask(__name__)
app.secret_key='6948ecfb326e597ac7df2e68cb3cc142'

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=587
app.config['MAIL_USE_TLS']=True
app.config['MAIL_USERNAME']='safeelansrin42484@gmail.com'
app.config['MAIL_PASSWORD']='..........'
mail=Mail(app)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DOWNLOAD_FOLDER = os.path.join(BASE_DIR, 'downloads')

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/#skills')
def skills():
    
    return render_template('index.html')

@app.route('/send_message',methods=['POST'])
def send_message():
    name=request.form.get('name')
    email=request.form.get('email')
    message_text=request.form.get('message')
    
    # compose email
    msg=Message(
        subject=f"new message from {name}",
        sender='safeelansrin42484@gmail.com',
        recipients=[app.config['MAIL_USERNAME']], # RECIEVE THE MESSAGE
        body=f"From:{name}<{email}>\n\n{message_text}"
    )
    try:
        mail.send(msg)
        flash('Message sent successfully!','success')
    except Exception as e:
        print(f"Failed to send Email:{e}")
        flash('Error while sending message.','error')
    return redirect('/#contactme')

@app.route('/#project')
def project():
    return render_template('index.html')

@app.route('/#contactme')
def contact():
    return render_template('index.html')

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory('DOWNLOAD_FOLDER', filename, as_attachment=True)

if __name__=='__main__':
    app.run(debug=True)
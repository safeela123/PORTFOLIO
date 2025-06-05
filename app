app.secret_key='6948ecfb326e597ac7df2e68cb3cc142'

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=587
app.config['MAIL_USE_TLS']=True
app.config['MAIL_USERNAME']='safeelansrin42484@gmail.com'
app.config['MAIL_PASSWORD']='...........'
mail=Mail(app)
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
    return redirect('/#contactMe')

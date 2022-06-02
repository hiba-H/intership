from asyncio.windows_events import NULL
import base64
import datetime
from http.client import HTTPResponse
import io
from msilib.schema import CustomAction
#from os import sendfile
#import os

import smtplib
import smtplib,email,email.encoders,email.mime.text,email.mime.base
from email.message import EmailMessage
from sqlite3 import Date
from cv2 import error
from flask import Markup
import pandas as pd 
from email.mime.text import MIMEText

import socket

from sqlalchemy import null
socket.getaddrinfo('127.0.0.1', 8080)

import  sqlite3



def sender():
  contact = pd.read_csv('contact.csv')
  print(contact)
  emails = []
  for i in range(len(contact)) : 
    emails.append(contact['EMAILS'][i])

  print(emails)
  EMAIL_ADDRESS = 'himihiba707@gmail.com'                             #this one
  #fname , lname , campanyName , campanyAdress                        #this one 2

  msg = EmailMessage()
  msg['Subject'] = 'This is my first Python email'
  msg['From'] = EMAIL_ADDRESS 
  msg['To'] = emails
  #msg["Bcc"] = receiver_email


  file = open('NEWSLETTER.HTML')
  htmlC = file.read()
  msg.set_content(htmlC, subtype='html')
 
  with smtplib.SMTP('localhost') as smtp:
      #smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) 
      smtp.send_message(EMAIL_ADDRESS,emails,msg)
      mail_json = msg.get('Content-Disposition')
      # Send an HTTP POST request to /mail/send
      #response = smtp.client.mail.send.post(request_body=mail_json)
      #print(response.status_code)
      #print(response.headers)
      print(mail_json)


#flask
from flask import Flask, render_template, Response , request ,session ,redirect,flash, url_for
from flask_admin import Admin,expose ,BaseView# pip install flask-admin*
from flask_admin.contrib.sqla import ModelView
from werkzeug.exceptions import abort



app = Flask(__name__)
admin = Admin(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Data.db'


app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'maslernono@gmail.com'
app.config['MAIL_PASSWORD'] = 'maslernono-123'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

class SecureModelView(ModelView):
    def is_accessible(self):
        if "logged_in" in session:
            return True
        else:
            abort(403)

#admin.add_view(ModelView(name='home', endpoint='home'))


"""@app.route("/signUP", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        fullname = request.form["fullname"]
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        if request.form.get('username') == 'Admin' and request.form.get('password') == 'Admin':
            session['logged_in'] = True
            return redirect('/login')
        else:
            return render_template('signup.html', failed=True)
    return render_template('login.html')"""

class NotificationsView(BaseView):
    @expose('/')
    def index(self):
        if 'username' in session :
            if request.method == 'GET':
                sqliteConnection = sqlite3.connect('Data.db')
                cursor = sqliteConnection.cursor() 
                print("Connected to SQLite") 
                #total pRoject -contact-contactdeleted   



            return self.render('admin/dashboard2.html')
        return redirect(url_for('signIN'))
     


admin.add_view(NotificationsView(name='home', endpoint='home'))


@app.route("/signIN", methods=["GET", "POST"])
def signIN():
    try:
        print(session.pop("username",None))
   #     print(session["username"])
        if request.method == 'POST':
            sqliteConnection = sqlite3.connect('Data.db')
            cursor = sqliteConnection.cursor() 
            print("Connected to SQLite")
            admin_Info = cursor.execute("SELECT * FROM sender;").fetchall()
            print(admin_Info)
            a = bool
            for i in range(len(admin_Info)):
                a == True
                if request.form.get('username') == admin_Info[i][0] and request.form.get('password') == admin_Info[i][1] :
                        session['logged_in'] = True
                        username = admin_Info[i][0]
                        session['username'] =username
                        print(i)
                        sender = cursor.execute("SELECT * FROM sender;").fetchall()
                        project = cursor.execute("SELECT * FROM project;").fetchall()
                        contacts = cursor.execute("SELECT * FROM contacts;").fetchall()
                        print('11111111111111111111111111')
                        print(sender ,len(contacts))
                        date = []
                        for i in range(len(project)):
                            print(project[i][2])
                            date.append(project[i][2])
                        print(date)
                        #sender = cursor.execute("SELECT * FROM sender;").fetchall()
                        #contacts = cursor.execute("SELECT * FROM contacts;").fetchall()
                        contact = {'contact_email':[],'contact_name':[] }
                        author = {'author_email':[],'author_username':[] }
                        contact_num =[]
                        author_num = []

                        print(contacts)
                        for i in range(len(contacts)):
                            contact["contact_email"].append( contacts[i][1])
                            contact["contact_name"].append( contacts[i][0])


                        for i in range(len(sender)):
                            author["author_username"].append( sender[i][0])
                            author["author_email"].append( sender[i][2])




                            #return render_template('dashboard2.html',username =username , failed=True)
                            #return self.render('admin/dashboard2.html')
                            return redirect(url_for('home.index',username = username,senders = len(sender) , project = len(project) , contact = len(contacts) ,author_num=[author_num], contact_num=contact_num,date = date , contacts = [contact] , author = [author]))
                else:
                    print('nada')
                    a == False
            if a != True :
                raise Exception("username is incorrect")

            
        
        return render_template("login.html")
    except Exception :
            flash(Markup("*login failed Try again later or <a href='/signUP'>signUP </a> ."), category='error')
            return render_template("login.html")
        
@app.route("/signUP", methods=["GET", "POST"])
def signUP():
    try :
    # print(session.pop("username",None))
    # print(session["username"])
        if request.method == 'POST':
             sqliteConnection = sqlite3.connect('Data.db')
             cursor = sqliteConnection.cursor() 
             print("Connected to SQLite")
             username = request.form['username']
             email = request.form['email']
             password = request.form['password']
             "SELECT username, password, email FROM sender;"
             #sender = cursor.execute("SELECT * FROM sender;").fetchall()

            
             cursor.execute("INSERT INTO sender (username, password, email)VALUES ('{}','{}','{}');".format(username,password,email))
             sqliteConnection.commit()
             print("added")
             flash(Markup("the sign up was successful! click '' <a href='/signIN'>here </a> '' to sign in "), category='success')

             cursor.close()

             return render_template("signUP.html")
        return render_template("signUP.html")

    except sqlite3.IntegrityError as e:
        print(e ,e.args[0] == 'UNIQUE constraint failed: sender.email')
        if e.args[0] == 'UNIQUE constraint failed: sender.email':
            flash("*The email excists already", category='error')
            return render_template("signUP.html")
        elif  e.args[0] == 'UNIQUE constraint failed: sender.username':
            flash("*The username excists already", category='error')
            return render_template("signUP.html")
        else : 
            return render_template("signUP.html")
            
@app.route("/logout", methods=["GET", "POST"])
def logout():
    #return render_template("login.html")
    return redirect(url_for('signIN'))

    


"""""
PIXEL_GIF_DATA = base64.b64decode(b"R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7")
def index(request):
   return redirect(location='http://127.0.0.1:5000/send', code=302)

"""
class sendView(BaseView):
    @expose('/', methods=["GET", "POST"])
    def contact(self):
        if 'username' in session :
            if request.method == 'POST':
                sqliteConnection = sqlite3.connect('Data.db')
                cursor = sqliteConnection.cursor() 
                print("Connected to SQLite")
                ####CONTACT ADDing  :/ 
                contact_add = request.form['added']
                contact_drop = request.form['unsup']

                if  request.form ["added" ] != '':

                    contact_file2 = pd.read_csv(request.form["added"])
                    for i in range(len(contact_file2)):
                        cursor.execute("INSERT INTO contacts (`contact-name`, email)VALUES ('{}','{}');".format(contact_file2['NAME'][i],contact_file2['EMAILS'][i]))
                        sqliteConnection.commit()
                    print("added")
                elif request.form["unsup" ] != '':

                    contact_file2 = pd.read_csv(request.form["unsup"])
                    for i in range(len(contact_file2)):
                        cursor.execute("DELETE FROM contacts WHERE email='{}';".format(contact_file2['EMAILS'][i]))
                        sqliteConnection.commit()
                    print("dropped")
                cursor.close()
                ####end CONTACT ADDing  :]


                return redirect(url_for('send.send'))
            return self.render('admin/contact.html')
        return redirect(url_for('signIN'))

    @expose('/send', methods=["GET", "POST"])

    def send(self):
        if 'username' in session : 
            print('username' in session ,session['username'] )   
            if request.method == 'POST':

                subtitle = request.form["subject"]

                newsletter = request.form["html"]
                print(subtitle  , newsletter)
                #sqlite1 
                sqliteConnection = sqlite3.connect('Data.db')
                cursor = sqliteConnection.cursor() 
                print("Connected to SQLite")

                #END sqlite1 

                #contact


                contact = cursor.execute("SELECT * FROM contacts;").fetchall()
                contacts = []
                for i in range(len(contact)):
                    contacts.append(contact[i][1])
                print(contacts)
                cursor.close()

                #args
                sqliteConnection = sqlite3.connect('Data.db')
                cursor = sqliteConnection.cursor() 
                print("Connected to SQLite")
                if 'username' in session : 

                    EMAIL_ADDRESS = cursor.execute("select email from sender where username = '{}'".format(session['username'])).fetchall()
                    print(EMAIL_ADDRESS[0][0])
                else : 
                    print('AGAIN /')
                #EMAIL_ADDRESS = 'himihiba707@gmail.com'
                EMAIL_PASSWORD = 'umxqpggzvnmsrtue'

                msg = EmailMessage()
                msg['Subject'] = subtitle
                msg['From'] = EMAIL_ADDRESS[0][0] 
                msg['To'] = contacts
                #msg["Bcc"] = receiver_email

                #end args

                #sending
                file = open('NEWSLETTER.HTML')
                htmlC = file.read()
                msg.set_content(htmlC, subtype='html')
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                    smtp.login(str(EMAIL_ADDRESS[0][0]), EMAIL_PASSWORD) 
                    smtp.send_message(msg)
                    #mail_json = msg.get('Content-Disposition')



                    # Send an HTTP POST request to /mail/send
                    #response = EMAIL_ADDRESS.client.mail.send.post(request_body=mail_json)
                    #print(response.status_code)
                    #print(response.headers)
                    #print(mail_json)

                #end sendding


                name = request.form['name']
                status  = 'Sent'
                date = datetime.datetime.now()


                #sqlite2
                def convertToBinaryData(filename):
                    blobdata = []
                    # Convert digital data to binary format
                    with open(filename, 'rb') as file:
                        blobdata = list(file.read())

                    return blobdata

                sqliteConnection = sqlite3.connect('Data.db')
                cursor = sqliteConnection.cursor() 
                print("Connected to SQLite")
                if "subject"in request.form:
                    content = convertToBinaryData("NEWSLETTER.HTML")
                    print(content)
                    query = "INSERT INTO content(content) VALUES ('{}');".format(content)
                    cursor.execute(query)
                    num_content = cursor.lastrowid
                    cursor.execute("INSERT INTO project (name, date, sender_username,status) VALUES ('{}','{}','{}','{}');".format(name,date,str(EMAIL_ADDRESS[0][0]),'sent'))
                    num_project = cursor.lastrowid
                    cursor.execute("INSERT INTO `pro-content` (`num-project`, `content-num`)VALUES ('{}','{}');".format(num_content,num_project))
                    #cursor.execute("INSERT INTO sender (username, password)VALUES ();".format(name,date,EMAIL_ADDRESS))

                    sqliteConnection.commit()


                cursor.close()
                #END sqlite2
                #return self.render('admin/sends.html' )
                return redirect(url_for('sends.sends'))

            return self.render('admin/send.html')
        return redirect(url_for('signIN'))

    
admin.add_view(sendView(name='send', endpoint='send'))

class sendsView(BaseView):
    #@app.route('/sends', methods=["GET", "POST"])

    @expose('/',methods=["GET", "POST"])
    @expose('/sends',methods=["GET", "POST"])
    def sends(self):
        if 'username'  in session :
            if request.method == 'GET':
                sqliteConnection = sqlite3.connect('Data.db')
                cursor = sqliteConnection.cursor() 
                print("Connected to SQLite")
                content_tab = cursor.execute("SELECT * FROM content;").fetchall()
                print(content_tab[0])
                decoded = str(content_tab[0]).encode('latin1')
                print(content_tab[0])

                sender = cursor.execute("SELECT * FROM sender;").fetchall()
                project = cursor.execute("SELECT * FROM project;").fetchall()
                content = cursor.execute("SELECT * FROM content;").fetchall()
                proj_name = []
                proj_sender_email = []
                proj_sender_username = []
                proj_date = []
                proj_status = []
                proj_num = []
                for i in range(len(project)):
                    proj_num.append(i)
                    proj_name.append(project[i][1])
                    #proj_sender_username.append(project[i][1])
                    proj_sender_email.append(project[i][3])
                    sender = cursor.execute("SELECT username FROM sender where email = '{}';".format(proj_sender_email[i])).fetchall()
                    proj_sender_username.append(sender[0][0])
                    proj_date.append(project[i][2])
                    proj_status.append(project[i][4])
                print(proj_sender_email,proj_name,proj_status,proj_date)
                file = "NEWSLETTER"
            elif request.method =='POST':
                    sqliteConnection = sqlite3.connect('Data.db')
                    cursor = sqliteConnection.cursor() 
                    print("Connected to SQLite")
                    sender = cursor.execute("SELECT * FROM sender;").fetchall()
                    project = cursor.execute("SELECT * FROM project;").fetchall()
                    contact = cursor.execute("SELECT * FROM contacts;").fetchall()
                    print('11111111111111111111111111')
                    print(sender ,len(contact))
                    date = []
                    for i in range(len(project)):
                        print(project[i][2])
                        date.append(project[i][2])
                    print(date)

                    return redirect(url_for('home.index',senders = len(sender) , project = len(project) , contact = len(contact) , date = date))




            return self.render('admin/sends.html', proj_num =  proj_num,proj_sender_username=proj_sender_username ,proj_sender_email=proj_sender_email,proj_name=proj_name,proj_status=proj_status,proj_date=proj_date , file = file)
        return self.render('signIN')

    @expose('/sends/preview',methods=["GET", "POST"])
    def file(self):
        if 'username'  in session :    
            file = request.args.get("file")
            return self.render(file)
        return redirect(url_for('signIN'))

admin.add_view(sendsView(name='sends', endpoint='sends'))

#@app.route('/pixelwithinfo.gif')
#def returnPixelparams():
#    params  = request.args.get('sizeinfo')
#    gif = 'R0lGODlhAQABAIAAAP///////yH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=='
#    gif_str = base64.b64decode(gif)
#    return os.sendfile(io.BytesIO(gif_str), mimetype='image/gif')



if __name__ == '__main__':
    app.run(debug=True,port=5000)
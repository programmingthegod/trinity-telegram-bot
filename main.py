import telegram.ext
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")

updater = telegram.ext.Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    update.message.reply_text("Hello, Welcome to Trinity Bot")

def helps(update, context):
    update.message.reply_text(
        """
        Hi, I am a bot created for Trinity: the AI/ML club of AIT, Pune. To efficiently use the bot use the following commands:

        *Normal Functionalities*
        /start- basic intro with intrducing help command
        /help- listing all the commands

        *Information about Club*
        /events - list all the events
        /upcoming - lists upcoming events in tabular form
        /achievements - list all the achievements
        /projects - list of all projects worked
        /resources - to get all the research papers

        *Contact and Team Members of the Club*
        /contacts - to contact the club for any collaboration or any other event
        /admin - contact of the admin of the Bot (Club Secretary)
        /seteam - lists the Second Year Student Team of the club
        /feteam - lists the First Year Student Team of the club

        *User Contribution*
        /suggestions - if you want to suggest any improvement in the club
        /contribute - if you wish to contribute to any ongoing or upcoming project or papers

        I hope this helps :)
        """
    )

def contact(update, context):
    update.message.reply_text(
        """
        Trinity always looks up to collaborate as collaboration brings out a chance of learning and improvement.

        Secretary - Harsh Bisht

        Club Mail - trinity.aiclub@gmail.com
        Linkedin page - https://www.linkedin.com/company/trinityaiclub/
        Instagram - https://www.instagram.com/trinity.aiclub/
        Youtube - https://www.youtube.com/@trinityaiclub/
        All other Club Links - https://trinityaiclub.bio.link/

        For any Collaboration prefer contacting using Club Mail ID.
        """
    )

def feteam(update, context):
    update.message.reply_text(
        """
        The First Year Students at Trinity are very enthusiastic learners and efficient engineers. The list of the First Year Student Members of Trinity is given below:

        Neha Rathore
        Beer Singh
        Goldi
        Yatul
        Utkarsh Sachan
        Rishabh Sharma
        Akhand Pratap Singh
        Saurav Chauhan
        Ayush Kumar
        Ritish Kumar
        Ayush Badoni
        Avinash
        Haritha
        Raj Kumar
        Vanshika
        Richpal
        Aman Singh Rajput
        Maneesh Kumar

        Their enthusiasm in working for the club has helped club grow a lot.
        """
    )

def seteam(update, context):
    update.message.reply_text(
        """
        Trinity is run by a very efficient team of Second Year Students. The contact details of these Students are mentioned here:

        Joint Secretaries :
        Nitin Mahala
        Himanshu
        Ankit Sharma
        Nabajit Das
        Sandipan Roy
        Prathmesh Pol
        Saurav Singh
        Tanisha
        Anmol Singh
        Simrandeep Singh
        Sairaj Adhav
        Aditya Bharti

        SE Members :
        Pratham
        Prabhat
        Roshnee
        Satyam Satpathi
        Taufeeq Syed
        Anuj Kumar
        Aryan Singh
        Sundram Kumar
        Gnana Sagar

        Their enthusiasm in working, planning and managing events for the club has helped club in various ways and grow multifold.
        """
    )

def admin(update, context):
    update.message.reply_text(
        """
        Trinity works under the able management of its Secretary Harsh Bisht. He is a great leader, a passionate learner and the admin of the bot. His contact details are shared below :

        Harsh Bisht
        Mail - aitpune.harshbisht@gmail.com
        Instagram - https://www.instagram.com/thesuperhitengineer/
        LinkedIn - https://www.linkedin.com/in/programmingthegod/
        Portfolio - https://bio.link/harshgods/

        He has also founded a Student Technical Community by the name of Dev Shastra. He makes decisions which have a long term impact. He is therefore the best leader for Trinity.

        """
    )

dispatcher.add_handler(telegram.ext.CommandHandler('start', start))
dispatcher.add_handler(telegram.ext.CommandHandler('help', helps))
dispatcher.add_handler(telegram.ext.CommandHandler('contacts', contact))
dispatcher.add_handler(telegram.ext.CommandHandler('feteam', feteam))
dispatcher.add_handler(telegram.ext.CommandHandler('seteam', seteam))
dispatcher.add_handler(telegram.ext.CommandHandler('admin', admin))

updater.start_polling()
updater.idle()

import telegram.ext
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN =os.getenv("TOKEN")

def start(update, context):
    update.message.reply_text("Hello ! Welcome, This Bot is Created by Rohit, Sparsh, Himanshu. Its our Sem 1 Project")


def helps(update, context):
    update.message.reply_text(
        """ Please  Follow these commands
        /start - to start the conversation
        /collegeinfo - Infromation about GU
        /contact - Student Contant
        /help - to get help menu
        /studymaterial-MCA Sem-1 Study Material
  
        I Hope this help :)
        """)

def collegeinfo(update, context):
    update.message.reply_text(
        """ Galgotias University is a private university established in 2011 in Greater Noida, Uttar Pradesh. The university is recognized by UGC and accredited with an A+ Grade by NAAC. It is approved by BCI, PCI, COA, NCTE, NCHM and INC. Galgotias University has 17 institutions offering 62 UG, 44 PG, 25 Doctoral, 1 Certificate, 15 Diploma, and 5 Integrated courses in the fields of Engineering, Business, Law, Arts, Sciences, Media & Communication, etc. As per NIRF Rankings 2023, Galgotias University has been ranked at 91st position in Management and 52nd position under Pharmacy. The campus is situated over an area of 52 acres. The university has collaborations with International Universities like Purdue University, Goethe University, Kent State University, and many more.

B.Tech, MBA and Law programs are the flagship courses offered at Galgotias University.
The university conducts Galgotias Engineering Entrance Exam (GEEE), Galgotias University Management Aptitude Test (GUMAT) and Galgotias University Law School Admission Test (GULSAT).
The university also accepts National Level Entrance examination scores such as NATA, CAT, CLAT, LSAT etc.
Galgotias University is among the top 12 Private Indian Universities according to NIRF Innovation Ranking 2023.
Galgotias University has been awarded IAR Placement Audit (5 Stars) indicating the highest capability of placing students in top companies. Galgotias University Placements 2023 recorded 8500+ job offers from more than 850 recruiters and the highest and average package stood at INR 1.5 CPA and INR 5.25 LPA respectively. Microsoft, Amazon, American Express, Commvault, Zscaler, Capillary Technologies, Deloitte, KPMG, EY, and Hero Corp are the top recruiters at Galgotias University Placements 2023. 
        """)
def studymaterial(update, context):
    update.message.reply_text("""COA: https://youtu.be/DsK35f8wyUw?si=1Lc_C_ZjNZqK6GI
                              Python:https://youtu.be/vLqTf2b6GZw?si=-vDeex-BRumXtskc
                              C:https://youtu.be/irqbmMNs2Bo?si=HGo00M5Z40Joy5J0
                              DBMS:https://youtu.be/dl00fOOYLOM?si=9zT9y8S5VIFQU5lz""")
       
def contact(update, context):
    update.message.reply_text("rohitbisht9560@gmail.com")



updater = telegram.ext.Updater(TOKEN, use_context=True)
dispatch=updater.dispatcher

dispatch.add_handler(telegram.ext.CommandHandler('start', start))
dispatch.add_handler(telegram.ext.CommandHandler('help', helps))
dispatch.add_handler(telegram.ext.CommandHandler('collegeinfo', collegeinfo))
dispatch.add_handler(telegram.ext.CommandHandler('studymaterial', studymaterial))
dispatch.add_handler(telegram.ext.CommandHandler('Contact', contact))
updater.start_polling()
updater.idle()


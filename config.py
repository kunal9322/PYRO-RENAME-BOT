import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "16743442")

API_HASH = os.environ.get("API_HASH", "12bbd720f4097ba7713c5e40a11dfd2a")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5913387061:AAHLi8DHPngHsIBDNw1dTeaVYCV8-EQcn50") 

FORCE_SUB = os.environ.get("FORCE_SUB", "-1001952437599") 

DB_NAME = os.environ.get("DB_NAME","kunal")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://sonu55:sonu55@cluster0.vqztrvk.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/c52ebfdb1462ddb830e3f.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5885920877').split()]


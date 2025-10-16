import os
from dotenv import load_dotenv
load_dotenv()
SYNC_DB_URL =  os.environ["postgresql://postgres:123456@localhost:5432/todo_db"]
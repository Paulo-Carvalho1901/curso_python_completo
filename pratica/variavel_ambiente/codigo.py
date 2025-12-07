from dotenv import load_dotenv
import os

load_dotenv()


print(os.getenv('PORT'))
print(os.getenv('EMAIL'))


print(type(os.getenv('DEBUG')))

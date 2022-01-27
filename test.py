import os
import pyupbit
from dotenv import load_dotenv
load_dotenv()
AccessKey=os.environ.get('AccessKey')
SecretKey=os.environ.get('SecretKey')
upbit = pyupbit.Upbit(AccessKey, SecretKey)

print(upbit.get_balance("KRW-XRP"))
print(upbit.get_balance("KRW"))
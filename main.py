import os
import sys
import time
import random
from datetime import datetime

GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"
DIM = "\033[2m"

NAMES = [
"Alex Morgan", "Jordan Blake", "Taylor Reed",
"Casey Brooks", "Riley Parker", "Jamie Quinn",
"Morgan Ellis", "Avery Stone", "Cameron Wells",
"Dakota Hayes", "Sam Rivers", "Robin Gray"
]

STATUSES = [
"ARCHIVE", "REVIEW", "PENDING",
"CLOSED", "UNVERIFIED", "TEST"
]

def clear():
os.system("clear")

def banner():
print(GREEN + r"""
███████╗██████╗ ██╗ ██████╗ ██████╗
██╔════╝██╔══██╗██║ ██╔══██╗██╔══██╗
█████╗ ██████╔╝██║ ██║ ██║██████╔╝
██╔══╝ ██╔══██╗██║ ██║ ██║██╔══██╗
██║ ██████╔╝██║ ██████╔╝██████╔╝
╚═╝ ╚═════╝ ╚═╝ ╚═════╝ ╚═════╝
""" + RESET)
print(CYAN + " TERMUX TEWL | FBI_DB STYLE" + RESET)
print(YELLOW + " FICTIONAL RECORD GENERATOR" + RESET)
print(DIM + " Offline demo - no real records" + RESET)
print("-" * 48)

def generate_record():
return {
"id": "DEMO-" + str(random.randint(100000, 999999)),
"name": random.choice(NAMES),
"age": random.randint(18, 85),
"status": random.choice(STATUSES),
"time": datetime.now().strftime("%H:%M:%S")
}

def display_record(record):
print(
GREEN + "[RECORD] " + RESET
+ f"{record['id']} | "
+ f"NAME: {record['name']} | "
+ f"AGE: {record['age']} | "
+ f"STATUS: {record['status']} | "
+ f"TIME: {record['time']}"
)

def start_stream():
count = 0
print(CYAN + "\nStarting record stream..." + RESET)
print("Press CTRL+C to stop.\n")

try:
while True:
display_record(generate_record())
count += 1

if count % 100 == 0:
print(DIM + f"--- {count} demo records ---" + RESET)

time.sleep(0.02)

except KeyboardInterrupt:
print(YELLOW + "\nStream stopped." + RESET)

def review_records():
clear()
banner()
print(CYAN + "REVIEW MODE" + RESET)

for _ in range(10):
display_record(generate_record())

input("\nPress Enter to return...")

def main():
while True:
clear()
banner()
print("[1] START RECORD STREAM")
print("[2] REVIEW SAMPLE RECORDS")
print("[3] STOP / EXIT")
print("-" * 48)

choice = input(CYAN + "TEWL > " + RESET).strip()

if choice == "1":
start_stream()
input("\nPress Enter to continue...")
elif choice == "2":
review_records()
elif choice == "3":
print(GREEN + "Session terminated." + RESET)
sys.exit(0)
else:
print(RED + "Invalid selection." + RESET)
time.sleep(1)

if name == "main":
try:
main()
except KeyboardInterrupt:
print("\nExiting TEWL.")
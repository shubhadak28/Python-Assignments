import datetime

now = datetime.datetime.now()
print("Now:", now)

print("Date:", now.date())
print("Time:", now.time())

formatted = now.strftime("%d-%m-%Y %H:%M:%S")
print("Formatted:", formatted)

#Create a Custom Date

d = datetime.date(2024, 12, 25)
print("Christmas:", d)


#Add/Subtract Days Using timedelta
today = datetime.date.today()
next_week = today + datetime.timedelta(days=7)
yesterday = today - datetime.timedelta(days=1)

print("Today:", today)
print("Next Week:", next_week)
print("Yesterday:", yesterday)

#Parse String to Date (strptime)

date_str = "04-06-2025"
parsed = datetime.datetime.strptime(date_str, "%d-%m-%Y")
print("Parsed Date:", parsed.date())

#Get Only Today’s Date
today = datetime.date.today()
print("Today:", today)


#Common Format Codes with Examples
from datetime import datetime

now = datetime.now()

print("Full date & time:", now.strftime("%Y-%m-%d %H:%M:%S"))
print("Short date:", now.strftime("%d/%m/%y"))
print("12hr format:", now.strftime("%I:%M %p"))
print("Day & Month name:", now.strftime("%A, %B"))
print("Week of the year:", now.strftime("Week %W"))

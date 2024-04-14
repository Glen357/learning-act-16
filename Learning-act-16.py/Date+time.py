# # Date and time module
# # Author Glen
# # Date 06/03/2024
#
# import datetime
# gvr = datetime.date(1956, 1, 31)
# print(gvr)
# mill = datetime.date(2000, 1, 1)
# dt = datetime.timedelta(100)
# print(mill + dt)
#
# print(gvr.strftime("%A, %B %d, %Y"))
#
# message = "GVR was born on {:%A, %B %d, %Y}."
# print(message.format(gvr))
#
# launch_date = datetime.date(2017, 3, 30)
# launch_time = datetime.time(22, 27, 0)
# launch_datetime = datetime.datetime(2017, 3, 30, 22, 27, 0)
#
# print(launch_date)
# print(launch_time)

# print("Space X launch was", launch_datetime)
#
# now = datetime.datetime.today()
# print(now)
#
# moon_landing = "7/20/1969"
# moon_landing_datetime = datetime.datetime.strptime(moon_landing, "%m/%d/%Y")
# print("The first moon landing was", moon_landing_datetime)

# from datetime import datetime, timedelta
#
# date_input = input("Please enter a date (format: yyyy-mm-dd): ")
#
# try:
#     user_input = datetime.strptime(date_input, "%Y-%m-%d")
#     future_date = user_input + timedelta(weeks=2)
#     print("The date in two weeks will be:", future_date.strftime("%Y-%m-%d"))
# except ValueError:
#     print("Invalid format, Please try again YYYY-MM-DD")


# from datetime import datetime, timedelta
# #
# #Welcome message
# print("Welcome to a date search by timeframe")
# #prompt date
# start_date_str = input("please enter a date(format: yyyy-mm-dd): ")
# start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
# #prompt years +
# timeframe = input("please enter the timeframe in years: ")
# timeframe_years = int(timeframe)
# #return prompt amnt + date
# end_date = start_date + timedelta(days=timeframe_years *365)
# print("The end date is: ", end_date.strftime("%Y-%m-%d"))

from datetime import datetime

def calculate_year_difference(date1, date2):

 difference = date1 - date2

 years = difference.days // 365

 return years


date1_str = input("please enter a date (format: yyyy-mm-dd: ")
date2_str = input("please enter a second date (format: yyyy-mm-dd: ")

date1 = datetime.strptime(date1_str, "%Y-%m-%d")
date2 = datetime.strptime(date2_str, "%Y-%m-%d")

years_diff = calculate_year_difference(date1, date2)

print(f"The difference between these dates in years is: {years_diff} years")
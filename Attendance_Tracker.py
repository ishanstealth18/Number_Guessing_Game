import openpyxl
import smtplib, ssl


path = 'D:\Python_Projects\Python_Beginner_Project\Attendance_Sheet.xlsx'
ref_workbook = openpyxl.load_workbook(path)
ws = ref_workbook.active


# Function to send email messages
def send_email(message, receiver_email):
    content = message
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    sender = "fnamesname972@gmail.com"
    receiver = "ishan.stealth@gmail.com"
    mail.login('fnamesname972@gmail.com', 'zzorpkbwvzrljkql')
    header = 'To: ' + receiver + '\n' + 'From: ' + sender + '\n' + 'Subject: Test Email\n'
    content = header + content
    mail.sendmail(sender, receiver, content)
    mail.close()


# Function to check attendance using roll number and subjects from the excel sheet
def check_attendance(roll_number, subject):
    leave_count = 0
    while True:
        row_no = roll_number + 1
        print("row number: {}".format(row_no))
        cell_obj = ws.cell(row=row_no, column=subject)
        leave_count = cell_obj.value
        print("Roll no: {}, Subject attendance: {}".format(roll_number, cell_obj.value))
        break
    return leave_count


# Function to check if the holiday count is not more than threshold, and send emails respectively
def validate_holiday_value(holiday_count):
    if holiday_count >= 3:
        print("Email need to be sent to staff and student regarding lack of attendance, not allowed to take "
              "exams")
        send_email("Email need to be sent to staff and student regarding lack of attendance, not allowed to take "
                   "exams", "ishan.stealth@gmail.com")
    elif holiday_count == 2:
        print("Reminder that 1 leave is only remaining to student")
        send_email("Reminder that 1 leave is only remaining to student", "ishan.stealth@gmail.com")
    else:
        print("Do nothing")


# ===============Start Game ==================== #
roll_num_lst = []
subject_lst = []
print("3 -> Maths || 4 -> Science || 5 -> Geography")
# Logic to ask input for roll number and subject code from the user till user does not want to play.
# Also, adding all the roll numbers and subjects to the list
while True:
    roll_num = int(input("Enter the roll number: "))
    subject_code = int(input("Enter the subject code: "))
    roll_num_lst.append(roll_num)
    subject_lst.append(subject_code)
    user_input = input("Do you want to add more roll number and subjects? (Y/N): ")
    if user_input == 'Y':
        continue
    else:
        print("Thank you!!")
        break
print("Roll number list : ", roll_num_lst)
print("Subject list : ", subject_lst)

# Logic to go through all the roll numbers and subjects codes to check the attendance and send email
for roll in roll_num_lst:
    for sub in subject_lst:
        print("Roll number: {}, Subject: {} ".format(roll, sub))
        current_leaves = check_attendance(roll, sub)
        validate_holiday_value(current_leaves)

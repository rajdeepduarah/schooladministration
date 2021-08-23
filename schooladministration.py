import csv
def write_info_csv(info_list):
    with open('student_info_csv','a',newline='') as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(["Name","Age","contact number","E-mail"])
        writer.writerow(info_list)

if __name__=='__main__':
    condition=True
    student_num=1
    while(condition):
        student_info=input("enter any student information for student #{} in format(name age contact no email)=".format(student_num))

        student_info_list=student_info.split(' ')
        print("\nthe entered information is-\nname: {}\nAge: {}\nContact number: {}\nE-mail: {}"
                  .format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
        choice_check=input("is the entered information correct?(yes/no)=")
        if choice_check=="yes":
             write_info_csv(student_info_list)
             print("Entered split up information is:"+str(student_info_list))
             condition_check=input("enter(yes/no) if u want to enter any other student info=")
             if condition_check=="yes":
                 condition=True
             elif condition_check=="no":
                 condition=False
        elif choice_check=="no":
            print("\nPlease re-enter the values\n")
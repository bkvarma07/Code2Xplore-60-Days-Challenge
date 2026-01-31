#Smart Registration system
std_id=input("enter your ID number: ")
email=input("enter Email id: ")
password=input("enter password: ")
refcode=input("enter referral code: ")
valid=0
if(len(std_id)==7 and std_id[0]=='C' and std_id[1]=='S' and std_id[2]=='E' and std_id[3]=='-'):
    if(std_id[4]<='9' and std_id[4]>='0'):
        if(std_id[5]<='9' and std_id[5]>='0'):
            if(std_id[6]<='9' and std_id[6]>='0'):
                valid+=1

if(email.count('@')==1 and email.count('.')==1):
    if(email[0]!='@' and email[len(email)-1]!='@'):
        if(email[len(email)-1]=='u' and email[len(email)-2]=='d' and email[len(email)-3]=='e' and email[len(email)-4]=='.'):
            valid+=1

if(len(password)>=8 and password[0]<='Z' and password[0]>='A' ):
    if(password.count('1') or password.count('2') or password.count('3') or password.count('4') or
    password.count('5') or password.count('6') or password.count('7') or password.count('8') or
    password.count('9')):
        valid+=1

if(len(refcode)==6 and refcode[0]=='R' and refcode[1]=='E' and refcode[2]=='F'):
    if(refcode[3]<='9' and refcode[3]>='0' and refcode[4]<='9' and refcode[4]>='0'):
        if(refcode[len(refcode)-1]=='@'):
            valid+=1

if(valid==4):
    print("APPROVED")
else:
    print("REJECTED")

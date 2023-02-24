import sys
import io
import csv
import os

# encoding with 'utf-8' codec to use Korean
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

def SignUp(id,pw):
    f = open('./res/data.csv','a', newline='')
    wr = csv.writer(f)
    wr.writerow([id,pw])
    print("회원가입이 완료되었습니다.")
    f.close()



def SignIn(id,pw):
    f = open('./res/data.csv','r')
    rdr = csv.reader(f)
    for line in rdr:
        if id == line[0]:
            if pw == line[1]:
                print(f"로그인 성공 아이디 : {id}로 로그인 되었습니다. ")
            else:
                print("비밀번호가 틀렸습니다.")
        else:
            print("아이디가 틀렸습니다.")
    f.close()

def main():
    print("1. 회원가입")
    print("2. 로그인")
    print("3. 종료")
    menu = input("메뉴를 선택하세요 : ")
    if menu == "1":
        id = input("ID를 입력하세요 : ")
        pw = input("PW를 입력하세요 : ")
        SignUp(id,pw)
    elif menu == "2":
        id = input("ID를 입력하세요 : ")
        pw = input("PW를 입력하세요 : ")
        SignIn(id,pw)
    elif menu == "3":
        print("종료합니다.")
        exit()
    else:
        print("잘못된 메뉴입니다.")

if __name__ == "__main__":
    while True:
        main()
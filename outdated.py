import re

list_month={
    "January":'01',
    "February":'02',
    "March":'03',
    "April":'04',
    "May":'05',
    "June":'06',
    "July":'07',
    "August":'08',
    "September":'09',
    "October":'10',
    "November":'11',
    "December":'12'}

def main():
    print(new_date())

def new_date():
    while True:
        try:
            x = input('Date: ')
            comma = re.split(r'[,/]+', x)
            break_date = re.findall(r"[A-Za-z]+|\d+",x)
            if int(break_date[1])< 31 and len(break_date[1])<=2 and (1<len(comma)<=3):
                if break_date[0] in list_month and len(comma)==2:
                    return f"{break_date[2]}-{list_month[break_date[0]].zfill(2)}-{break_date[1].zfill(2)}"
                elif int(break_date[0])<=12 :
                    return f"{break_date[2]}-{break_date[0].zfill(2)}-{break_date[1].zfill(2)}"
                else:
                    pass
        except ValueError:
            pass
main()

def main():
    hours = input("What time is it ? ")
    hours = convert(hours)

    if 7<= hours <=8:
        print("breakfast time")
    elif 12<= hours <=13:
        print("lunch time")
    elif 18<= hours <=19:
        print("dinner time")

def convert(time):
    hour,minute = time.split(':')
    hour = float(hour)
    hour2 = float(minute) / 60
    time = float(hour) + float(hour2)
    return float(time)

if __name__ == "__main__":
    main()

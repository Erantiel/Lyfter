seconds = int(input("Enter the time in seconds to find out how many seconds are left until 10 minutes: "))

if seconds < 600:
    print(f'The missing seconds to reach 10 minutes are: {600-seconds}')
elif seconds == 600:
    print("The seconds entered are exactly 10 minutes.")
else:
    print("El tiempo introducido es mayor a 10 minutos.")
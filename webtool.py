print('''

 _   _  _____  ____     _____   ___    ___   _     
| | | ||  ___||  _ \   |_   _| / _ \  / _ \ | |    
| |_| || |___ | |_| |    | |  | | | || | | || |    
| / \ ||  ___||    /     | |  | | | || | | || |    
|  _  || |    |  _ \     | |  | | | || | | || |    
| / \ || |___ | |_| |    | |  | |_| || |_| || |___ 
|/   \||_____||____/     |_|   \___/  \___/ |_____|

****** Tool Name ::Web Tool ******
       Why This tool :: This tool Is Made for Gathering Information from Website
       Contact with Me : https://github.com/mrwnknown
    ** Donot try to Copy This. All right Reserved By MR.UNKOWN 
''')

print('''
01. Website to IP Address
02. Open Port Scanner
''')



num = int(input("Enter the Number :"))

if(num == 1):
    print('''
     _____  _____  _   _  ____     _     _   ___   _   _  ____     _____  ____  
     _____  _____  _   _  ____     _     _   ___   _   _  ____     _____  ____  
    |  ___||_   _|| \ | ||  _ \   \ \   / / / _ \ | | | ||  _ \   |_   _||  _ \ 
    | |___   | |  |  \| || | | |   \ \_/ / | | | || | | || |_| |    | |  | |_| |
    |  ___|  | |  | |\  || | | |    \   /  | | | || | | ||    /     | |  |  __/ 
    | |      | |  | | | || | | |     | |   | | | || | | || |\ \     | |  | |    
    | |     _| |_ | | | || |_| |     | |   | |_| || |_| || | | |   _| |_ | |    
    |_|    |_____||_| |_||____/      |_|    \___/  \___/ |_| |_|  |_____||_|      
        ''')

    a = raw_input("Enter your Website without http or https:")

    import socket as s
    host = str(a)
    ip = s.gethostbyname(host)
    print 'Your HOST is:',host
    print 'Your IP is  :',ip

    print("**Note : Copy The IP Address!!")

elif(num == 2):
    
    import sys
    import socket
    from datetime import datetime

    print('''
     ____    ___   ____   _____     ____   ____  _____  _   _  _   _  _____  ____  
    |  _ \  / _ \ |  _ \ |_   _|   / ___| /  __||  _  || \ | || \ | ||  ___||  _ \ 
    | |_| || | | || |_| |  | |    | |__  |  /   | | | ||  \| ||  \| || |___ | |_| |
    |  __/ | | | ||    /   | |     \__ \ | |    | |_| || |\  || |\  ||  ___||    / 
    | |    | | | || |\ \   | |        | || |    |  _  || | | || | | || |    | |\ \ 
    | |    | |_| || | | |  | |     ___| ||  \__ | | | || | | || | | || |___ | | | |
    |_|     \___/ |_| |_|  |_|    |____/  \____||_| |_||_| |_||_| |_||_____||_| |_|

        ''')

    target = raw_input("Target IP :")

    print("_" * 50)
    print("Scanning Target :",target)
    print("Scannig Started At :",str(datetime.now()))
    print("_" * 50)


    try:
        for port in range(1,655535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.5)


            result = s.connect_ex((target,port))
            if result == 0:
                print("[*] port {} is open".format(port))
            s.close()    

    except KeyboardInterrupt:
        print("\n Exiting :(")
        sys.exit()

    except socket.error:
        print("\ Host not Responding :(")
        sys.exit()

    else:
        print("ERROR")
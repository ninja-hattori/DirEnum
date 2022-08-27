#importing library
import requests
import argparse

#function to scan directory
def scanner(ip,wordlist):
    print('---------------Scanning---------------')
    print('---------------Valid URL--------------')

#looping through each word in wordlist
    for word in wordlist:
        #making the url
        url=f"http://{ip}/{word}"
        #print(url)

        #making a try block to avoid failure of program
        try:
            #sending the request
            response=requests.head(url)

            #if url is valid, print
            if response.status_code==200:
                print(f'[+] {url}')
            elif response.status_code==301:
                print(f'[+] DIRECTORY-> {url}')
            else:
                pass
        #if url is invalid, pass
        except requests.ConnectionError:
            pass
    print("\n")
    print('---------------Ending---------------')
    print('---------------Stopped--------------')

#main function
if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("-u", help="provide the ip address in the format 1.2.3.4")
    parser.add_argument("-w", help="path of wordlist(optional)")
    args=parser.parse_args()
    ip = args.u
    print("--------------------")
    print("| DirEnum          |")
    print("| by Ninja Hattori |")
    print("--------------------")
    print("\n")
    
    if args.w == None:
        wordlist="default.txt"
    else:
        wordlist=args.w
    
    if args.u is None:
        parser.print_help()
    
    else:
        try:
            print(f"Testing URL: http://{ip}\n")
            print(f"Wordlist used: {wordlist}\n")
            #reading the wordlist
            with open(wordlist,"r") as file:
                    name=file.read()
                    words=name.splitlines()
                    #print(type(words))
                    length=len(words)
                    print(f"Total words generated = {length}\n")
            scanner(ip,words)
        except KeyboardInterrupt:
            print("!!Keyboard Interruption!!")

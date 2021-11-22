X=open("C:\Users\subha\OneDrive\Desktop\info.py", "r")
word=input("Enter the word to search: ")
s=" "
count=1
while(s):
    s=X.readline()
    L=s.split()
    if word in L:
        print("Line Number:",count,":",s)
    count+=1

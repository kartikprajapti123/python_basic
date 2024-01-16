# this is for reading purpose nly
filename=open("test.txt")
reading=filename.read()
print(reading)

# method 2
with open("test.txt") as f:
    test=f.read()
    print(test)
    
    f.close()
    
    
# Writinh in file  
with open("test.txt","w") as f:
    test1=f.write("hello this is another name of txt ")
    f.close()
    
    
     

with open("test.txt","a") as f:
    test1=f.write("hello this is another name of txt ")
    f.close()
    

with open("test.txt","a") as f:
    test1=f.write("\nThis is the besthello my name is kartik \n")
    
    
    f.close()
    
    
text = "This is new content"
# writing new content to the file
fp = open("test.txt", 'w')
fp.write(text)
print('Done Writing')
fp.close()

# this is way we can write study in file 

with open("test.txt","r+") as f:
    text1=f.read()
    print(text1)
    if "hello" in text1:
        print("we found it ")
    else:
        print(text1)
    
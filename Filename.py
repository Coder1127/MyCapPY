name=input("Enter your Filename")
n=name.split(".")
ex="."+ n[-1]
if n[-1]=="py":
    print("The file is a Python file with Extension",ex)
elif n[-1]=="cpp":
    print("The file is a C++ file with Extension",ex)
elif n[-1]=="htm" or n[-1]=="html":
    print("The file is a HTML file with Extension",ex)
elif n[-1]=="txt":
    print("The file is a Text file with Extension",ex)
else:
    print("Invalid File Format")

# coding=utf-8
from base64 import encode, decode
from tkinter.filedialog import askopenfile
from tkinter.messagebox import showinfo
from tqdm.rich import tqdm

print("Please zip all your files to a zip file (dialog 1)")
f1 = askopenfile().name
print("Please select output file at (github-path)/installer/core_base64.py (dialog 2)")
f2=askopenfile().name
# f2 = "../mysql.py"
print("Hi")
print(encode(open(f1, "rb"), open(f2, "wb")) or "Encoding ended...")
f = open(f1, "rb")
s = f.read()
s = bytes(("{}='''".format(f1)), "utf-8", "strict") + s + b"'''"
f = open(f.name, "wb")
print("Hi")
for i in tqdm(s.split(b"\n")):
    f.write(i + b"\n")
f.close()
showinfo("Great! [howtoupdate-program-faq]",
         "You have already updated the file, why not pack it to the new installer by"
         " recompiling it?"
" Note: please add core_base64=''' at the beginning and ''' at the ending")
print(s)

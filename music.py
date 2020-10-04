from playsound import playsound

print("Select Track")
print("1) Track 1")
print("2) Track 2")

c = int(input("Enter Your choice))
if c==1:
    playsound("file1.mp3")
else:
    playsound("file2.mpeg")
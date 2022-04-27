commandln = input("Put in command line thingo: ")
pasttext = input("How much past commands: ")

pastcommands = []
for i in range(0, int(pasttext)):
    comd = input("Write past command %d: " % i)
    pastcommands.append(comd)

text = input("Put in typed command: ")
wait = input("Time to wait between chars in seconds(ish): ")
f = open("generated-cmd.bat", "a")

f.write("@echo off\n")
for i in range(1, len(text)+1):
    for j in pastcommands:
        f.write("echo. %s^> %s\n" % (commandln, j))
    f.write("echo. %s^> %s\n" % (commandln, text[0 : i]))
    f.write("ping localhost -n %s > nul\n" % wait)
    f.write("cls\n")
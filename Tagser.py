from appJar import gui

app = gui("Tagser")


app.addLabel("title", "Tagser")
app.setLabelBg("title", "green")
app.addLabelEntry("Input Tags")

def press(button):
        tagsString = app.getEntry("Input Tags")
        tagsString = tagsString.lower();
        tagsList = tagsString.split()
        print(tagsList)

app.addButtons(["Search"], press)

app.go()
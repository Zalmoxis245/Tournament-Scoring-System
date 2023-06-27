from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import os


databasePath = "./default.txt"
class EntryWithPlaceholder(tk.Entry):

    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey', alignment = "center", hider = "" ):    
        super().__init__(master, justify = alignment, show = "")

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']
        self.hider = hider

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self, a = False):
        if a:
            self.delete('0', 'end')
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color


    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end') 
            self['fg'] = self.default_fg_color
            super().config(show = self.hider)

    def foc_out(self, *args):
        if not self.get():
            super().config(show = "")
            self.put_placeholder()

def foundWarningLabel(array, text, showIt = False, rArray = False, doX = False, x = 0, giveDoX = False):
    a = []
    b = False
    for i in range(len(array)):
        if(array[i]["text"] == text):
            if showIt:
                a.append(i)
                b = True
            else:
                return True
    if doX:
      for i in range(len(a)):
          if array[a[i]].winfo_x() - x <50 and array[a[i]].winfo_x() - x > -50:
              return True
    elif giveDoX:
        for i in range(len(a)):
          if array[a[i]].winfo_x() - x <50 and array[a[i]].winfo_x() - x > -50:
              return a[i]
    elif b:
        return a
    elif rArray:
        return [-6.8, -6.9]
    return False

def getX(parameter):
        if parameter == 1:
            return [0.5]
        elif parameter == 2:
            return [0.28, 0.72]
        elif parameter == 3:
            return [0.2, 0.5, 0.8]
        elif parameter == 4:
            return [0.15, 0.3875, 0.6125, 0.85]
        elif parameter == 5:
            return [0.125, 0.3125, 0.5, 0.6875, 0.875]
        else:
            return []
def getWW(parameter):
        if parameter == 1:
            return 1
        elif parameter == 2:
            return 1.1
        elif parameter == 3:
            return 1.5
        elif parameter == 4:
            return 2
        elif parameter == 5:
            return 2.3
        
def showError(self, errorCode, fnr = 0):

    #No dropdown selected in "Add Participant/s"
    if (errorCode == 1000):
        self.warning = Label(self.root, text = "Select the number of participants you wish to add.", font = ("Times New Roman", 11), fg = 'red')
        self.warning.place(
            y = self.posDFN + int(self.incrementalFH*1.3),
            relx = .5,
            anchor = "center"
        )
        self.warningLabels.append(self.warning)
    #Invalid team name
    elif (errorCode == 1001):
        if foundWarningLabel(self.warningLabels, "Invalid team name"):
            pass
        else:
            #Placing Warning Label
            self.warning = Label(self.root, text = "Invalid team name", font = ("Times New Roman", 11), fg = 'red')
            self.warning.place(
                y = self.teamName.winfo_y()+int(self.incrementalFH*1.3),
                relx = .5,
                anchor = "center"
            )
            self.warningLabels.append(self.warning)
            #Replacing Everything Below It
            for i in range(len(self.fields)):
                if i == 0:
                    pass
                else:
                    self.root.geometry(f'{self.root.winfo_width()}x{int(self.root.winfo_height()+int(self.incrementalFH*.7))}+{self.root.winfo_x()}+{self.root.winfo_y()}')
                    for j in range(3):
                        self.fields[i][j].place(
                            y = self.fields[i][j].winfo_y() + int(self.incrementalFH*.8)
                        )
            for i in range(len(self.btnObjects)):
                self.btnObjects[i].place(
                    y = self.btnObjects[i].winfo_y() + 9 + int(self.incrementalFH*.7)
                )
        
    elif (errorCode == 1002):
        if foundWarningLabel(self.warningLabels, "Invalid first name", showIt = True, doX = True, x = self.fields[fnr][0].winfo_x()):
            pass
        else:
            #Placing Warning Label
            self.warning = Label(self.root, text = "Invalid first name", font = ("Times New Roman", 11), fg = 'red')
            self.warning.place(
                y = self.fields[fnr][0].winfo_y()+int(self.incrementalFH*1.7),
                relx = getX(int(self.args))[fnr-1],
                anchor = "center"
            )
            self.warningLabels.append(self.warning)
            #Replacing Everything Below It
            if self.level1 == False:
                self.root.geometry(f'{self.root.winfo_width()}x{int(self.root.winfo_height()+int(self.incrementalFH*1.8))}+{self.root.winfo_x()}+{self.root.winfo_y()}')
                for i in range(len(self.fields)):
                    if i == 0:
                        pass
                    else:
                        self.fields[i][1].place(
                            y = self.fields[i][1].winfo_y()+ 9 + int(self.incrementalFH*1.3)
                        )
                for i in range(len(self.btnObjects)):
                    self.btnObjects[i].place(
                        y = self.btnObjects[i].winfo_y() + 9 + int(self.incrementalFH*1.8)
                    )
                self.level1 = True
            
    elif (errorCode == 1003):
        if foundWarningLabel(self.warningLabels, "Invalid surname", showIt = True, doX = True, x = self.fields[fnr][1].winfo_x()):
            pass
        else:
            #Placing Warning Label
            self.warning = Label(self.root, text = "Invalid surname", font = ("Times New Roman", 11), fg = 'red')
            if self.level1:
                asdf = self.fields[fnr][1].winfo_y()+int(self.incrementalFH*2.2) + 9
            else:
                asdf = self.fields[fnr][1].winfo_y()+int(self.incrementalFH*1.7)
            self.warning.place(
                y = asdf,
                relx = getX(int(self.args))[fnr-1],
                anchor = "center"
            )
            self.warningLabels.append(self.warning)
            #Replacing Everything Below It
            if self.level2 == False:
                self.root.geometry(f'{self.root.winfo_width()}x{int(self.root.winfo_height()+int(self.incrementalFH*1.8))}+{self.root.winfo_x()}+{self.root.winfo_y()}')
                for i in range(len(self.btnObjects)):
                    self.btnObjects[i].place(
                        y = self.btnObjects[i].winfo_y() + 9 + int(self.incrementalFH*1.8)
                    )
                self.level2 = True
                

                
    elif (errorCode == 1004):
        messagebox.showerror(f"Error {errorCode}", "Team name already taken.")
    elif (errorCode == 1005):
        messagebox.showerror(f"Error {errorCode}", f"Paricipant {fnr+1} already registered in another team.")
    elif (errorCode == 1006):
        messagebox.showerror(f"Error {errorCode}", "There are duplicate team members in your team. \nYou might want to select a team of smaller size.")
    elif (errorCode == 1007):
        messagebox.showerror(f"Error {errorCode}", "Database file non-existant! \nCheck the path of it or add participants!")
    elif (errorCode == 1008):
        messagebox.showerror(f"Error {errorCode}", "Database file empty! \nAdd a team first!")
    elif (errorCode == 1009):
        pass
    elif (errorCode == 1010):
        pass
    elif (errorCode == 1011):
        pass
    elif (errorCode == 1100):
        self.warning = Label(self.root, text = "Select the event you want to add results to.", font = ("Times New Roman", 11), fg = 'red')
        self.fields[0].place(
            y = self.posDFN - self.incrementalFH
        )
        self.warning.place(
            y = self.posDFN + int(self.incrementalFH*.5),
            relx = .5,
            anchor = "center"
        )
        self.warningLabels.append(self.warning)
    elif (errorCode == 1101):
        self.warning = Label(self.root, text = "Select the team you want to add the results to.", font = ("Times New Roman", 11), fg = 'red')
        self.warning.place(
            y = self.posDFN + int(self.incrementalFH),
            relx = .5,
            anchor = "center"
        )
        self.warningLabels.append(self.warning)
    elif (errorCode == 1102):
        if foundWarningLabel(self.warningLabels, "Set his/her score.", showIt = True, doX = True, x = self.fields[fnr][0].winfo_x()):
            pass
        else:
            self.warning = Label(self.root, text = "Set his/her score.", font = ("Times New Roman", 11), fg = 'red')
            self.warning.place(
                y = self.posDFN + int(self.incrementalFH*4),
                relx = getX(self.added_fields)[fnr-2],
                anchor = "center"
            )
            self.warningLabels.append(self.warning)
    elif (errorCode == 1103):
        pass
    elif (errorCode == 1104):
        pass
    elif (errorCode == 1105):
        pass
    elif (errorCode == 1106):
        pass
    elif (errorCode == 1107):
        pass

class EntryWMK():

    #eFN - entry Field Number
    #dFN - dropdown Field Number // PUT ONE MORE THAN YOU WANT, CUZ FOR SOME REASON WHICH I FORGOT, I SUBSTRACT 1 FROM THE WHILE LOOP OF "dFN"
    #WMKnr - A variable which keeps track of which window should it make next ( it's easier this way than implementing more complicated stuff like multithreading or event listeners )
    #        You just have to basicly make a separate function with alot of "elif" in it which checks which window should it make next, it does provide a security issue if I think about it, but it's not a problem for me right now

    def nothing(*args):
        print(args[0])
    

    def __init__(self, wW, wH, wTitle, eFN, dFN,WMKnr,
                 wPos = "+700+400", options = [[[], ""]], buttons = [["Default", "Default","Default"]], 
                 firstWidgetHeight = .45, GapBetweenButtons = 1,
                 dropdownCommands = [],
                 nothingCommand = nothing
                 ):
    
        self.root = tk.Toplevel()
        self.root.title(f"{wTitle}")
        self.root.resizable(False, False)
        wPos = f"+{self.root.winfo_screenwidth() // 2 - wW // 2}+{self.root.winfo_screenheight() // 2 - wH // 2}"
        self.fields = []
        self.btnObjects = []
        self.warningLabels = []
        self.options = options
        self.buttons = buttons
        self.wW = wW
        self.wPos = wPos
        self.WMKnr = WMKnr
        self.posDFN = 0
        self.posBB = 0
        self.added_fields = 0
        self.errorLevels = 0
        self.args = 0
        self.level1 = False
        self.level2 = False
        self.currentEvent = ""
        if buttons[0] == ["Default", "Default", "Default"]:
            buttons[0] = ["Submit", self.defaultSubmit, WMKnr, [1, 10]]

        self.firstFH = wH * firstWidgetHeight
        self.incrementalFH = wH *.1
        self.titleH = int(wH * .22)

        self.title = Label(self.root, text = f"{wTitle}", font=("Times New Roman", 16))
        self.title.grid(row = 0, column = 0, pady = 2)
        self.title.place(relx = .5, y = self.titleH, anchor="center")

        

        
        i = 0
        if eFN != 0:
            for i in range(eFN):
                
                self.field = EntryWithPlaceholder(self.root, f"field{i}")
                self.field.place(
                    y = self.firstFH+i*self.incrementalFH,
                    relx = .5,
                    anchor = "center"
                    )
                self.fields.append(self.field)
        if dFN != 0:
            while i <(dFN+eFN-1):
                if len(dropdownCommands)==0:
                    currentCommand = nothingCommand
                else:
                    currentCommand = dropdownCommands[-1]
                    dropdownCommands.pop()
                
                    
                i = i + 1
                
                clicked = StringVar()
                clicked.set(self.options[dFN+eFN-i-1][1])
                
                self.field = OptionMenu(self.root, clicked, *self.options[dFN+eFN-i-1][0], command = currentCommand(self))
                self.field.place(y = self.firstFH+i*self.incrementalFH*1.15 - 5,
                                 relx = .5,
                                 anchor = "center",
                                 height = 25
                                 )
                self.fields.append(self.field)
                self.posDFN = self.firstFH+i*self.incrementalFH*1.15 - 5

        
        for uniqueNumber in range(len(buttons)):
            self.Btn = Button(
                self.root,
                text = buttons[uniqueNumber][0],
                height = buttons[uniqueNumber][3][0],
                width = buttons[uniqueNumber][3][1],
                command = lambda a = buttons[uniqueNumber][2], anotherUniqueNumberForButtons = uniqueNumber: buttons[anotherUniqueNumberForButtons][1](self,a)
                )
            self.Btn.place(
                y = self.firstFH*(1.025*dFN-dFN+1) + (i+2+uniqueNumber*GapBetweenButtons)*self.incrementalFH,
                relx = .5,
                anchor = "center"
                )
            self.btnObjects.append(self.Btn)
            self.posBB = self.firstFH*(1.025*dFN-dFN+1) + (i+2+uniqueNumber*GapBetweenButtons)*self.incrementalFH
            
        i = i + len(buttons)
        self.nH = int(wH+self.incrementalFH*(i-3)*(1.013*dFN-dFN+1))
        self.root.geometry(f'{wW}x{self.nH}{wPos}')
        
    
        
    def CFV(self, field, newPlaceholder = "\u0000"):
        if newPlaceholder != "\u0000":
            self.fields[field].placeholder = newPlaceholder
            self.fields[field].put_placeholder(newPlaceholder)

    def defaultSubmit(self, WMKnr):
        func(WMKnr, self)
        
    
            
def EditWindowWrapper(self):
        
    def EditWindow(args):
        self.args = args

        #Deleting Fields
        self.level1 = False
        if(len(self.warningLabels) != 0):
            for uniqueNumbersakndask in range(len(self.warningLabels)):
                self.warningLabels[-1].destroy()
                self.warningLabels.pop()
        unique_number = 0
        for i in range(self.added_fields+1):
            if (i == 0):
                pass
            else:
                for j in range(2):
                    self.fields[i][j].destroy()
                self.fields[i][2].destroy()
        del self.fields[1:6]
        self.added_fields = 0

        #Adding the fields
        self.teamName = EntryWithPlaceholder(self.root, "Team Name")
        self.teamName.place(
            y = self.firstFH + self.incrementalFH *.8,
            relx = .5,
            anchor = "center"
        )
        if int(args) == 1:
            self.teamName.config(state="disabled")
        for i in range(int(args)):
            participant = []
            for j in range(2):
                self.field = EntryWithPlaceholder(self.root, f"{'Firstname'*(j==0)}{'Surname'*(j==1)}")
                self.field.place(
                        y = self.firstFH+3+j*self.incrementalFH + int(self.incrementalFH * 3),
                        relx = getX(int(args))[i],
                        anchor = "center"
                        )
                participant.append(self.field)
            self.field = Label(self.root, text = f"Participant {i+1}", font=("Times New Roman", 10))
            self.field.place(
                y = self.firstFH + int(self.incrementalFH*2.2),
                relx = getX(int(args))[i],
                anchor = "center"
            )
            participant.append(self.field)
            self.fields.append(participant)
            self.added_fields = self.added_fields + 1

        #Updating the UI based on how many fields I added
        win_width = int(self.wW*getWW(int(args)))
        win_height = int(self.nH + self.incrementalFH * 3)
        x = self.root.winfo_screenwidth() // 2 - win_width // 2
        y = self.root.winfo_screenheight() // 2 - win_height // 2
        self.root.geometry(f'{win_width}x{win_height}+{x}+{y}')

        self.fields[0].place(
            y = self.posDFN - self.incrementalFH,
            relx = .5,
            anchor = "center",
            height = 25
        )
        
        self.btnObjects[0].place(
            y = self.posBB + self.incrementalFH * 3,
            relx = .5,
            anchor = "center"
        )

        self.btnObjects[1].place(
            y = self.posBB + self.incrementalFH * 4.3,
            relx = .5,
            anchor = "center"
        )
        
        
    return EditWindow
    
def submitTeam(self, WMKnr):
    if (len(self.fields) == 1):
        showError(self, 1000)
    else:
        if((self.teamName.get() == "Team Name" or self.teamName.get() == "") and int(self.args) != 1):
            showError(self, 1001)
        else:
            if foundWarningLabel(self.warningLabels, "Invalid team name"):
                a = foundWarningLabel(self.warningLabels, "Invalid team name", showIt = True)[0]
                self.warningLabels[a].destroy()
                del self.warningLabels[a]
                for i in range(len(self.fields)):
                    if i == 0:
                        pass
                    else:
                        #Reset Screen Position
                        win_width = int(self.root.winfo_width())
                        win_height = int(self.root.winfo_height() - self.incrementalFH*.7)
                        x = int(self.root.winfo_screenwidth() // 2 - win_width // 2)
                        y = int(self.root.winfo_screenheight() // 2 - win_height // 2)
                        self.root.geometry(f'{win_width}x{win_height}+{x}+{y}')
                        #Reset Object Position
                        for j in range(2):
                            self.fields[i][j].place(
                                y = self.fields[i][j].winfo_y() - int(self.incrementalFH*.1)
                            )
                        self.fields[i][2].place(
                                y = self.fields[i][2].winfo_y() - int(self.incrementalFH*.03)
                            )
                        for i in range(len(self.btnObjects)):
                            self.btnObjects[i].place(
                                y = self.btnObjects[i].winfo_y() + 9 - int(self.incrementalFH*.4)
                            )
        for i in range(len(self.fields)):
            if i == 0:
                pass
            else:
                if self.fields[i][0].get() == "Firstname" or self.fields[i][0].get() == "":
                    showError(self, 1002, fnr = i)
                else:
                    if foundWarningLabel(self.warningLabels, "Invalid first name", showIt = True, doX = True, x = self.fields[i][0].winfo_x()):
                        arr = foundWarningLabel(self.warningLabels, "Invalid first name", showIt = True)
                        for p in arr:
                            if (self.warningLabels[p].winfo_x() - self.fields[i][0].winfo_x()) < 50 and (self.warningLabels[p].winfo_x() - self.fields[i][0].winfo_x()) > -50:
                                self.warningLabels[p].destroy()
                                del self.warningLabels[p]
                                for j in range(len(arr)):
                                    if arr[j]>p:
                                        arr[j]= arr[j] - 1
                                if foundWarningLabel(self.warningLabels, "Invalid first name"):
                                    pass
                                else:
                                    
                                    #Reset Screen Position
                                    win_width = int(self.root.winfo_width())
                                    win_height = int(self.root.winfo_height() - self.incrementalFH*1.2)
                                    x = int(self.root.winfo_screenwidth() // 2 - win_width // 2)
                                    y = int(self.root.winfo_screenheight() // 2 - win_height // 2)
                                    self.root.geometry(f'{win_width}x{win_height}+{x}+{y}')
                                    #Reset Object Position
                                    for q in range(len(self.fields)):
                                        if q == 0:
                                            pass
                                        else:
                                            self.fields[q][1].place(
                                                y = self.fields[q][1].winfo_y() - int(self.incrementalFH*.4)
                                            )
                                    for i in range(len(self.btnObjects)):
                                        self.btnObjects[i].place(
                                            y = self.btnObjects[i].winfo_y() + 9 - int(self.incrementalFH*.8)
                                        )
                                    self.level1 = False
                if self.fields[i][1].get() == "Surname" or self.fields[i][1].get() == "":
                    showError(self, 1003, fnr = i)
                else:
                    if foundWarningLabel(self.warningLabels, "Invalid surname", showIt = True, doX = True, x = self.fields[i][1].winfo_x()):
                        arr = foundWarningLabel(self.warningLabels, "Invalid surname", showIt = True)
                        for p in arr:
                            if (self.warningLabels[p].winfo_x() - self.fields[i][1].winfo_x()) < 50 and (self.warningLabels[p].winfo_x() - self.fields[i][1].winfo_x()) > -50:
                                self.warningLabels[p].destroy()
                                del self.warningLabels[p]
                                for j in range(len(arr)):
                                    if arr[j]>p:
                                        arr[j]= arr[j] - 1
                                if foundWarningLabel(self.warningLabels, "Invalid surname"):
                                    pass
                                else:
                                    
                                    #Reset Screen Position
                                    win_width = int(self.root.winfo_width())
                                    win_height = int(self.root.winfo_height() - self.incrementalFH*1.2)
                                    x = int(self.root.winfo_screenwidth() // 2 - win_width // 2)
                                    y = int(self.root.winfo_screenheight() // 2 - win_height // 2)
                                    self.root.geometry(f'{win_width}x{win_height}+{x}+{y}')
                                    #Reset Object Position
                                    for i in range(len(self.btnObjects)):
                                        self.btnObjects[i].place(
                                            y = self.btnObjects[i].winfo_y() + 9 - int(self.incrementalFH*.8)
                                        )
                                    self.level2 = False
        if(len(self.warningLabels) == 0):
            users = []
            uniqueCheck = []
            for i in range(len(self.fields)):
                if i == 0:
                    pass
                else:
                    users.append(['"'+self.fields[i][0].get()+'"', '"'+self.fields[i][1].get()+'"'])
                    uniqueCheck.append('"'+self.fields[i][0].get()+'"' + '"'+self.fields[i][1].get()+'"')

            q = 0
            bol1 = True
            while q < len(uniqueCheck):
                w = q + 1
                while w < len(uniqueCheck):
                    if(uniqueCheck[q] == uniqueCheck[w]):
                        bol1 = False
                    w = w+1
                q = q+1
            if bol1 == False:
                showError(self, 1006)
            else:
                if int(self.args) == 1:
                    teamName = '"'+users[0][0].replace('"', '')+" "+users[0][1].replace('"', '')+'"'
                    tOrI = "Individual Participant"
                else:
                    teamName = '"'+self.teamName.get()+'"'
                    tOrI = "Team"
                bol = True
                if os.path.exists(databasePath):
                    with open(databasePath, "r") as file:
                        for line in file:
                            if ("TEAM NAME: " + teamName) in line:
                                showError(self, 1004)
                                bol = False
                            for anotherUniqueNumberForUsers in range(len(users)):
                                if ("\t\tFIRSTNAME: " + users[anotherUniqueNumberForUsers][0]) in line and ("\t\tSURNAME: " + users[anotherUniqueNumberForUsers][1]) in next(file, None):
                                    showError(self, 1005, fnr = anotherUniqueNumberForUsers)
                                    bol = False
                            if bol == False:
                                break
                    
                if bol:
                    messagebox.showinfo("Saved", f"{tOrI} Record Saved Succesfully!")
                    f = open(databasePath, "a")
                    f.write(F'TEAM NAME: {teamName}\n\tSCORE: "NO DATA"\n')
                    for jml in range(len(users)):
                        f.write(F'\tUSER{jml}:\n\t\tFIRSTNAME: {users[jml][0]}\n\t\tSURNAME: {users[jml][1]}\n\t\tFOOTBALL: "0"\n\t\tBASKETBALL: "0"\n\t\tCRICKET: "0"\n\t\tMATHS: "0"\n\t\tCHESS: "0"\n')
                    f.write('\n')
                    f.close()
                    func(self.WMKnr, self)
                    self.root.destroy()
def submitResults(self, WMKnr):
    if len(self.fields) == 1:
        showError(self, 1100)
    else:
        if len(self.fields) == 2:
            showError(self, 1101)
        else:
            for i in range(len(self.fields)):
                if i == 0 or i == 1:
                    pass
                else:
                    if self.fields[i][2].get() == "Score":
                        showError(self, 1102, fnr = i)
                    else:
                        if foundWarningLabel(self.warningLabels, "Set his/her score.", showIt = True, doX = True, x = self.fields[i][0].winfo_x()):
                            p = foundWarningLabel(self.warningLabels, "Set his/her score.", showIt = True, x = self.fields[i][0].winfo_x(), giveDoX = True)
                            self.warningLabels[p].destroy()
                            del self.warningLabels[p]
            def getEventIndex(eventName):
                if eventName == "FOOTBALL":
                    return 3
                elif eventName == "BASKETBALL":
                    return 4
                elif eventName == "CRICKET":
                    return 5
                elif eventName == "MATHS":
                    return 6
                elif eventName == "CHESS":
                    return 7
            if(len(self.warningLabels) == 0):
                writingToFile = []
                teamName = self.fields[1][1].get()
                totalScore = 0
                for k in range(self.added_fields):
                    writingToFile.append([k, self.currentEvent.upper(), int(self.fields[k+2][2].get())])
                    totalScore = totalScore + int(self.fields[k+2][2].get())
                with open(databasePath, "r") as file:
                    data = file.readlines()
                lineStart = 0
                for line in data:
                    if f'TEAM NAME: "{teamName}"' in line:
                        lineStart = data.index(line)
                        data[lineStart+1] = f'\tSCORE: "{totalScore}"\n'
                for g in range(self.added_fields):
                    data[lineStart+2+getEventIndex(self.currentEvent.upper())+8*g] = f'\t\t{self.currentEvent.upper()}: "{int(self.fields[g+2][2].get())}"\n'

                with open(databasePath, "w") as file:
                    file.writelines(data)
                messagebox.showinfo("Saved", "Data Saved Successfully")

                                        
def EditERWindowWrapper(self):
    def EditERWindow(teamName):
        #Deleting Existing Fields
        if(len(self.warningLabels) != 0):
            for uniqueNumbersakndask in range(len(self.warningLabels)):
                self.warningLabels[-1].destroy()
                self.warningLabels.pop()
        if self.added_fields != 0:
            for i in range(self.added_fields+2):
                if i == 0 or i == 1:
                    pass
                else:
                    for j in range(2):
                        self.fields[i][j].destroy()
            del self.fields[2:8]
            self.added_fields = 0
        #Initializing Data
        bol = False
        users = []
        with open(databasePath, "r") as file:
            for line in file:
                if 'TEAM NAME: "' in line:
                    if 'TEAM NAME: "' + teamName + '"' in line:
                        bol = True
                    else:
                        bol = False
                if bol:
                    if '\t\tFIRSTNAME: "' in line:
                        ln = line[14:]
                        users.append(ln[:-2])
                    if '\t\tSURNAME: "' in line:
                        ln = line[12:]
                        users[-1] = users[-1] + " " + ln[:-2]
        
        #Making Member Fields

        for i in range(len(users)):
            participant = []
            
            self.field = Label(self.root, text = users[i], font=("Times New Roman", 14))
            self.field.place(
                y = self.posDFN + int(self.incrementalFH*2.5),
                relx = getX(len(users))[i],
                anchor = "center"
            )
            participant.append(self.field)

            
            clicked = StringVar()
            clicked.set("Score")
            self.field = OptionMenu(self.root, clicked, *["1","2","3","4","5","6","7","8","9","10"])
            self.field.place(
                y = self.posDFN + int(self.incrementalFH*3.8),
                relx = getX(len(users))[i],
                anchor = "center"
            )
            participant.append(self.field)
            participant.append(clicked)
            
            self.fields.append(participant)
            self.added_fields = self.added_fields + 1
        #Updating the UI based on how many fields I added
        win_width = int(self.wW*getWW(len(users)))
        win_height = int(self.nH + self.incrementalFH * 3)
        x = self.root.winfo_screenwidth() // 2 - win_width // 2
        y = self.root.winfo_screenheight() // 2 - win_height // 2
        self.root.geometry(f'{win_width}x{win_height}+{x}+{y}')

        
        self.btnObjects[0].place(
            y = self.posBB + self.incrementalFH * 1.6,
            relx = .5,
            anchor = "center"
        )

        self.btnObjects[1].place(
            y = self.posBB + self.incrementalFH * 3,
            relx = .5,
            anchor = "center"
        )
        
    return EditERWindow
def AddERDropdownWrapper(self):
    def AddERDropdown(args):
        #Initializing data for the "Select Team" dropdown
        teams = []
        self.currentEvent = args
        with open(databasePath, "r") as file:
            for line in file:
                if "TEAM NAME: " in line:
                    ms = line[12:]
                    teams.append(ms[:-2])
        clicked = StringVar()
        clicked.set("Select Team")
        #Deleting Fields
        if(len(self.warningLabels) != 0):
            for uniqueNumbersakndask in range(len(self.warningLabels)):
                self.warningLabels[-1].destroy()
                self.warningLabels.pop()     
        #Making the "Select Team" dropdown
        if len(self.fields) == 1:
            teamName = []
            self.field = OptionMenu(self.root, clicked, *teams, command = EditERWindowWrapper(self))
            self.field.place(
                y = self.posDFN + self.incrementalFH,
                relx = .5,
                anchor = "center",
                height = 25
            )
            teamName.append(self.field)
            teamName.append(clicked)
            self.fields.append(teamName)


        
    return AddERDropdown

def EditResultsWindowWrapper(self):
    def EditResultsWindow(args):
        #Deleting Existing Fields
        if self.added_fields != 0:
            for i in range(self.added_fields+1):
                if i == 0:
                    pass
                elif i == 1:
                    self.fields[1].destroy()
                else:
                    for j in range(6):
                        self.fields[i][j].destroy()
            del self.fields[1:8]
            self.added_fields = 0
        #Initializing Data
        events = ["Football","Basketball","Cricket","Maths","Chess"]
        users = []
        userScore = []
        userScores = []
        totalScore = 0
        bol = False
        with open(databasePath, "r") as file:
            for line in file:
                if 'TEAM NAME: ' in line:
                    if f'TEAM NAME: "{args}"' in line:
                        bol = True
                    else:
                        bol = False
                if bol:
                    if '\t\tFIRSTNAME: "' in line:
                        ln = line[14:]
                        users.append(ln[:-2])
                    if '\t\tSURNAME: "' in line:
                        ln = line[12:]
                        users[-1] = users[-1] + " " + ln[:-2]
                    if '\t\tFOOTBALL: "' in line:
                        ln = line[13:]
                        userScore.append(ln[:-2])
                        totalScore = totalScore + int(ln[:-2])
                    if '\t\tBASKETBALL: "'in line:
                        ln = line[15:]
                        userScore.append(ln[:-2])
                        totalScore = totalScore + int(ln[:-2])
                    if '\t\tCRICKET: "' in line:
                        ln = line[12:]
                        userScore.append(ln[:-2])
                        totalScore = totalScore + int(ln[:-2])
                    if '\t\tMATHS: "' in line:
                        ln = line[10:]
                        userScore.append(ln[:-2])
                        totalScore = totalScore + int(ln[:-2])
                    if '\t\tCHESS: "' in line:
                        ln = line[10:]
                        userScore.append(ln[:-2])
                        totalScore = totalScore + int(ln[:-2])
                        userScores.append(userScore)
                        userScore = []
        
        #Making Member Fields
        self.field = Label(self.root, text = f'Total Score: {totalScore}', font=("Times New Roman", 14))
        self.field.place(
            y = self.posDFN + int(self.incrementalFH*.6),
            relx = .5,
            anchor = "center"
        )
        self.fields.append(self.field)
        self.added_fields = self.added_fields + 1
                        
        for i in range(len(users)):
            participant = []
            
            self.field = Label(self.root, text = users[i], font=("Times New Roman", 14))
            self.field.place(
                y = self.posDFN + int(self.incrementalFH*2),
                relx = getX(len(users))[i],
                anchor = "center"
            )
            participant.append(self.field)
            
            for j in range(len(events)):
                self.field = Label(self.root, text = events[j] + ": " + userScores[i][j], font=("Times New Roman", 10))
                self.field.place(
                    y = self.posDFN + int(self.incrementalFH*2.3) + self.incrementalFH * (j+1),
                    relx = getX(len(users))[i],
                    anchor = "center"
                )
                participant.append(self.field)
            
            self.fields.append(participant)
            self.added_fields = self.added_fields + 1
            
        #Updating the UI based on how many fields I added
        win_width = int(self.wW*getWW(len(users)))
        win_height = int(self.nH + self.incrementalFH * 7.3)
        x = self.root.winfo_screenwidth() // 2 - win_width // 2
        y = self.root.winfo_screenheight() // 2 - win_height // 2
        self.root.geometry(f'{win_width}x{win_height}+{x}+{y}')

        self.btnObjects[0].place(
            y = self.posBB + int(self.incrementalFH * 7.3),
            relx = .5,
            anchor = "center"
        )
        

    return EditResultsWindow
                    

def func(var, self):
    if (var==0):
        self.root.destroy()
        home = EntryWMK(350, 240, "Tournament Scoring System", 0,0,0,
                    
                    buttons = [
                        ["Add Participant/s", EntryWMK.defaultSubmit, 1, [1, 15]],
                        ["Enter Event Results", EntryWMK.defaultSubmit, 2 , [1, 17]],
                        ["Results", EntryWMK.defaultSubmit, 3, [1, 11]],
                        ["Quit", EntryWMK.defaultSubmit, 4, [1, 6]]
                    ],
                    
                    firstWidgetHeight = .34,
                    
                    GapBetweenButtons = 1.25
                    );
    elif var == 1:
        self.root.destroy()
        AP = EntryWMK(350, 250, "Add Participant/s", 0, 2, 0, options = [[["1","2","3","4","5"],"Please Select"]],
                    buttons = [
                        ["Submit", submitTeam, 0, [1, 10]],
                        ["Back", EntryWMK.defaultSubmit, 0, [1, 6]]
                    ],
                      
                    dropdownCommands = [EditWindowWrapper]
                    )
        AP.posDFN = AP.posDFN - 20
        AP.posBB = AP.posBB - 30
        AP.fields[0].place(
            y = AP.posDFN,
            relx = .5,
            anchor = "center",
            height = 25
        )
        AP.btnObjects[0].place(
            y = AP.posBB,
            relx = .5,
            anchor = "center"
        )
    elif var == 2:
        if os.path.exists(databasePath):
            with open(databasePath, 'r') as abc:
                lines = [i for i in abc.readlines() if len(i)>1]
                if len(lines) >2:
                    self.root.destroy()
                    ER = EntryWMK(350, 250, "Enter Event Results", 0, 2, 0, options = [[["Football","Basketball","Cricket","Maths","Chess"],"Select Event"]],
                                buttons = [
                                    ["Submit", submitResults, 0, [1, 10]],
                                    ["Back", EntryWMK.defaultSubmit, 0, [1, 6]]
                                ],
                                GapBetweenButtons = 1.3,
                                dropdownCommands = [AddERDropdownWrapper]
                                )
                    ER.posDFN = ER.posDFN - ER.incrementalFH
                    ER.fields[0].place(
                        y = ER.posDFN
                    )
                else:
                    showError(None, 1008)
        else:
            showError(None, 1007)
    elif var == 3:
        if os.path.exists(databasePath):
            with open(databasePath, 'r') as abc:
                lines = [i for i in abc.readlines() if len(i)>1]
            teams = []
            with open(databasePath, 'r') as file:
                for line in file:
                    if "TEAM NAME: " in line:
                        ms = line[12:]
                        teams.append(ms[:-2])
            if len(lines) >2:
                self.root.destroy()
                R = EntryWMK(350, 250, "Results", 0, 2, 0, options = [[teams,"Select Team"]],
                            buttons = [
                                ["Back", EntryWMK.defaultSubmit, 0, [1, 6]]
                            ],
                            GapBetweenButtons = 1,
                            dropdownCommands = [EditResultsWindowWrapper]
                            )
                R.fields[0].place(
                    y = R.posDFN - R.incrementalFH
                )
            else:
                showError(None, 1008)
        else:
            showError(None, 1007)
    elif var == 4:
        result = messagebox.askquestion("Quiting", "Are you sure you want to QUIT?")
        if result  == "yes":
            self.root.destroy()
        else:
            pass
            

if __name__ == "__main__":

    root = tk.Tk()
    root.withdraw()


    home = EntryWMK(350, 240, "Tournament Scoring System", 0,0,0,
                    
                    buttons = [
                        ["Add Participant/s", EntryWMK.defaultSubmit, 1, [1, 15]],
                        ["Enter Event Results", EntryWMK.defaultSubmit, 2 , [1, 17]],
                        ["Results", EntryWMK.defaultSubmit, 3, [1, 11]],
                        ["Quit", EntryWMK.defaultSubmit, 4, [1, 6]]
                    ],
                    
                    firstWidgetHeight = .34,
                    
                    GapBetweenButtons = 1.25
                    );

    
    







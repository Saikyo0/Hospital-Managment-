from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.list import MDList, OneLineAvatarIconListItem

# from kivymd.uix.list import ScrollView

kv = """
Screen:
    id: screen
	MDLabel:
		id:label
		text:"          Welcome to _____ Hospital System"
		pos_hint:{"center_x":0.5,"center_y":0.8}

	MDLabel:
		id:label2
		text:"          Please Choose Your Mode"
		pos_hint:{"center_x":0.5,"center_y":0.7}
	
	Button:
		id:button3
		text:""
		pos_hint:{"center_x":0.7,"center_y":2.0}
		size_hint:(0.4,0.2)
		on_press:
		    app.accept()
	Button:
		id:button4
		text:""
		pos_hint:{"center_x":0.7,"center_y":2.0}
		size_hint:(0.4,0.2)
        on_press:
            app.list(1)
    Button:
		id:button7
		text:""
		pos_hint:{"center_x":0.7,"center_y":2.0}
		size_hint:(0.4,0.2)
        on_press:
            app.current(1)
	Button:
		id:button5
		text:"User mode"
		pos_hint:{"center_x":0.7,"center_y":0.5}
		size_hint:(0.4,0.2)
        on_press:
            label.text = "          Welcome Please Choose An option"
            button.pos_hint = {"center_x":10,"center_y":10}
            button2.pos_hint = {"center_x":10,"center_y":10}
            button7.text = ""
            button7.pos_hint = {"center_x":0.3,"center_y":0.5}
            button4.text = "Manage Appointments"
            button4.pos_hint = {"center_x":0.7,"center_y":0.5}
            button5.pos_hint = {"center_x":0.3,"center_y":1.5}
            button6.pos_hint = {"center_x":0.3,"center_y":0.3}
            button6.text = "close"
	Button:
		id:button2
		text:""
		pos_hint:{"center_x":0.7,"center_y":2.0}
		size_hint:(0.4,0.2)
	
	Button:
		id:button6
		text:""
		pos_hint:{"center_x":0.7,"center_y":2.0}
		size_hint:(0.4,0.2)
		    
	Button:
		id:button
		text:"Admin Mode"
		pos_hint:{"center_x":0.3,"center_y":0.5}
		size_hint:(0.4,0.2)
		on_press:
			app.some()
			label.text = "        Welcome Please Choose An option"
			button.pos_hint = {"center_x":10,"center_y":10}
			button2.pos_hint = {"center_x":10,"center_y":10}
			button3.text = "Manage New Patients"
			button3.pos_hint = {"center_x":0.3,"center_y":0.5}
			button4.text = "Manage Appointments"
			button4.pos_hint = {"center_x":0.7,"center_y":0.5}
			button5.pos_hint = {"center_x":0.3,"center_y":1.5}
			button6.pos_hint = {"center_x":0.3,"center_y":0.3}
			button6.text = "close"
	
"""


class main(MDApp):
    def build(self):
        self.num = 0
        self.data = open("./data.txt",'w+')
        return Builder.load_string(kv)

    def some(self):
        self.username = MDTextField(hint_text="", pos_hint={"center_x": 0.5, "center_y": 0.6}, size_hint=(0.4, 0.4))
        self.sign_in = MDDialog(title="log-in", text="Username", size_hint=(0.8, 1.5),
                                buttons=[MDFlatButton(text="Next", on_press=self.some2)])
        self.sign_in.add_widget(self.username)
        self.sign_in.open()

    def some2(self, obj):
        self.sign_in.dismiss()
        self.sign_in2 = MDDialog(title="log-in", text="Password", size_hint=(0.8, 1.5),
                                 buttons=[MDFlatButton(text="Next", on_press=self.check)])
        self.password = MDTextField(hint_text="", pos_hint={"center_x": 0.5, "center_y": 0.2}, size_hint=(0.4, 0.4))
        self.sign_in2.add_widget(self.password)
        self.sign_in2.open()

    def check(self, obj):
        self.sign_in2.dismiss()
        self.sign_in.dismiss()
        if self.username.text == "admin" and self.password.text == "admin":
            pass
        else:
            main().stop()

    def change(self):
        pass

    def accept(self):
        self.pID = MDTextField(hint_text="", pos_hint={"center_x": 0.5, "center_y": 0.6}, size_hint=(0.4, 0.4))
        self.layout1 = MDDialog(title="New Patient", text="ID", size_hint=(0.8, 1.5),
                               buttons=[MDFlatButton(text="Next", on_press=self.pDept)])
        self.layout1.add_widget(self.pID)
        self.layout1.open()

    def pDept(self, obj):
        self.num+=1
        self.layout1.dismiss()
        self.data = open("./data.txt")
        num=str(self.num)+';'
        word = str(self.pID.text)
        self.data.writelines(num)
        self.data.writelines(word)
        self.pDepar = MDTextField(hint_text="", pos_hint={"center_x": 0.5, "center_y": 0.6}, size_hint=(0.4, 0.4))
        self.layout2 = MDDialog(title="New Patient", text="Department", size_hint=(0.8, 1.5),
                               buttons=[MDFlatButton(text="Next", on_press=self.pDoc)])
        self.layout2.add_widget(self.pDepar)
        self.layout2.open()

    def pDoc(self, obj):
        self.layout2.dismiss()
        word = str(self.pDepar.text)
        self.data = open("./data.txt")
        if word != "":
            self.data.writelines(word+'\n')
        self.Doc = MDTextField(hint_text="", pos_hint={"center_x": 0.5, "center_y": 0.6}, size_hint=(0.4, 0.4))
        self.layout3 = MDDialog(title="New Patient", text="Doctor", size_hint=(0.8, 1.5),
                               buttons=[MDFlatButton(text="Next", on_press=self.pName)])
        self.layout3.add_widget(self.Doc)
        self.layout3.open()

    def pName(self, obj):
        self.layout3.dismiss()
        word = str(self.Doc.text)
        self.data = open("./data.txt")
        if word != "":
            self.data.writelines(word+'\n')
        self.Name = MDTextField(hint_text="", pos_hint={"center_x": 0.5, "center_y": 0.6}, size_hint=(0.4, 0.4))
        self.layout4 = MDDialog(title="New Patient", text="Name", size_hint=(0.8, 1.5),
                               buttons=[MDFlatButton(text="Next", on_press=self.pGender)])
        self.layout4.add_widget(self.Name)
        self.layout4.open()

    def pGender(self, obj):
        self.layout4.dismiss()
        word = str(self.Name.text)
        self.data = open("./data.txt")
        if word != "":
            self.data.writelines(word+'\n')
        self.Gender = MDTextField(hint_text="", pos_hint={"center_x": 0.5, "center_y": 0.6}, size_hint=(0.4, 0.4))
        self.layout5 = MDDialog(title="New Patient", text="Gender", size_hint=(0.8, 1.5),
                               buttons=[MDFlatButton(text="Next", on_press=self.pAdress)])
        self.layout5.add_widget(self.Gender)
        self.layout5.open()

    def pAdress(self, obj):
        self.layout5.dismiss()
        word = str(self.pDepar.text)
        self.data = open("./data.txt")
        if word != "":
            self.data.writelines(word+'\n')
        self.Paddress = MDTextField(hint_text="", pos_hint={"center_x": 0.5, "center_y": 0.6}, size_hint=(0.4, 0.4))
        self.layout6 = MDDialog(title="New Patient", text="Address", size_hint=(0.8, 1.5),
                               buttons=[MDFlatButton(text="Next", on_press=self.pRoomnum)])
        self.layout6.add_widget(self.Paddress)
        self.layout6.open()

    def pRoomnum(self, obj):
        self.layout6.dismiss()
        word = str(self.Paddress.text)
        self.data = open("./data.txt")
        if word != "":
            self.data.writelines(word+'\n')
        self.roomnum = MDTextField(hint_text="", pos_hint={"center_x": 0.5, "center_y": 0.6}, size_hint=(0.4, 0.4))
        self.layout7 = MDDialog(title="New Patient", text="Room Number", size_hint=(0.8, 1.5),
                               buttons=[MDFlatButton(text="Next", on_press=self.close)])
        self.layout7.add_widget(self.roomnum)
        self.layout7.open()

    def close(self, obj):
        word = str(self.roomnum.text)
        if word != "":
            self.data.writelines(word)
            self.data.close()
        self.layout1.dismiss()
        self.layout2.dismiss()
        self.layout3.dismiss()
        self.layout4.dismiss()
        self.layout5.dismiss()
        self.layout6.dismiss()
        self.layout7.dismiss()


    def list(self, obj):
        self.totallist = MDDialog()
        self.data = open("./data.txt")
        self.data2 = self.data.read()
        self.data2 = self.data2.split(';')
        a = 0
        for x in self.data2:
            a=a+1
            print(a)
        self.totallist.add_widget(MDLabel(text=str(a)))
        self.totallist.open()

    def current(self,obj):
        self.dialog = MDDialog(text=" ")
        self.dialog.open()

main().run()

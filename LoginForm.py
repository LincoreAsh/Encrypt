from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import *


MORSE_CODE_DICT = {'А': '.-', 'Б': '-...', 'В': '.--',
                   'Г': '--.', 'Д': '-..', 'Е': '.',
                   'Ё': '.', 'Ж': '...-', 'З': '--..',
                   'И': '..', 'Й': '.---', 'К': '-.-',
                   'Л': '.-..', 'М': '--', 'Н': '-.',
                   'О': '---', 'П': '.--.', 'Р': '.-.',
                   'С': '...', 'Т': '-', 'У': '..-',
                   'Ф': '..-.', 'Х': '....', 'Ц': '-.-.',
                   'Ч': '---.', 'Ш': '----', 'Щ': '--.-',
                   'Ъ': '.--.-.', 'Ы': '-.--', 'Ь': '-..-',
                    'Э': '..-..', 'Ю': '..--', 'Я': '.-.-',
                   'а': '.-*', 'б': '-...*', 'в': '.--*',
                   'г': '--.*', 'д': '-..*', 'е': '.*',
                   'ё': '.*', 'ж': '...-*', 'з': '--..*',
                   'и': '..*', 'й': '.---*', 'к': '-.-*',
                   'л': '.-..*', 'м': '--*', 'н': '-.*',
                   'о': '---*', 'п': '.--.*', 'р': '.-.*',
                   'с': '...*', 'т': '-*', 'у': '..-*',
                   'ф': '..-.*', 'х': '....*', 'ц': '-.-.*',
                   'ч': '---.*', 'ш': '----*', 'щ': '--.-*',
                   'ъ': '.--.-.*', 'ы': '-.--*', 'ь': '-..-*',
                   'э': '..-..*', 'ю': '..--*', 'я': '.-.-*',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}

class Ui_LoginForm(object):

    def Close(self):
        exit()

    def Correct(self):

        u_ind = 0
        p_ind = 0
        cipher = ''
        for letter in self.lineEdit.text():
            if letter != ' ':
                try:
                    cipher += MORSE_CODE_DICT[letter] + ' '
                except:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("Введены некорректные символы")
                    msg.setWindowTitle("Неправильные символы")
                    msg.exec_()
                    break;
            else:

                try:
                    cipher += ' '
                except:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("Введены некорректные символы")
                    msg.setWindowTitle("Неправильные символы")
                    msg.exec_()
                    break;
        word = cipher


        with open(r'username.txt', 'r') as fp:
            # read all lines in a list
            lines = fp.readlines()
            for line in lines:
                line = ('\n'.join(filter(bool, line.split('\n'))))
                u_ind +=1
                if (word == line):
                    self.u_ind = u_ind
                    break;
                if ((self.lineEdit_2.text() == "") or (self.lineEdit.text() == "")):
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("Поле Username или Password не может быть пустым")
                    msg.setWindowTitle("Пустое поле")
                    msg.exec_()
                    break;

        p_cipher = ''
        for p_letter in self.lineEdit_2.text():
            if p_letter != ' ':
                try:
                    p_cipher += MORSE_CODE_DICT[p_letter] + ' '
                except:

                    break;
            else:
                try:
                    p_cipher += ' '
                except:
                    break;
        p_word = p_cipher


        with open(r'password.txt', 'r') as fp:
            # read all lines in a list
            p_lines = fp.readlines()
            for p_line in p_lines:
                p_line = ('\n'.join(filter(bool, p_line.split('\n'))))
                p_ind +=1
                if (p_word == p_line):
                    self.p_ind = p_ind

                    if self.p_ind == self.u_ind:
                        break


                if ((self.lineEdit_2.text() == "") or (self.lineEdit.text() == "")):
                    break;

        try:
            if (p_word == p_line) and (word == line):
                print()
        except:
            line = ""
            p_line = ""
        if (p_word == p_line) and (word == line):
            if ((p_ind == u_ind) and ((p_ind or u_ind) != 0)):
                global Username
                Username = cipher
                LoginForm.close()
                PersonalAccount.show()
                self.lineEdit.setText("")
                self.lineEdit_2.setText("")
                self.instance = Ui_PersonalAccount()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Вы успешно вошли. Знак '*' в шифровании означает маленькую русскую букву. При заполнении поля пожалуйста, вводите только русский текст, цифры и некоторые знаки препинания")
                msg.setWindowTitle("Успешный вход")
                msg.exec_()

            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Такой Username или Password не существует")
                msg.setWindowTitle("Неправильные данные")
                msg.exec_()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Такой Username или Password не существует")
            msg.setWindowTitle("Неправильные данные")
            msg.exec_()



    def encryptUser(self):

        cipher = ''
        for letter in self.lineEdit.text():
            if letter != ' ':
                try:
                    cipher += MORSE_CODE_DICT[letter] + ' '
                except:
                    break;
            else:
                # 1 пробел для разделения букв
                # 2 пробела для разделения слов
                try:
                    cipher += ' '
                except:
                    break;
        word = cipher
        def english(string):
                for char in string:
                    if (ord(char) <= 122 and ord(char) >= 65):
                        return True
                        break
                return False

        result = english(self.lineEdit.text())
        with open(r'username.txt', 'r') as fp:
            # read all lines in a list
            lines = fp.readlines()
            for line in lines:
                line = ('\n'.join(filter(bool, line.split('\n'))))
                if word == line or word == "" or (self.lineEdit_2.text() == "" or result == True):
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("Введены неправильные данные либо данные уже существуют. Разрешён ввод только русских букв, цифр и некоторых знаков препинания")
                    msg.setWindowTitle("Неправильные данные")
                    msg.exec_()
                    break;
            else:

                with open("username.txt", 'a', encoding='utf-8') as file:
                            file.write(f'{cipher}\n')
                            msg = QMessageBox()
                            msg.setIcon(QMessageBox.Information)
                            msg.setText("Вы успешно зарегистрировались")
                            msg.setWindowTitle("Успешная регистрация")
                            msg.exec_()


        p_cipher = ''
        for p_letter in self.lineEdit_2.text():
            if p_letter != ' ':
                try:
                    p_cipher += MORSE_CODE_DICT[p_letter] + ' '
                except:
                    break;
            else:
                # 1 пробел для разделения букв
                # 2 пробела для разделения слов
                try:
                    p_cipher += ' '
                except:
                    break;
        p_word = p_cipher
        with open(r'password.txt', 'r') as fp_file:
            # read all lines in a list
            p_lines = fp_file.readlines()
            for p_line in p_lines:
                p_line = ('\n'.join(filter(bool, p_line.split('\n'))))
                if word == line or word == "" or self.lineEdit.text() == "" or self.lineEdit_2.text() == "":
                    break;
            else:

                with open("password.txt", 'a', encoding='utf-8') as p_file:
                    p_file.write(f'{p_cipher}\n')
        return cipher


    def setupUi(self, LoginForm):

        LoginForm.setObjectName("LoginForm")
        LoginForm.setWindowIcon(QtGui.QIcon('verify.png'))
        LoginForm.resize(450, 550)
        LoginForm.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        LoginForm.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(LoginForm)
        self.widget.setGeometry(QtCore.QRect(20, 20, 370, 480))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(30, 30, 300, 420))
        self.label.setStyleSheet("background-image: url(background.jpeg);\n"
"border-radius:20px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(150, 90, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgba(255, 255, 255, 210);")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(70, 140, 220, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(105, 118. 132, 255);\n"
"color: rgba(255, 255, 255, 230);\n"
"padding-bottom: 7px;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 210, 220, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(105, 118. 132, 255);\n"
"color: rgba(255, 255, 255, 230);\n"
"padding-bottom: 7px;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(70, 280, 220, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton#pushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(61, 169, 208, 255), stop: 1 rgba(78, 73, 197, 255));\n"
"    color: rgba(255, 255,255,210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#pushButton:hover{    \n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(81, 189, 228, 255), stop: 1 rgba(98, 93, 217, 255));\n"
"}\n"
"QPushButton#pushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(21, 129, 168, 240), stop: 1 rgba(58, 53, 177, 255));\n"
"}\n"
"")
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
#################################Button Event#######################

        self.pushButton.clicked.connect(self.Correct)
####################################################################
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 40, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton#pushButton_2{\n"
"    color: rgb(255, 255,255);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#pushButton_2:hover{    \n"
"    background-color: rgb(255,0,0);\n"
"}\n"
"QPushButton#pushButton_2:pressed{\n"
"    padding-top:5px;\n"
"    background-color: rgb(155,0,40);\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
#################################Button Event#######################
        self.pushButton_2.clicked.connect(self.Close)
####################################################################
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(70, 320, 220, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton#pushButton_4{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(61, 169, 208, 255), stop: 1 rgba(78, 73, 197, 255));\n"
"    color: rgba(255, 255,255,210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#pushButton_4:hover{    \n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(81, 189, 228, 255), stop: 1 rgba(98, 93, 217, 255));\n"
"}\n"
"QPushButton#pushButton_4:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(21, 129, 168, 240), stop: 1 rgba(58, 53, 177, 255));\n"
"}\n"
"")
        self.pushButton_4.setFlat(False)
        self.pushButton_4.setObjectName("pushButton_4")
##########################################################
        self.pushButton_4.clicked.connect(self.encryptUser)
##########################################################

        self.retranslateUi(LoginForm)
        QtCore.QMetaObject.connectSlotsByName(LoginForm)




    def retranslateUi(self, LoginForm):
        _translate = QtCore.QCoreApplication.translate
        LoginForm.setWindowTitle(_translate("LoginForm", "Авторизация"))
        self.label_2.setText(_translate("LoginForm", "Login"))
        self.lineEdit.setPlaceholderText(_translate("LoginForm", "Username"))
        self.lineEdit_2.setPlaceholderText(_translate("LoginForm", "Password"))
        self.pushButton.setText(_translate("LoginForm", "Войти"))
        self.pushButton_2.setText(_translate("LoginForm", "X"))
        self.pushButton_4.setText(_translate("LoginForm", "Зарегистрироваться"))
#import res_rc


#################################################################################################################################################################################
##################################################################################################################################################################################
###################################################################################################################################################################################

class Ui_PersonalAccount(object):
    def encrypt(self):
        cipher = ''
        for letter in self.lineEdit_10.text():
            if letter != ' ':
                try:
                    cipher += MORSE_CODE_DICT[letter] + ' '
                except:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("Разрешён ввод только русских букв, цифр и некоторых знаков препинания")
                    msg.setWindowTitle("Неправильные данные")
                    msg.exec_()
                    break;

            else:
                # 1 пробел для разделения букв
                # 2 пробела для разделения слов
                cipher += ' '
        self.lineEdit_11.setText(cipher)
        return cipher

    def decrypt(self):
        def english(string):
                for char in string:
                    if (ord(char) <= 122 and ord(char) >= 65):
                        return True
                        break
                return False

        result = english(self.lineEdit_10.text())
        if result == True:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Разрешён ввод только русских букв и некоторых знаков препинания")
            msg.setWindowTitle("Неправильные данные")
            msg.exec_()

        decipher = ''
        citext = ''
        for letter in self.lineEdit_10.text():
            # проверка пробела
            if (letter != ' '):
                i = 0
                citext += letter
            else:
                i += 1
                if i == 2:
                    decipher += ' '
                else:
                    decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]

                    citext = ''
        self.lineEdit_11.setText(decipher)
        return decipher

    def ToLoginForm(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Вы действительно хотите вернуться на главную страницу? Ваши данные не будут сохранены")
        msg.setWindowTitle("Выход")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.exec_()
        result = msg.standardButton(msg.clickedButton())
        if result == 1024:
            PersonalAccount.close()
            self.lineEdit_10.setText("")
            self.lineEdit_11.setText("")
            LoginForm.show()

    def UsernameShow(self):
        decipher = ''
        citext = ''
        for letter in Username:
            # проверка пробела
            if (letter != ' '):
                i = 0
                citext += letter
            else:
                i += 1
                if i == 2:
                    decipher += ' '
                else:
                    decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]

                    citext = ''
        self.label_12.setText("Username: "+decipher)
        return decipher

    def setupUi(self, PersonalAccount):
        PersonalAccount.setObjectName("PersonalAccount")
        LoginForm.setWindowIcon(QtGui.QIcon('avatar.png'))
        PersonalAccount.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        PersonalAccount.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        PersonalAccount.resize(643, 655)
        self.widget_10 = QtWidgets.QWidget(PersonalAccount)
        self.widget_10.setGeometry(QtCore.QRect(30, 30, 571, 591))
        self.widget_10.setObjectName("widget_10")
        self.label_11 = QtWidgets.QLabel(self.widget_10)
        self.label_11.setEnabled(True)
        self.label_11.setGeometry(QtCore.QRect(40, 30, 461, 551))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setStyleSheet("background-image: url(backgrnd.jpg);\n"
"border-top-left-radius: 50px;\n"
"border-bottom-right-radius: 50px;")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_10 = QtWidgets.QLabel(self.widget_10)
        self.label_10.setGeometry(QtCore.QRect(130, 0, 401, 141))
        font = QtGui.QFont()
        font.setFamily("BigNoodleTooOblique")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255,255,255);")
        self.label_10.setObjectName("label_10")
        self.label_12 = QtWidgets.QLabel(self.widget_10)
        self.label_12.setGeometry(QtCore.QRect(90, 110, 371, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(False)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(255,255,255);")

        self.label_12.setObjectName("label_12")

        self.pushButton_10 = QtWidgets.QPushButton(self.widget_10)
        self.pushButton_10.setGeometry(QtCore.QRect(440, 40, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("QPushButton#pushButton_10{\n"
"    color: rgb(255, 255,255);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#pushButton_10:hover{    \n"
"    background-color: rgb(255,0,0);\n"
"}\n"
"QPushButton#pushButton_10:pressed{\n"
"    padding-top:5px;\n"
"    background-color: rgb(155,0,40);\n"
"}\n"
"")
        self.pushButton_10.setObjectName("pushButton_10")
#######################################################################################################################################
        self.pushButton_10.clicked.connect(self.ToLoginForm)
######################################################################################################################################
        self.pushButton_12 = QtWidgets.QPushButton(self.widget_10)
        self.pushButton_12.setGeometry(QtCore.QRect(360, 250, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("QPushButton#pushButton_12{\n"
"    background-color: rgba(80,255,80,240);\n"
"    color: rgba(0, 0,0,210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#pushButton_12:hover{    \n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(81, 189, 228, 255), stop: 1 rgba(98, 93, 217, 255));\n"
"}\n"
"QPushButton#pushButton_12:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(21, 129, 168, 240), stop: 1 rgba(58, 53, 177, 255));\n"
"}\n"
"")
        self.pushButton_12.setFlat(False)
        self.pushButton_12.setObjectName("pushButton_12")
#####################################################################################
        self.pushButton_12.clicked.connect(self.decrypt)
#####################################################################################
        self.lineEdit_10 = QtWidgets.QLineEdit(self.widget_10)
        self.lineEdit_10.setGeometry(QtCore.QRect(90, 180, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(105, 118. 132, 255);\n"
"color: rgba(255, 255, 255, 255);\n"
"padding-bottom: 7px;")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_13 = QtWidgets.QLabel(self.widget_10)
        self.label_13.setGeometry(QtCore.QRect(90, 360, 371, 51))
        font = QtGui.QFont()
        font.setFamily("BigNoodleTooOblique")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(False)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(255,255,255);")
        self.label_13.setObjectName("label_13")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.widget_10)
        self.lineEdit_11.setGeometry(QtCore.QRect(90, 430, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 2px solid rgba(105, 118. 132, 255);\n"
"color: rgba(255, 255, 255, 255);\n"
"padding-bottom: 7px;")
        self.lineEdit_11.setText("")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.pushButton_11 = QtWidgets.QPushButton(self.widget_10)
        self.pushButton_11.setGeometry(QtCore.QRect(210, 250, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("QPushButton#pushButton_11{\n"
"    background-color: rgba(255,80,80,240);\n"
"    color: rgba(0, 0,0,210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#pushButton_11:hover{    \n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(81, 189, 228, 255), stop: 1 rgba(98, 93, 217, 255));\n"
"}\n"
"QPushButton#pushButton_11:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(21, 129, 168, 240), stop: 1 rgba(58, 53, 177, 255));\n"
"}\n"
"")
        self.pushButton_11.setFlat(False)
        self.pushButton_11.setObjectName("pushButton_11")
#####################################################################################
        self.pushButton_11.clicked.connect(self.encrypt)
#####################################################################################
        self.pushButton_13 = QtWidgets.QPushButton(self.widget_10)
        self.pushButton_13.setGeometry(QtCore.QRect(100, 150, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("QPushButton#pushButton_13{\n"
                                         "    background-color: rgba(80,80,80,240);\n"
                                         "    color: rgba(255, 255,255,210);\n"
                                         "    border-radius: 5px;\n"
                                         "}\n"
                                         "QPushButton#pushButton_13:hover{    \n"
                                         "    \n"
                                         "    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(81, 189, 228, 255), stop: 1 rgba(98, 93, 217, 255));\n"
                                         "}\n"
                                         "QPushButton#pushButton_13:pressed{\n"
                                         "    padding-left:5px;\n"
                                         "    padding-top:5px;\n"
                                         "    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 rgba(21, 129, 168, 240), stop: 1 rgba(58, 53, 177, 255));\n"
                                         "}\n"
                                         "")
        self.pushButton_13.setFlat(False)
        self.pushButton_13.setObjectName("pushButton_13")
######################################################################
        self.pushButton_13.clicked.connect(self.UsernameShow)
######################################################################


        self.retranslateUi(PersonalAccount)
        QtCore.QMetaObject.connectSlotsByName(PersonalAccount)


    def retranslateUi(self, PersonalAccount):


        _translate = QtCore.QCoreApplication.translate
        PersonalAccount.setWindowTitle(_translate("PersonalAccount", "Личный кабинет"))
        self.label_10.setText(_translate("PersonalAccount", "Личный кабинет"))
        self.label_12.setText(_translate("PersonalAccount", "Username: ***" ))
        self.pushButton_10.setText(_translate("PersonalAccount", "Выйти"))
        self.pushButton_12.setText(_translate("PersonalAccount", "Расшифровать"))
        self.pushButton_13.setText(_translate("PersonalAccount", "Показать"))
        self.lineEdit_10.setPlaceholderText(_translate("PersonalAccount", "Введите текст..."))
        self.label_13.setText(_translate("PersonalAccount", "Ваш результат:"))
        self.lineEdit_11.setPlaceholderText(_translate("PersonalAccount", "Здесь ничего писать не нужно"))
        self.pushButton_11.setText(_translate("PersonalAccount", "Зашифровать"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginForm = QtWidgets.QWidget()
    PersonalAccount = QtWidgets.QWidget()
    ui = Ui_LoginForm()
    qi = Ui_PersonalAccount()
    ui.setupUi(LoginForm)
    qi.setupUi(PersonalAccount)
    LoginForm.show()
    sys.exit(app.exec_())

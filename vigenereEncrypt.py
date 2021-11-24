# Ron Shabso

import os
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QInputDialog
from PyQt5.QtWidgets import QMessageBox

alphabet = "abcdefghijklmnopqrstuvwxyz"  # for the cypher function


class Ui_VigenereProgram(QDialog):

    def setupUi(self, VigenereProgram):

        VigenereProgram.setObjectName("VigenereProgram")
        VigenereProgram.resize(604, 604)
        VigenereProgram.setStyleSheet("background-color: rgb(3, 45, 0);")
        VigenereProgram.setAnimated(True)
        VigenereProgram.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(VigenereProgram)
        self.centralwidget.setObjectName("centralwidget")

        ######### big Title

        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(10, 0, 581, 61))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(36)
        font.setItalic(False)
        self.Title.setFont(font)
        self.Title.setStyleSheet("color: rgb(71, 239, 0);")
        self.Title.setObjectName("Title")

        ######### END

        ###### Sub Titile ( the little one under the first title )

        self.subTitle = QtWidgets.QLabel(self.centralwidget)
        self.subTitle.setGeometry(QtCore.QRect(160, 60, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(26)
        self.subTitle.setFont(font)
        self.subTitle.setStyleSheet("color: rgb(71, 239, 0);")
        self.subTitle.setObjectName("subTitle")

        ######### END

        ##### running button

        self.encryptPush = QtWidgets.QPushButton(self.centralwidget)
        self.encryptPush.setGeometry(QtCore.QRect(230, 330, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.encryptPush.setFont(font)
        self.encryptPush.setStyleSheet(
            "background-color: rgb(17, 255, 0);\n""color: rgb(255, 255, 255);\n""border-radius: 20px;")
        self.encryptPush.setObjectName("encryptPush")
        self.encryptPush.clicked.connect(self.run)  # calling the function to run the encryption

        ######### END

        ######## about button

        self.aboutPush = QtWidgets.QPushButton(self.centralwidget)
        self.aboutPush.setGeometry(QtCore.QRect(20, 510, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(10)
        self.aboutPush.setFont(font)
        self.aboutPush.setStyleSheet(
            "background-color: rgb(17, 255, 0);\n""color: rgb(255, 255, 255);\n""border-radius: 20px;")
        self.aboutPush.setObjectName("aboutPush")
        self.aboutPush.clicked.connect(self.aboutus)  # this shows the names of the people that worked on this project

        ######### END

        ######### Export

        self.exportPush = QtWidgets.QPushButton(self.centralwidget)
        self.exportPush.setGeometry(QtCore.QRect(480, 510, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(10)
        self.exportPush.setFont(font)
        self.exportPush.setStyleSheet(
            "background-color: rgb(17, 255, 0);\n""color: rgb(255, 255, 255);\n""border-radius: 20px;")
        self.exportPush.setObjectName("exportPush")
        self.exportPush.clicked.connect(
            self.exportfile)  # exporting the file to txt and opening it with os to show the user the final crypt

        ######### END

        ####### Result linetext

        self.Result = QtWidgets.QLineEdit(self.centralwidget)
        self.Result.setGeometry(QtCore.QRect(160, 390, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Result.setFont(font)
        self.Result.setStyleSheet(
            "border-raduis: 10px;\n""background-color: rgb(0, 42, 3);\n""color: rgb(255, 255, 255);")
        self.Result.setText("")
        self.Result.setObjectName("Result")

        ######### END

        ############## file browser

        self.FileBrowser = QtWidgets.QLineEdit(self.centralwidget)
        self.FileBrowser.setGeometry(QtCore.QRect(180, 210, 151, 31))
        self.FileBrowser.setStyleSheet("border-raduis:5px;\n""background-color: rgb(255, 255, 255);")
        self.FileBrowser.setText("")
        self.FileBrowser.setObjectName("FileBrowser")

        self.browsePush = QtWidgets.QPushButton(self.centralwidget)
        self.browsePush.setEnabled(True)
        self.browsePush.setGeometry(QtCore.QRect(340, 210, 71, 31))
        self.browsePush.setStyleSheet(
            "background-color: rgb(0, 255, 0);\n""color: rgb(255, 255, 255);\n""border-radius: 5px;")
        self.browsePush.setObjectName("browsePush")
        self.browsePush.clicked.connect(self.browsefiles)  # the user opens the file and the program reads it
        self.browsePush.setObjectName("browsePush")

        ######### END

        ############ key for the encryption

        self.keyPush = QtWidgets.QPushButton(self.centralwidget)
        self.keyPush.setGeometry(QtCore.QRect(330, 260, 101, 41))
        self.keyPush.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.keyPush.setFont(font)
        self.keyPush.setStyleSheet(
            "background-color: rgb(0, 255, 0);\n" "color: rgb(255, 255, 255);\n""border-radius: 20px;")
        self.keyPush.setObjectName("keyPush")

        ######### END

        ########### Key input

        self.keyInput = QtWidgets.QLineEdit(self.centralwidget)

        self.keyInput.setMaxLength(2)
        self.keyInput.setGeometry(QtCore.QRect(160, 260, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.keyInput.setFont(font)
        self.keyInput.setStyleSheet("border-radius: 20px;\n""background-color: rgb(255, 255, 255);")
        self.keyInput.setText("")
        self.keyInput.setObjectName("keyInput")
        self.keyPush.clicked.connect(self.getinteger)  # here i couldnt convert the QlineEdit to an int, so ive
        # used another widget for int capture

        ######### END

        self.subTitle.raise_()
        self.encryptPush.raise_()
        self.aboutPush.raise_()
        self.Title.raise_()
        self.exportPush.raise_()
        self.FileBrowser.raise_()
        self.browsePush.raise_()
        self.Result.raise_()
        self.keyInput.raise_()

        # Default Menu and Status bar
        VigenereProgram.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VigenereProgram)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 604, 21))
        self.menubar.setObjectName("menubar")
        VigenereProgram.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(VigenereProgram)
        self.statusbar.setObjectName("statusbar")
        VigenereProgram.setStatusBar(self.statusbar)
        self.retranslateUi(VigenereProgram)
        QtCore.QMetaObject.connectSlotsByName(VigenereProgram)

    # Default function pyqt5 desigen made
    def retranslateUi(self, VigenereProgram):
        _translate = QtCore.QCoreApplication.translate
        VigenereProgram.setWindowTitle(_translate("VigenereProgram", "VigenereProgram"))
        self.subTitle.setText(_translate("VigenereProgram", "Encryption"))
        self.encryptPush.setText(_translate("VigenereProgram", "Encrypt"))
        self.aboutPush.setText(_translate("VigenereProgram", "About"))
        self.Title.setText(_translate("VigenereProgram", "Welcome to Vigenere"))
        self.exportPush.setText(_translate("VigenereProgram", "Export"))
        self.browsePush.setText(_translate("VigenereProgram", "Browse"))
        self.keyPush.setText(_translate("VigenereProgram", " Key"))

    # this functions opens file explorer, for the user to pick this txt file to encrypt, reads it and copies
    # it to the lineEdit section for further processing
    def browsefiles(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)

        if dialog.exec_():
            filenames = dialog.selectedFiles()
            if filenames[0].endswith(".txt"):  # if the file is truly an txt file
                with open(filenames[0], 'r') as f:  # if it is, read it and paste it to the lineEdit area
                    data = f.read()  # read the lines
                    self.FileBrowser.setText(data)  # write in the linEdit section
                    f.close()  # close the file for no error

            else:  # if not, pop up message comes up
                msg = QMessageBox()  # new message box
                msg.setWindowTitle("TXT file not found 404")
                msg.setText("ERROR #8778\n" "Please enter an .TXT file !!")
                msg.setIcon(QMessageBox.Warning)  # its a warning kind, meaning its an yellow triangle warning sign
                x = msg.exec_()  # running the window
                pass

    # this function confirms and runs the encryption system
    def run(self):
        if not self.FileBrowser.text() or not self.keyInput.text():  # cheking if the str's are empty
            msg = QMessageBox()
            msg.setWindowTitle("ERROR")
            msg.setText("ERROR #9991\n" "Please Fill The Following Fields !")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()  # if it is, pop up an error
        else:
            self.vinegerecipher(self.FileBrowser.text(), self.i)
            # sending the variables to the main encryption function, self i is the integer the user inputted in the
            # function called " getInteger "

    # getting an integer from the user using an input pop up dialog, i couldn't really scanned from the user
    # from the lineEdit section, i coudn't do " int(self.keyInput.text()) " so ive came up with this.
    def getinteger(self):
        self.i, okPressed = QInputDialog.getInt(self, "Please Enter The Key", "Key:", 0, 0, 26, 0)
        if okPressed:
            self.keyInput.setText(str(self.i))

    # the encryption block to do the actual job to encrypt, gts the text from the text file and an key(integer)
    def vinegerecipher(self, text, k1):
        cipherText = ""
        int(k1)
        if k1 >= 0:
            for b in text:
                position = alphabet.find(b)
                newPosition = (position + k1) % 26
                cipherText += alphabet[newPosition]
            self.Result.setText(cipherText)

    # about us section shows the people who worked on this program, me :)
    def aboutus(self):
        msg = QMessageBox()
        msg.setWindowTitle("מגיש")
        msg.setText("   רון שאבסו \n")
        msg.setIcon(QMessageBox.NoIcon)
        x = msg.exec_()

    # exporting the file to the main directory, opening it using os to show the user its final encryption
    def exportfile(self):
        if not self.Result.text():  # if its empty, don't export an blank file
            pass
        else:
            f = open('secret.txt', "w")
            f.write(self.Result.text())
            f.close()
            msg = QMessageBox()
            msg.setWindowTitle("export finished")
            msg.setText("Successfully Exported")
            msg.setIcon(QMessageBox.NoIcon)
            x = msg.exec_()
            os.startfile('secret.txt')  # starting the file


# main code the run the class
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_VigenereProgram()
    w = QtWidgets.QMainWindow()
    ex.setupUi(w)
    w.show()
    sys.exit(app.exec_())

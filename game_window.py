# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wl2_formMsOFbX.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QLabel, QSizePolicy,
    QTimeEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(780, 700)
        Form.setMinimumSize(QSize(780, 700))
        Form.setMaximumSize(QSize(780, 700))
        Form.setStyleSheet(u"background: #0f1255;\n"
"font-family: \"Oswald\", sans-serif;\n"
"font-weight: 700;\n"
"font-size: 20px;\n"
"color: #fff;")
        self.sum_7 = QLabel(Form)
        self.sum_7.setObjectName(u"sum_7")
        self.sum_7.setGeometry(QRect(30, 100, 120, 40))
        self.sum_7.setStyleSheet(u"background: #2c5cd8;\n"
"border-radius: 5px;\n"
"font-size: 15px;")
        self.sum_7.setAlignment(Qt.AlignCenter)
        self.textResultRound = QLabel(Form)
        self.textResultRound.setObjectName(u"textResultRound")
        self.textResultRound.setGeometry(QRect(45, 540, 91, 22))
        self.textResultRound.setStyleSheet(u"background: transparent;\n"
"font-size: 15px;\n"
"")
        self.textResultRound.setAlignment(Qt.AlignCenter)
        self.sum_4 = QLabel(Form)
        self.sum_4.setObjectName(u"sum_4")
        self.sum_4.setGeometry(QRect(30, 265, 120, 40))
        self.sum_4.setStyleSheet(u"background: #2c5cd8;\n"
"border-radius: 5px;\n"
"font-size: 15px;")
        self.sum_4.setAlignment(Qt.AlignCenter)
        self.sum_1 = QLabel(Form)
        self.sum_1.setObjectName(u"sum_1")
        self.sum_1.setGeometry(QRect(30, 430, 120, 40))
        self.sum_1.setStyleSheet(u"background: #2c5cd8;\n"
"border-radius: 5px;\n"
"font-size: 15px;")
        self.sum_1.setAlignment(Qt.AlignCenter)
        self.sum_0 = QLabel(Form)
        self.sum_0.setObjectName(u"sum_0")
        self.sum_0.setGeometry(QRect(30, 485, 120, 40))
        self.sum_0.setStyleSheet(u"background: #2c5cd8;\n"
"border-radius: 5px;\n"
"font-size: 15px;")
        self.sum_0.setAlignment(Qt.AlignCenter)
        self.resultRound = QLabel(Form)
        self.resultRound.setObjectName(u"resultRound")
        self.resultRound.setGeometry(QRect(30, 570, 120, 40))
        self.resultRound.setStyleSheet(u"background: #2c5cd8;\n"
"border-radius: 5px;\n"
"font-size: 15px;")
        self.resultRound.setAlignment(Qt.AlignCenter)
        self.sum_3 = QLabel(Form)
        self.sum_3.setObjectName(u"sum_3")
        self.sum_3.setGeometry(QRect(30, 320, 120, 40))
        self.sum_3.setStyleSheet(u"background: #2c5cd8;\n"
"border-radius: 5px;\n"
"font-size: 15px;")
        self.sum_3.setAlignment(Qt.AlignCenter)
        self.sum_5 = QLabel(Form)
        self.sum_5.setObjectName(u"sum_5")
        self.sum_5.setGeometry(QRect(30, 210, 120, 40))
        self.sum_5.setStyleSheet(u"background: #49a94d;\n"
"border-radius: 5px;\n"
"font-size: 15px;")
        self.sum_5.setAlignment(Qt.AlignCenter)
        self.sum_2 = QLabel(Form)
        self.sum_2.setObjectName(u"sum_2")
        self.sum_2.setGeometry(QRect(30, 375, 120, 40))
        self.sum_2.setStyleSheet(u"background: #2c5cd8;\n"
"border-radius: 5px;\n"
"font-size: 15px;")
        self.sum_2.setAlignment(Qt.AlignCenter)
        self.sum_6 = QLabel(Form)
        self.sum_6.setObjectName(u"sum_6")
        self.sum_6.setGeometry(QRect(30, 155, 120, 40))
        self.sum_6.setStyleSheet(u"background: #2c5cd8;\n"
"border-radius: 5px;\n"
"font-size: 15px;")
        self.sum_6.setAlignment(Qt.AlignCenter)
        self.sum_8 = QLabel(Form)
        self.sum_8.setObjectName(u"sum_8")
        self.sum_8.setGeometry(QRect(30, 45, 120, 40))
        self.sum_8.setStyleSheet(u"background: #2c5cd8;\n"
"border-radius: 5px;\n"
"font-size: 15px;")
        self.sum_8.setAlignment(Qt.AlignCenter)
        self.timer = QTimeEdit(Form)
        self.timer.setObjectName(u"timer")
        self.timer.setGeometry(QRect(200, 45, 241, 91))
        self.timer.setStyleSheet(u"background: #232323;\n"
"font-size: 46px;")
        self.timer.setWrapping(False)
        self.timer.setFrame(True)
        self.timer.setAlignment(Qt.AlignCenter)
        self.timer.setReadOnly(True)
        self.timer.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.timer.setCorrectionMode(QAbstractSpinBox.CorrectToPreviousValue)
        self.timer.setKeyboardTracking(False)
        self.timer.setProperty("showGroupSeparator", False)
        self.sgPlayer1 = QLabel(Form)
        self.sgPlayer1.setObjectName(u"sgPlayer1")
        self.sgPlayer1.setGeometry(QRect(215, 374, 140, 46))
        self.sgPlayer1.setStyleSheet(u"background: #1774a8;\n"
"border-radius: 5px;\n"
"font-size: 15px;")
        self.sgPlayer1.setAlignment(Qt.AlignCenter)
        self.sgPlayer2_ans4 = QLabel(Form)
        self.sgPlayer2_ans4.setObjectName(u"sgPlayer2_ans4")
        self.sgPlayer2_ans4.setGeometry(QRect(545, 440, 30, 30))
        self.sgPlayer2_ans4.setStyleSheet(u"background: #2c5cd8;")
        self.sgPlayer2_ans5 = QLabel(Form)
        self.sgPlayer2_ans5.setObjectName(u"sgPlayer2_ans5")
        self.sgPlayer2_ans5.setGeometry(QRect(600, 440, 30, 30))
        self.sgPlayer2_ans5.setStyleSheet(u"background: #2c5cd8;")
        self.sgPlayer2_ans2 = QLabel(Form)
        self.sgPlayer2_ans2.setObjectName(u"sgPlayer2_ans2")
        self.sgPlayer2_ans2.setGeometry(QRect(435, 440, 30, 30))
        self.sgPlayer2_ans2.setStyleSheet(u"background: #2c5cd8;")
        self.sgPlayer2 = QLabel(Form)
        self.sgPlayer2.setObjectName(u"sgPlayer2")
        self.sgPlayer2.setGeometry(QRect(215, 435, 140, 46))
        self.sgPlayer2.setStyleSheet(u"background: #490462;\n"
"border-radius: 5px;\n"
"font-size: 15px;")
        self.sgPlayer2.setAlignment(Qt.AlignCenter)
        self.sgPlayer2_ans3 = QLabel(Form)
        self.sgPlayer2_ans3.setObjectName(u"sgPlayer2_ans3")
        self.sgPlayer2_ans3.setGeometry(QRect(490, 440, 30, 30))
        self.sgPlayer2_ans3.setStyleSheet(u"background: #2c5cd8;")
        self.sgPlayer2_ans1 = QLabel(Form)
        self.sgPlayer2_ans1.setObjectName(u"sgPlayer2_ans1")
        self.sgPlayer2_ans1.setGeometry(QRect(380, 440, 30, 30))
        self.sgPlayer2_ans1.setStyleSheet(u"background: #ac3838;")
        self.sgPlayer1_ans5 = QLabel(Form)
        self.sgPlayer1_ans5.setObjectName(u"sgPlayer1_ans5")
        self.sgPlayer1_ans5.setGeometry(QRect(600, 380, 30, 30))
        self.sgPlayer1_ans5.setStyleSheet(u"background: #2c5cd8;")
        self.sgPlayer1_ans1 = QLabel(Form)
        self.sgPlayer1_ans1.setObjectName(u"sgPlayer1_ans1")
        self.sgPlayer1_ans1.setGeometry(QRect(380, 380, 30, 30))
        self.sgPlayer1_ans1.setStyleSheet(u"background: #49a94d;")
        self.sgPlayer1_ans4 = QLabel(Form)
        self.sgPlayer1_ans4.setObjectName(u"sgPlayer1_ans4")
        self.sgPlayer1_ans4.setGeometry(QRect(545, 380, 30, 30))
        self.sgPlayer1_ans4.setStyleSheet(u"background: #2c5cd8;")
        self.sgPlayer1_ans3 = QLabel(Form)
        self.sgPlayer1_ans3.setObjectName(u"sgPlayer1_ans3")
        self.sgPlayer1_ans3.setGeometry(QRect(490, 380, 30, 30))
        self.sgPlayer1_ans3.setStyleSheet(u"background: #2c5cd8;")
        self.sgPlayer1_ans2 = QLabel(Form)
        self.sgPlayer1_ans2.setObjectName(u"sgPlayer1_ans2")
        self.sgPlayer1_ans2.setGeometry(QRect(435, 380, 30, 30))
        self.sgPlayer1_ans2.setStyleSheet(u"background: #2c5cd8;")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"TheWeakLink - PLAYERS", None))
        self.sum_7.setText(QCoreApplication.translate("Form", u"$ 65", None))
        self.textResultRound.setText(QCoreApplication.translate("Form", u"\u0411\u0430\u043d\u043a \u0440\u0430\u0443\u043d\u0434\u0430", None))
        self.sum_4.setText(QCoreApplication.translate("Form", u"$ 20", None))
        self.sum_1.setText(QCoreApplication.translate("Form", u"$ 5", None))
        self.sum_0.setText(QCoreApplication.translate("Form", u"$ 0", None))
        self.resultRound.setText(QCoreApplication.translate("Form", u"$ 0", None))
        self.sum_3.setText(QCoreApplication.translate("Form", u"$ 15", None))
        self.sum_5.setText(QCoreApplication.translate("Form", u"$ 30", None))
        self.sum_2.setText(QCoreApplication.translate("Form", u"$ 10", None))
        self.sum_6.setText(QCoreApplication.translate("Form", u"$ 45", None))
        self.sum_8.setText(QCoreApplication.translate("Form", u"$ 100", None))
        self.timer.setSpecialValueText("")
        self.sgPlayer1.setText(QCoreApplication.translate("Form", u"\u0418\u0433\u0440\u043e\u043a 1", None))
        self.sgPlayer2_ans4.setText("")
        self.sgPlayer2_ans5.setText("")
        self.sgPlayer2_ans2.setText("")
        self.sgPlayer2.setText(QCoreApplication.translate("Form", u"\u0418\u0433\u0440\u043e\u043a 2", None))
        self.sgPlayer2_ans3.setText("")
        self.sgPlayer2_ans1.setText("")
        self.sgPlayer1_ans5.setText("")
        self.sgPlayer1_ans1.setText("")
        self.sgPlayer1_ans4.setText("")
        self.sgPlayer1_ans3.setText("")
        self.sgPlayer1_ans2.setText("")
    # retranslateUi

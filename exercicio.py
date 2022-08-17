# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'exercicio1.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(575, 360)
        MainWindow.setMinimumSize(QSize(575, 360))
        MainWindow.setMaximumSize(QSize(575, 360))
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setFamily(u"Bell MT")
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.pg_inicial = QStackedWidget(self.centralwidget)
        self.pg_inicial.setObjectName(u"pg_inicial")
        self.pg_inicial.setStyleSheet(u"background-color: rgb(27, 131, 191);\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"border-style: solid;\n"
"border-radius: 10px;")
        self.formulario = QWidget()
        self.formulario.setObjectName(u"formulario")
        self.verticalLayout_6 = QVBoxLayout(self.formulario)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_2 = QFrame(self.formulario)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(180, 30))
        self.label.setMaximumSize(QSize(100, 30))
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-style: None;\n"
"border-radius: 5px;")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.entry_nome = QLineEdit(self.frame_2)
        self.entry_nome.setObjectName(u"entry_nome")
        self.entry_nome.setMinimumSize(QSize(180, 30))
        self.entry_nome.setMaximumSize(QSize(100, 30))
        self.entry_nome.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.entry_nome.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.entry_nome)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(180, 30))
        self.label_2.setMaximumSize(QSize(100, 30))
        self.label_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-style: None;\n"
"border-radius: 5px;")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_2)

        self.entry_idade = QLineEdit(self.frame_2)
        self.entry_idade.setObjectName(u"entry_idade")
        self.entry_idade.setMinimumSize(QSize(180, 30))
        self.entry_idade.setMaximumSize(QSize(100, 30))
        self.entry_idade.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.entry_idade.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.entry_idade)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)


        self.gridLayout.addLayout(self.verticalLayout_4, 0, 1, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.cb_genero = QComboBox(self.frame_2)
        self.cb_genero.addItem("")
        self.cb_genero.addItem("")
        self.cb_genero.addItem("")
        self.cb_genero.setObjectName(u"cb_genero")
        self.cb_genero.setMinimumSize(QSize(130, 30))
        self.cb_genero.setMaximumSize(QSize(130, 25))
        self.cb_genero.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-style: None;\n"
"border-radius: 5px;")

        self.verticalLayout_5.addWidget(self.cb_genero)


        self.gridLayout.addLayout(self.verticalLayout_5, 0, 2, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_cadastrar = QPushButton(self.frame_2)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setMinimumSize(QSize(110, 40))
        self.btn_cadastrar.setMaximumSize(QSize(110, 40))
        font1 = QFont()
        font1.setFamily(u"Bell MT")
        font1.setPointSize(11)
        self.btn_cadastrar.setFont(font1)
        self.btn_cadastrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar.setStyleSheet(u"QPushButton{\n"
"border-style: solid;\n"
"selection-color: rgb(255, 0, 0);\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-style: solid;\n"
"selection-color: rgb(255, 0, 0);\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout.addWidget(self.btn_cadastrar)

        self.btn_irtabela = QPushButton(self.frame_2)
        self.btn_irtabela.setObjectName(u"btn_irtabela")
        self.btn_irtabela.setMinimumSize(QSize(110, 40))
        self.btn_irtabela.setMaximumSize(QSize(110, 40))
        self.btn_irtabela.setFont(font1)
        self.btn_irtabela.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_irtabela.setStyleSheet(u"QPushButton{\n"
"border-style: solid;\n"
"selection-color: rgb(255, 0, 0);\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(0, 51, 102);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-style: solid;\n"
"selection-color: rgb(255, 0, 0);\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout.addWidget(self.btn_irtabela)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 3)


        self.verticalLayout_6.addWidget(self.frame_2)

        self.pg_inicial.addWidget(self.formulario)
        self.ver_alunos = QWidget()
        self.ver_alunos.setObjectName(u"ver_alunos")
        self.verticalLayout_2 = QVBoxLayout(self.ver_alunos)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.cb_genero2 = QComboBox(self.ver_alunos)
        self.cb_genero2.addItem("")
        self.cb_genero2.addItem("")
        self.cb_genero2.addItem("")
        self.cb_genero2.setObjectName(u"cb_genero2")
        self.cb_genero2.setMinimumSize(QSize(130, 30))
        self.cb_genero2.setMaximumSize(QSize(130, 30))
        self.cb_genero2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-style: None;\n"
"border-radius: 5px;")

        self.horizontalLayout_13.addWidget(self.cb_genero2)

        self.entry_pesquisar = QLineEdit(self.ver_alunos)
        self.entry_pesquisar.setObjectName(u"entry_pesquisar")
        self.entry_pesquisar.setMinimumSize(QSize(0, 30))
        self.entry_pesquisar.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.entry_pesquisar.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.entry_pesquisar)

        self.btn_pesquisar = QPushButton(self.ver_alunos)
        self.btn_pesquisar.setObjectName(u"btn_pesquisar")
        self.btn_pesquisar.setMinimumSize(QSize(100, 30))
        self.btn_pesquisar.setMaximumSize(QSize(100, 30))
        self.btn_pesquisar.setFont(font1)
        self.btn_pesquisar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pesquisar.setStyleSheet(u"QPushButton{\n"
"border-style: solid;\n"
"selection-color: rgb(255, 0, 0);\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(0, 51, 102);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-style: solid;\n"
"selection-color: rgb(255, 0, 0);\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 5px;\n"
"}")

        self.horizontalLayout_13.addWidget(self.btn_pesquisar)


        self.verticalLayout_2.addLayout(self.horizontalLayout_13)

        self.tb_alunos = QTableWidget(self.ver_alunos)
        if (self.tb_alunos.columnCount() < 4):
            self.tb_alunos.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_alunos.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_alunos.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_alunos.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tb_alunos.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tb_alunos.setObjectName(u"tb_alunos")
        self.tb_alunos.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-style: None;\n"
"border-radius: 5px;")
        self.tb_alunos.horizontalHeader().setDefaultSectionSize(130)

        self.verticalLayout_2.addWidget(self.tb_alunos)

        self.btn_voltar = QPushButton(self.ver_alunos)
        self.btn_voltar.setObjectName(u"btn_voltar")
        self.btn_voltar.setMinimumSize(QSize(100, 30))
        self.btn_voltar.setMaximumSize(QSize(100, 30))
        self.btn_voltar.setFont(font1)
        self.btn_voltar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_voltar.setStyleSheet(u"QPushButton{\n"
"border-style: solid;\n"
"selection-color: rgb(255, 0, 0);\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(0, 51, 102);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-style: solid;\n"
"selection-color: rgb(255, 0, 0);\n"
"border-width: 1px;\n"
"border-color: rgb(0, 51, 102);\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 5px;\n"
"}")

        self.verticalLayout_2.addWidget(self.btn_voltar)

        self.pg_inicial.addWidget(self.ver_alunos)

        self.verticalLayout.addWidget(self.pg_inicial)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pg_inicial.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Estrutura de dados II", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.entry_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Idade", None))
        self.entry_idade.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Idade", None))
        self.cb_genero.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione o g\u00eanero", None))
        self.cb_genero.setItemText(1, QCoreApplication.translate("MainWindow", u"Masculino", None))
        self.cb_genero.setItemText(2, QCoreApplication.translate("MainWindow", u"Feminino", None))

        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.btn_irtabela.setText(QCoreApplication.translate("MainWindow", u"Ir para tabela", None))
        self.cb_genero2.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione o g\u00eanero", None))
        self.cb_genero2.setItemText(1, QCoreApplication.translate("MainWindow", u"Masculino", None))
        self.cb_genero2.setItemText(2, QCoreApplication.translate("MainWindow", u"Feminino", None))

        self.entry_pesquisar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        self.btn_pesquisar.setText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        ___qtablewidgetitem = self.tb_alunos.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tb_alunos.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem2 = self.tb_alunos.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Idade", None));
        ___qtablewidgetitem3 = self.tb_alunos.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"G\u00eanero", None));
        self.btn_voltar.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
    # retranslateUi


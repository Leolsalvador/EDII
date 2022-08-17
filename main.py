from exercicio import Ui_MainWindow
import sys
from PySide2.QtWidgets import ( QApplication,QMainWindow,  QTableWidgetItem, QWidget)
from database import DataBase
import pymsgbox as a

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Cadastramento")

        self.btn_voltar.clicked.connect(lambda: self.pg_inicial.setCurrentWidget(self.formulario))
        self.btn_irtabela.clicked.connect(lambda: self.pg_inicial.setCurrentWidget(self.ver_alunos))

        self.btn_cadastrar.clicked.connect(self.cadastrar)
        self.btn_irtabela.clicked.connect(self.ver_tabela)
        self.btn_pesquisar.clicked.connect(self.pesquisar)

    def cadastrar(self):
        self.n = self.entry_nome.text()
        self.i = self.entry_idade.text()
        self.g = self.cb_genero.currentText()

        db = DataBase()
        db.conecta()
        db.cadastrar(self.n, self.i, self.g)
        db.close_connection()
        a.alert("Aluno cadastrado com sucesso","Cadastrado")

    def ver_tabela(self):
        db = DataBase()
        db.conecta()
        self.todos = db.ver_tabela()

        window.tb_alunos.setRowCount(len(self.todos))
        window.tb_alunos.setColumnCount(4)

        for i in range (0, len(self.todos)):
            for j in range(0, 4):
                window.tb_alunos.setItem(i,j,QTableWidgetItem(str(self.todos[i][j])))
        db.close_connection()

    def pesquisar(self):
        self.p = self.entry_pesquisar.text()
        self.gf = self.cb_genero2.currentText()

        db = DataBase()
        db.conecta()
        self.filtro = db.filtro(self.p, self.gf)

        window.tb_alunos.setRowCount(len(self.filtro))
        window.tb_alunos.setColumnCount(4)

        for i in range (0, len(self.filtro)):
            for j in range(0, 4):
                window.tb_alunos.setItem(i,j,QTableWidgetItem(str(self.filtro[i][j])))
        db.close_connection()

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
    

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox
from PyQt5.QtGui import QFont, QColor, QPalette

class VentanaRegistro(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro de Usuario")
        self.setFixedSize(300, 300)
        
        self.init_ui()

    def init_ui(self):
        # Crear campos de entrada
        self.label_nombre = QLabel("Nombre:", self)
        self.entry_nombre = QLineEdit(self)

        self.label_correo = QLabel("Correo electrónico:", self)
        self.entry_correo = QLineEdit(self)

        self.label_contraseña = QLabel("Contraseña:", self)
        self.entry_contraseña = QLineEdit(self)
        self.entry_contraseña.setEchoMode(QLineEdit.Password)

        # Crear botón de registro
        self.btn_registrar = QPushButton("Registrar", self)
        self.btn_registrar.clicked.connect(self.registrar_usuario)

        # Crear layout vertical
        layout = QVBoxLayout()
        layout.addWidget(self.label_nombre)
        layout.addWidget(self.entry_nombre)
        layout.addWidget(self.label_correo)
        layout.addWidget(self.entry_correo)
        layout.addWidget(self.label_contraseña)
        layout.addWidget(self.entry_contraseña)
        layout.addWidget(self.btn_registrar)

        # Crear widget contenedor y establecer el layout
        widget = QWidget()
        widget.setLayout(layout)

        # Establecer el widget contenedor como el widget central de la ventana
        self.setCentralWidget(widget)

        # Aplicar estilos
        self.setStyleSheet(
            "QMainWindow { background-color: #FFFFFF; }"
            "QLabel { color: #333333; }"
            "QLineEdit { background-color: #F2F2F2; border: 1px solid #E5E5E5; border-radius: 3px; padding: 4px; }"
            "QPushButton { background-color: #4CAF50; color: #FFFFFF; border: none; border-radius: 3px; padding: 8px; }"
            "QPushButton:hover { background-color: #45A049; }"
        )

    def registrar_usuario(self):
        nombre = self.entry_nombre.text()
        correo = self.entry_correo.text()
        contraseña = self.entry_contraseña.text()

        # Verificar campos vacíos
        if not nombre or not correo or not contraseña:
            QMessageBox.critical(self, "Error de registro", "Error: Todos los campos deben estar llenos.")
            return

        # Verificar si el usuario ya está registrado
        if correo in usuarios:
            QMessageBox.critical(self, "Error de registro", "Error: el correo electrónico ya está registrado.")
        else:
            # Registrar nuevo usuario
            usuarios[correo] = {"nombre": nombre, "contraseña": contraseña}
            QMessageBox.information(self, "Registro exitoso", "Usuario registrado correctamente.")
            self.limpiar_campos()

    def limpiar_campos(self):
        self.entry_nombre.clear()
        self.entry_correo.clear()
        self.entry_contraseña.clear()

class VentanaInicioSesion(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inicio de Sesión")
        self.setFixedSize(300, 200)
        
        self.init_ui()

    def init_ui(self):
        # Crear campos de entrada
        self.label_correo = QLabel("Correo electrónico:", self)
        self.entry_correo = QLineEdit(self)

        self.label_contraseña = QLabel("Contraseña:", self)
        self.entry_contraseña = QLineEdit(self)
        self.entry_contraseña.setEchoMode(QLineEdit.Password)

        # Crear botón de inicio de sesión
        self.btn_iniciar_sesion = QPushButton("Iniciar sesión", self)
        self.btn_iniciar_sesion.clicked.connect(self.iniciar_sesion)

        # Crear layout vertical
        layout = QVBoxLayout()
        layout.addWidget(self.label_correo)
        layout.addWidget(self.entry_correo)
        layout.addWidget(self.label_contraseña)
        layout.addWidget(self.entry_contraseña)
        layout.addWidget(self.btn_iniciar_sesion)

        # Crear widget contenedor y establecer el layout
        widget = QWidget()
        widget.setLayout(layout)

        # Establecer el widget contenedor como el widget central de la ventana
        self.setCentralWidget(widget)

        # Aplicar estilos
        self.setStyleSheet(
            "QMainWindow { background-color: #FFFFFF; }"
            "QLabel { color: #333333; }"
            "QLineEdit { background-color: #F2F2F2; border: 1px solid #E5E5E5; border-radius: 3px; padding: 4px; }"
            "QPushButton { background-color: #4CAF50; color: #FFFFFF; border: none; border-radius: 3px; padding: 8px; }"
            "QPushButton:hover { background-color: #45A049; }"
        )

    def iniciar_sesion(self):
        correo = self.entry_correo.text()
        contraseña = self.entry_contraseña.text()

        # Verificar campos vacíos
        if not correo or not contraseña:
            QMessageBox.critical(self, "Error de inicio de sesión", "Error: Todos los campos deben estar llenos.")
            return

        # Verificar si el usuario existe y la contraseña es correcta
        if correo in usuarios and usuarios[correo]["contraseña"] == contraseña:
            QMessageBox.information(self, "Inicio de sesión exitoso", "Inicio de sesión exitoso.")
            self.limpiar_campos()
        else:
            QMessageBox.critical(self, "Error de inicio de sesión", "Error: correo o contraseña incorrectos.")

    def limpiar_campos(self):
        self.entry_correo.clear()
        self.entry_contraseña.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Base de datos ficticia de usuarios registrados
    usuarios = {}

    ventana_registro = VentanaRegistro()
    ventana_inicio_sesion = VentanaInicioSesion()

    ventana_principal = QMainWindow()
    ventana_principal.setWindowTitle("Sistema de Registro y Inicio de Sesión")
    ventana_principal.setFixedSize(300, 200)

    # Crear botón de registro
    btn_registro = QPushButton("Registrar", ventana_principal)
    btn_registro.setStyleSheet("QPushButton { background-color: #1E88E5; color: #FFFFFF; border: none; border-radius: 3px; padding: 8px; }"
                               "QPushButton:hover { background-color: #1565C0; }")
    btn_registro.clicked.connect(ventana_registro.show)

    # Crear botón de inicio de sesión
    btn_inicio_sesion = QPushButton("Iniciar Sesión", ventana_principal)
    btn_inicio_sesion.setStyleSheet("QPushButton { background-color: #1E88E5; color: #FFFFFF; border: none; border-radius: 3px; padding: 8px; }"
                                    "QPushButton:hover { background-color: #1565C0; }")
    btn_inicio_sesion.clicked.connect(ventana_inicio_sesion.show)

    # Crear botón de salida
    btn_salir = QPushButton("Salir", ventana_principal)
    btn_salir.setStyleSheet("QPushButton { background-color: #E53935; color: #FFFFFF; border: none; border-radius: 3px; padding: 8px; }"
                            "QPushButton:hover { background-color: #C62828; }")
    btn_salir.clicked.connect(app.quit)

    # Crear layout vertical
    layout = QVBoxLayout()
    layout.addWidget(btn_registro)
    layout.addWidget(btn_inicio_sesion)
    layout.addWidget(btn_salir)

    # Crear widget contenedor y establecer el layout
    central_widget = QWidget(ventana_principal)
    central_widget.setLayout(layout)
    ventana_principal.setCentralWidget(central_widget)

    ventana_principal.show()
    sys.exit(app.exec_())

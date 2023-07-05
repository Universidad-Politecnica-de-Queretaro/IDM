import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QWidget, \
    QPushButton, QLineEdit, QTextEdit, QTableWidget, QTableWidgetItem


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Inventario")
        self.setGeometry(100, 100, 500, 500)

        self.layout_principal = QVBoxLayout()
        self.layout_busqueda = QHBoxLayout()
        self.layout_tabla = QVBoxLayout()
        self.layout_gestion = QHBoxLayout()
        self.layout_filtros = QHBoxLayout()

        self.label_busqueda = QLabel("Código de Producto:")
        self.input_busqueda = QLineEdit()
        self.boton_buscar = QPushButton("Buscar")
        self.boton_buscar.clicked.connect(self.buscar_producto)

        self.tabla_productos = QTableWidget()
        self.tabla_productos.setColumnCount(4)
        self.tabla_productos.setHorizontalHeaderLabels(["Código", "Nombre", "Descripción", "Stock"])
        self.tabla_productos.setEditTriggers(QTableWidget.NoEditTriggers)

        self.label_gestion = QLabel("Gestión de Inventario:")
        self.input_codigo = QLineEdit()
        self.input_nombre = QLineEdit()
        self.input_descripcion = QLineEdit()
        self.input_stock = QLineEdit()
        self.boton_agregar = QPushButton("Agregar")
        self.boton_agregar.clicked.connect(self.agregar_producto)
        self.boton_modificar = QPushButton("Modificar")
        self.boton_modificar.clicked.connect(self.modificar_producto)
        self.boton_vender = QPushButton("Vender")
        self.boton_eliminar = QPushButton("Eliminar")

        self.label_filtros = QLabel("Filtrar por:")
        self.input_filtro = QLineEdit()
        self.boton_filtrar = QPushButton("Filtrar")
        self.boton_filtrar.clicked.connect(self.filtrar_productos)

        self.layout_busqueda.addWidget(self.label_busqueda)
        self.layout_busqueda.addWidget(self.input_busqueda)
        self.layout_busqueda.addWidget(self.boton_buscar)

        self.layout_tabla.addWidget(self.tabla_productos)

        self.layout_gestion.addWidget(self.label_gestion)
        self.layout_gestion.addWidget(self.input_codigo)
        self.layout_gestion.addWidget(self.input_nombre)
        self.layout_gestion.addWidget(self.input_descripcion)
        self.layout_gestion.addWidget(self.input_stock)
        self.layout_gestion.addWidget(self.boton_agregar)
        self.layout_gestion.addWidget(self.boton_modificar)
        self.layout_gestion.addWidget(self.boton_vender)
        self.layout_gestion.addWidget(self.boton_eliminar)

        self.layout_filtros.addWidget(self.label_filtros)
        self.layout_filtros.addWidget(self.input_filtro)
        self.layout_filtros.addWidget(self.boton_filtrar)

        self.layout_principal.addLayout(self.layout_busqueda)
        self.layout_principal.addLayout(self.layout_tabla)
        self.layout_principal.addLayout(self.layout_gestion)
        self.layout_principal.addLayout(self.layout_filtros)

        self.widget_principal = QWidget()
        self.widget_principal.setLayout(self.layout_principal)
        self.setCentralWidget(self.widget_principal)

    def buscar_producto(self):
        codigo = self.input_busqueda.text()
        # Lógica para buscar el producto en el inventario y mostrarlo en los campos correspondientes

    def agregar_producto(self):
        codigo = self.input_codigo.text()
        nombre = self.input_nombre.text()
        descripcion = self.input_descripcion.text()
        stock = self.input_stock.text()
        # Lógica para agregar el producto al inventario

    def modificar_producto(self):
        codigo = self.input_codigo.text()
        nombre = self.input_nombre.text()
        descripcion = self.input_descripcion.text()
        stock = self.input_stock.text()
        # Lógica para modificar el producto en el inventario

    def filtrar_productos(self):
        filtro = self.input_filtro.text()
        # Lógica para filtrar los productos en el inventario

    def cargar_productos(self):
        # Lógica para cargar los productos existentes en la tabla
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())

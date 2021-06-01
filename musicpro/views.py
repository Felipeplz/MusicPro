from django.shortcuts import render
from musicpro.models import SQLProductos, SQLUsuarios, SQLProductos, SQLVentas, SQLItemVentas, SQLEstadoPedido
import pyodbc

# Create your views here.
def usuariosTodos(request):
    conn = pyodbc.connect('Driver={sql server};'
                        'Server=RENO-PC\SQLEXPRESS;'
                        'Database=MusicPro;'
                        'Trusted_Connection=yes')
    cursor = conn.cursor()
    result = cursor.execute("SELECT USUARIO.id_usuario, USUARIO.mail, USUARIO.rut, USUARIO.dv_rut, USUARIO.nombre, USUARIO.direccion," 
     "ROL.nombre_rol FROM USUARIO INNER JOIN ROL ON USUARIO.id_rol = ROL.id_rol ORDER BY USUARIO.id_usuario ASC").fetchall()
    return render(request, 'Usuarios_lista.html', {'SQLUsuarios':result})

def productosTodos(request):
    conn = pyodbc.connect('Driver={sql server};'
                        'Server=RENO-PC\SQLEXPRESS;'
                        'Database=MusicPro;'
                        'Trusted_Connection=yes')
    cursor = conn.cursor()
    result = cursor.execute("SELECT * FROM PRODUCTO ORDER BY id_producto ASC").fetchall()
    return render(request, 'Productos_Lista.html', {'SQLProductos':result})

def productosCarrito(request):
    conn = pyodbc.connect('Driver={sql server};'
                        'Server=RENO-PC\SQLEXPRESS;'
                        'Database=MusicPro;'
                        'Trusted_Connection=yes')
    cursor = conn.cursor()
    result = cursor.execute("SELECT * FROM PRODUCTO ORDER BY id_producto ASC").fetchall()
    return render(request, 'indexCarrito.html', {'SQLCarrito':result})


def seguimientoBodeguero(request):
    conn = pyodbc.connect('Driver={sql server};'
                        'Server=RENO-PC\SQLEXPRESS;'
                        'Database=MusicPro;'
                        'Trusted_Connection=yes')
    cursor = conn.cursor()
    result = cursor.execute("SELECT V.id_venta, IV.cantidad, U.nombre, P.tipo, EP.fecha_estado,EP.estado FROM VENTA V JOIN USUARIO U ON U.id_usuario = V.id_cliente JOIN ESTADO_PEDIDO EP ON EP.id_venta = V.id_venta JOIN ITEM_VENTA IV ON V.id_venta = IV.id_venta JOIN PRODUCTO P ON IV.id_producto = P.id_producto ORDER BY V.id_venta ASC").fetchall()
    return render(request, 'Seguimiento_bodeguero_pedidos_generales.html', {'SQLBodeguero':result})

def seguimientoBodeguero2(request):
    conn = pyodbc.connect('Driver={sql server};'
                        'Server=RENO-PC\SQLEXPRESS;'
                        'Database=MusicPro;'
                        'Trusted_Connection=yes')
    cursor = conn.cursor()
    result = cursor.execute("SELECT V.id_venta, IV.cantidad, U.nombre, P.tipo, EP.fecha_estado,EP.estado FROM VENTA V JOIN USUARIO U ON U.id_usuario = V.id_cliente JOIN ESTADO_PEDIDO EP ON EP.id_venta = V.id_venta JOIN ITEM_VENTA IV ON V.id_venta = IV.id_venta JOIN PRODUCTO P ON IV.id_producto = P.id_producto WHERE U.nombre = 'ELNOMBRE DEL USUARIO' ORDER BY U.nombre ASC").fetchall()
    return render(request, 'Seguimiento_bodeguero_mis_pedidos.html', {'SQLBodeguero2':result})

#Cambiar consulta de seguimiento bodeguero 2 para dejarlos solo los pedidos del usuario bodeguero#

def promociones(request):
    conn = pyodbc.connect('Driver={sql server};'
                        'Server=RENO-PC\SQLEXPRESS;'
                        'Database=MusicPro;'
                        'Trusted_Connection=yes')
    cursor = conn.cursor()
    result = cursor.execute("SELECT * FROM PRODUCTO ORDER BY NOMBRE ASC").fetchall()
    return render(request, 'indexPromocionesLista.html', {'SQLBodeguero2':result}) 

#Cambiar consulta promociones y preguntar dudas#   
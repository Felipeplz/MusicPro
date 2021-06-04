from django.shortcuts import redirect, render
from musicpro.models import SQLProductos, SQLUsuarios, SQLProductos, SQLVentas, SQLItemVentas, SQLEstadoPedido
import pyodbc

# Create your views here.
def Conectar():
    conn = pyodbc.connect('Driver={sql server};'
                        'Server=###BASEDEDATOS###;'
                        'Database=MusicPro;'
                        'Trusted_Connection=yes')
    return conn.cursor()

def seguimientoContador(request):
    result = Conectar().execute("SELECT * FROM SEG_CONTADOR ORDER BY id_seg_cont ASC").fetchall()
    return render(request, 'Seguimiento_contador.html', {'SQLSegCont':result})

def seguimientoCliente(request):
    result = Conectar().execute("SELECT * FROM SEG_CLIENTE ORDER BY id_seg_client ASC").fetchall()
    return render(request, 'Seguimiento_cliente.html', {'SQLSegClient':result})

def seguimientoVendedor(request):
    result = Conectar().execute("SELECT * FROM SEG_VENDEDOR ORDER BY id_seg_vend ASC").fetchall()
    return render(request, 'Seguimiento_vendedor.html', {'SQLSegVend':result})

def ventaDatos(request):
    result = Conectar().execute("SELECT * FROM VENTA_DATOS ORDER BY id_vent_dat ASC").fetchall()
    return render(request, 'Venta_Datos.html', {'SQLVentDat':result})

def VentasConfirmar(request):
    result = Conectar().execute("SELECT * FROM VENT_CONFIRMAR ORDER BY id_vent_confir ASC").fetchall()
    return render(request, 'Ventas_Confirmar.html', {'SQLVentConfir':result})

def viewUsuarios(request):
    result = Conectar().execute("SELECT USUARIO.id_usuario, USUARIO.mail, USUARIO.rut, USUARIO.dv_rut, USUARIO.nombre, USUARIO.direccion," 
     "ROL.nombre_rol FROM USUARIO INNER JOIN ROL ON USUARIO.id_rol = ROL.id_rol ORDER BY USUARIO.id_usuario ASC").fetchall()
    return render(request, 'Usuarios_lista.html', {'SQLUsuarios':result})

def viewCatalogo(request, **kwargs):
    if (request.path == "/"):
        return redirect('/catalogo')
    tab = kwargs.get('tab')
    if (tab == None):
        tab = "todos"
        query = ""
    else:
        query = f"WHERE categoria = '{tab}'"
    result = Conectar().execute(f"SELECT * FROM PRODUCTO {query} ORDER BY id_producto ASC").fetchall()
    return render(request, 'Catalogo_Producto.html', {'SQLProductos':result, 'tab': tab})

# def productosCarrito(request):
#     result = Conectar().execute("SELECT * FROM PRODUCTO ORDER BY id_producto ASC").fetchall()
#     return render(request, 'indexCarrito.html', {'SQLCarrito':result})


def seguimientoBodeguero(request):
    result = Conectar().execute("SELECT V.id_venta, IV.cantidad, U.nombre, P.tipo, EP.fecha_estado,EP.estado FROM VENTA V JOIN USUARIO U ON U.id_usuario = V.id_cliente JOIN ESTADO_PEDIDO EP ON EP.id_venta = V.id_venta JOIN ITEM_VENTA IV ON V.id_venta = IV.id_venta JOIN PRODUCTO P ON IV.id_producto = P.id_producto ORDER BY V.id_venta ASC").fetchall()
    return render(request, 'Seguimiento_bodeguero_pedidos_generales.html', {'SQLBodeguero':result})

def seguimientoBodeguero2(request):
    result = Conectar().execute("SELECT V.id_venta, IV.cantidad, U.nombre, P.tipo, EP.fecha_estado,EP.estado FROM VENTA V JOIN USUARIO U ON U.id_usuario = V.id_cliente JOIN ESTADO_PEDIDO EP ON EP.id_venta = V.id_venta JOIN ITEM_VENTA IV ON V.id_venta = IV.id_venta JOIN PRODUCTO P ON IV.id_producto = P.id_producto WHERE U.nombre = 'ELNOMBRE DEL USUARIO' ORDER BY U.nombre ASC").fetchall()
    return render(request, 'Seguimiento_bodeguero_mis_pedidos.html', {'SQLBodeguero2':result})

#Cambiar consulta de seguimiento bodeguero 2 para dejarlos solo los pedidos del usuario bodeguero#

def promociones(request):
    result = Conectar().execute("SELECT [dbo].[PRODUCTO].[id_producto]"
                                ",[codigo_producto]"
                                ",[nombre]"
                                ",[marca]"
                                ",[precio]"
                                ",[tipo]"
                                ",[subtipo]"
                                ",[categoria]"
                                ",[cantidad_min]"
                                ",[descuento]"
                            "FROM [dbo].[PRODUCTO] JOIN"
                            "[dbo].[PROMOCION] ON [dbo].[PRODUCTO].[id_producto] = [dbo].[PROMOCION].[id_producto]"
                            "WHERE GETDATE() BETWEEN [fecha_desde] AND [fecha_hasta]").fetchall()
    return render(request, 'indexPromocionesLista.html', {'SQLPromo':result})

from django.shortcuts import redirect, render
from musicpro.models import SQLProductos
import pyodbc

# Create your views here.

def Conectar():
    conn = pyodbc.connect('Driver={sql server};'
                        'Server=26.230.2.16\FELIPE;'
                        'Database=MusicPro;'
                        'UID=django-user;'
                        'PWD=%.ZSix:)R:NN5RT')
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

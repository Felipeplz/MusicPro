from django.shortcuts import redirect, render
from musicpro.models import SQLDespachos,SQLEstadoPedidos,SQLItemVentas,SQLPagos,SQLProductos,SQLPromociones,SQLRoles,SQLSucursales,SQLUsuarios,SQLVentas
from .conn import *
import pyodbc

def Conectar():
    conn = pyodbc.connect('Driver={ODBC DRIVER 17 FOR SQL SERVER};'
                        'Server=DESKTOP-IJJK685;'
                        'Database=MusicPro;'
                        'Trusted_Connection=yes')
    return conn.cursor()
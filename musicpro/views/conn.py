from django.shortcuts import redirect, render
from musicpro.models import SQLDespachos,SQLEstadoPedidos,SQLItemVentas,SQLPagos,SQLProductos,SQLPromociones,SQLRoles,SQLSucursales,SQLUsuarios,SQLVentas
from .conn import *
import pyodbc

def Conectar():
    conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                        'Server=LAPTOP-R0CJDD69\PIA;'
                        'Database=MusicPro;'
                        'Trusted_Connection=yes')
    return conn.cursor()
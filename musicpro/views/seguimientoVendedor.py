from .conn import *

def seguimientoVendedor(request):
    result = Conectar().execute("SELECT v.id_venta AS Pedido, COUNT(iv.cantidad) AS cantidad, CONVERT(date,ep.fecha_estado) AS Fecha, CONVERT(time(0),ep.fecha_estado) AS Hora, (CASE WHEN v.id_sucursal_retiro IS NOT NULL THEN 'Retiro' ELSE 'Despacho' END)  AS Tipo, ep.estado AS Estado, u.nombre AS Encargado FROM ESTADO_PEDIDO AS ep JOIN VENTA AS v ON ep.id_venta = v.id_venta JOIN ITEM_VENTA AS iv ON v.id_venta = iv.id_venta JOIN USUARIO AS u ON ep.id_encargado = u.id_usuario GROUP BY v.id_venta, ep.estado, ep.fecha_estado, u.nombre, v.id_sucursal_retiro ORDER BY ep.fecha_estado ASC").fetchall()
    return render(request, 'seguimientoVendedor.html', {'SQLSegVendedor':result})
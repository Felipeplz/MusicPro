from .conn import *
from .moneda import getLocale, getIP
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.core.paginator import Paginator


def viewCatalogo(request, **kwargs):
    if not request.user.is_authenticated:
        user = authenticate(
            request,
            username="anon" + getIP(request),
            password=")42&&6?-5'{T52^4sW=`72mASt}j?p8d6>!uyS's8FtcasvVAuM#cw(*5FpRw_8?",
        )
        if user is None:
            user = User.objects.create_user(
                "anon" + getIP(request),
                "anon" + getIP(request),
                ")42&&6?-5'{T52^4sW=`72mASt}j?p8d6>!uyS's8FtcasvVAuM#cw(*5FpRw_8?",
            )
        usuario = Usuario.objects.get_or_create(
            mail=user.username, rut="1", rol="Cliente"
        )
        auth_login(request, user)
    local = getLocale(request)
    if not request.path.startswith("/catalogo/"):
        return redirect("../../catalogo/")
    usuario = getUsuario(request.user.email)
    catalogo = Producto.objects.all()
    tab = kwargs.get("tab")
    if tab == None:
        tab = "todos"
    else:
        if tab == "cuerda":
            filtro = "Instrumentos de Cuerdas"
        elif tab == "percusion":
            filtro = "Percusión"
        elif tab == "amplificadores":
            filtro = "Amplificadores"
        elif tab == "accesorios":
            filtro = "Accesorios varios"
        else:
            return redirect("../../catalogo/")
        catalogo = catalogo.filter(categoria=filtro)
    pag = kwargs.get("pag")
    if pag == None or pag < 1:
        pag = 1
    paginador = Paginator(catalogo, 6)
    if pag > paginador.num_pages:
      return redirect("../../catalogo/")
    pagina = paginador.page(pag)
    return render(
        request,
        "catalogo.html",
        {
            "catalogo": pagina,
            "pags": paginador.page_range,
            "tab": tab,
            "local": local,
            "usuario": usuario,
        },
    )

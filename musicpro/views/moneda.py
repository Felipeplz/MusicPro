from .conn import *
import geoip2.database
from country_currencies import get_by_country
from urllib.request import urlopen
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def getIP(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def getLocale(request):
    ip = getIP(request)
    if ip == "127.0.0.1":
        return "CLP"

    reader = geoip2.database.Reader(BASE_DIR / 'GeoLite2-City.mmdb')
    response = reader.city(ip)
    return get_by_country(response.country.iso_code)[0]
    
def convertir(moneda, total):
    req = urlopen('https://currencyapi.net/api/v1/rates?key=1KHhYSaYoxPQwsFirO0zMktXRHlZPNJUgpoa')
    #req = open(BASE_DIR / 'rates.json')
    resultadoJSON = json.load(req)
    coeficiente = (total/resultadoJSON['rates']['CLP'])
    valor = (coeficiente*resultadoJSON['rates'][moneda])
    return round(valor, 2)
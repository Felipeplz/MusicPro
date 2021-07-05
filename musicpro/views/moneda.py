import os
import geoip2.database
from country_currencies import get_by_country
from urllib.request import urlopen
import json
from pathlib import Path
from datetime import date, timedelta

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
    path = str(BASE_DIR)
    try:
      req = open(path + '\\rates' + str(date.today()) +  '.json')
    except:
      print('Creando rates...')
      try:
        for p in BASE_DIR.glob("*.json"):
          p.unlink()
      except:
        pass
      req = open(path + '\\rates' + str(date.today()) +  '.json', 'w')
      req.write(urlopen('https://currencyapi.net/api/v1/rates?key=1KHhYSaYoxPQwsFirO0zMktXRHlZPNJUgpoa').read().decode('utf-8'))
      req.close
      req = open(path + '\\rates' + str(date.today()) +  '.json', 'r')
    resultadoJSON = json.load(req)
    req.close()
    if ip == "127.0.0.1":
        response = "CLP"
    else:
        reader = geoip2.database.Reader(BASE_DIR / 'GeoLite2-City.mmdb')
        response = reader.city(ip)
        response = get_by_country(response.country.iso_code)[0]
    if not response in resultadoJSON['rates']:
      response = "USD"
    return response
    
def convertir(moneda, total):
    path = str(BASE_DIR)
    try:
      req = open(path + '\\rates' + str(date.today()) +  '.json')
    except:
      print('Creando rates...')
      try:
        for p in BASE_DIR.glob("*.json"):
          p.unlink()
      except:
        pass
      req = open(path + '\\rates' + str(date.today()) +  '.json', 'w')
      req.write(urlopen('https://currencyapi.net/api/v1/rates?key=1KHhYSaYoxPQwsFirO0zMktXRHlZPNJUgpoa').read().decode('utf-8'))
      req.close
      req = open(path + '\\rates' + str(date.today()) +  '.json', 'r')
    resultadoJSON = json.load(req)
    req.close()
    coeficiente = (total/resultadoJSON['rates']['CLP'])
    if not moneda in resultadoJSON['rates']:
      moneda = "USD"
    valor = (coeficiente*resultadoJSON['rates'][moneda])
    return round(valor, 2)
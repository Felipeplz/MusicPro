from django.test import SimpleTestCase
from django.urls import reverse, resolve 
from musicpro.views import *

class TestUrls(SimpleTestCase):

    def test_catologo_url_is_resolves(self):
        url = reverse('catalogo')                        
        self.assertEquals(resolve(url).func, viewCatalogo)

    def test_producto_url_is_resolves(self):
        url = reverse('producto')   
        self.assertEquals(resolve(url).func, viewProducto)

    def test_productoid_url_is_resolves(self):
        url = reverse('productoid', args=['1'])   
        self.assertEquals(resolve(url).func, viewProducto)

    def test_nuevoproducto_url_is_resolves(self):
        url = reverse('nuevoproducto')   
        self.assertEquals(resolve(url).func, newProducto)
    
    def test_editarproducto_url_is_resolves(self):
        url = reverse('editarproducto', args=['1'])   
        self.assertEquals(resolve(url).func, editProducto)
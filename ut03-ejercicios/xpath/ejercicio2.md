# Ejercicio 2. Tienda de electrónica.
```
<electronics>
  <item id="201">
    <name>Smartphone</name>
    <brand>BrandX</brand>
    <price currency="USD">699.99</price>
    <stock>50</stock>
  </item>
  <item id="202">
    <name>Laptop</name>
    <brand>BrandY</brand>
    <price currency="USD">999.99</price>
    <stock>10</stock>
  </item>
  <item id="203">
    <name>Tablet</name>
    <brand>BrandX</brand>
    <price currency="USD">399.99</price>
    <stock>25</stock>
  </item>
  <item id="204">
    <name>Headphones</name>
    <brand>BrandZ</brand>
    <price currency="USD">199.99</price>
    <stock>100</stock>
  </item>
</electronics>
```

Pregunta 1. Selecciona todos los nombres de productos. `//name/text()`

Pregunta 2. Selecciona los productos de la marca "BrandX". `//item[brand="BrandX"]`

Pregunta 3. Selecciona el producto más barato. `//item[price=min(//price)]`

Pregunta 4. Selecciona el producto más caro. `//item[price=max(//price)]`

Pregunta 5. Selecciona los nombres y precios de productos con más de 30 unidades en stock. `//item[stock > 30]/(name/text() | price/text())`

Pregunta 6. Selecciona el atributo currency de todos los precios. `//@currency`

Pregunta 7. Cuenta cuántos productos hay en stock con menos de 20 unidades. `count(//item[stock < 20])`

Pregunta 8. Selecciona los nombres de todos los productos cuyo precio sea mayor a 500. `//item[price > 500]/name/text()`

Pregunta 9. Selecciona los nombres de productos con el atributo id mayor a 202. `//item[price > 500]/name/text()`

Pregunta 10. Selecciona todos los nodos completos de productos con "BrandZ". `//item[brand="BrandZ"]`
# Ejercicio 5. Inventario de Productos
```
<inventory>
  <product id="P001">
    <name>Chair</name>
    <category>Furniture</category>
    <price currency="USD">49.99</price>
    <stock>200</stock>
  </product>
  <product id="P002">
    <name>Table</name>
    <category>Furniture</category>
    <price currency="USD">129.99</price>
    <stock>50</stock>
  </product>
  <product id="P003">
    <name>Lamp</name>
    <category>Lighting</category>
    <price currency="USD">19.99</price>
    <stock>100</stock>
  </product>
  <product id="P004">
    <name>Desk</name>
    <category>Furniture</category>
    <price currency="USD">249.99</price>
    <stock>20</stock>
  </product>
  <product id="P005">
    <name>Ceiling Light</name>
    <category>Lighting</category>
    <price currency="USD">79.99</price>
    <stock>30</stock>
  </product>
</inventory>
```

Pregunta 1. Selecciona los nombres de todos los productos. `//name/text()`

Pregunta 2. Selecciona todos los productos de la categoría "Furniture". `//product[category="Furniture"]`

Pregunta 3. Selecciona el precio del producto "Lamp". `//product[name="Lamp"]/price/text()`

Pregunta 4. Cuenta cuántos productos tienen más de 50 en stock. `count(//product[stock > 50])`

Pregunta 5. Selecciona el producto más caro. `//product[price=max(//price)]`

Pregunta 6. Selecciona los nombres de los productos con menos de 30 en stock. `//product[stock < 30]/name/text()`

Pregunta 7. Selecciona todos los precios en USD. `//price[@currency="USD"]`

Pregunta 8. Selecciona el ID de todos los productos de la categoría "Lighting". `//product[category="Lighting"]/@id`

Pregunta 9. Selecciona el precio del producto más barato. `min(//price)`

Pregunta 10. Selecciona los nombres y precios de todos los productos ordenados por precio. `//name/text() | //price/text()`
**En XPath no se pueden ordenar los productos por precio**
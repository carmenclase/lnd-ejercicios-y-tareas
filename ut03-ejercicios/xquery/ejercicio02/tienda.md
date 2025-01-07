# Ejercicio 2. Tienda

**Pregunta 1.** Devuelve los nombres de todos los productos.
```
for $producto in doc("tienda.xml")/tienda/producto
return $producto/nombre
```
**Pregunta 2.** Devuelve los productos de la categoría "Accesorios".
```
for $producto in doc("tienda.xml")/tienda/producto
where $producto/@categoria = "Accesorios"
return $producto
```
**Pregunta 3.** Calcula el precio total de todos los productos.
```
let $precios := doc("tienda.xml")/tienda/producto/precio
return sum($precios)
```
**Pregunta 4.** Encuentra productos con un precio mayor a 500 USD.
```
for $producto in doc("tienda.xml")/tienda/producto
where $producto/precio > 500
return $producto
```
**Pregunta 5.** Devuelve los productos y sus precios con un descuento del 10%.
```
for $producto in doc("tienda.xml")/tienda/producto
let $descuento := $producto/precio * 0.9
return <producto>
	<nombre>{$producto/nombre}</nombre>
	<descuento>{$descuento}</descuento>
</producto>
```
**Pregunta 6.** Lista los productos ordenados por precio de menor a mayor.
```
for $producto in doc("tienda.xml")/tienda/producto
order by $producto/precio ascending
return $producto
```
**Pregunta 7.** Devuelve los productos de la marca "HP".
```
for $producto in doc("tienda.xml")/tienda/producto
where $producto/marca = "HP"
return $producto
```
**Pregunta 8.** Devuelve los nombres y categorías de los productos como elementos <item>.
```
for $producto in doc("tienda.xml")/tienda/producto
return <item>
    <nombre>{$producto/nombre}</nombre>
    <categoria>{$producto/@categoria}</categoria>
</item>
```
**Pregunta 9.** Encuentra el producto más barato.
```
for $producto in doc("tienda.xml")/tienda/producto
where $producto/precio = min(//precio)
return $producto
```
**Pregunta 10.** Calcula el precio promedio de los productos en la categoría "Computadoras".
```
let $producto := doc("tienda.xml")/tienda/producto[@categoria="Computadoras"]
let $promedio := $producto/precio
return avg($promedio)
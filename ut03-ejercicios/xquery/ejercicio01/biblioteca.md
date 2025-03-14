# Ejercicio 1. Biblioteca

**Pregunta 1.** Devuelve todos los títulos de los libros. 
```
for $libro in doc("biblioteca.xml")/biblioteca/libro 
return $libro/titulo
```
**Pregunta 2.** Devuelve los títulos de libros cuyo precio es mayor a 15. 
```
for $libro in doc("biblioteca.xml")/biblioteca/libro 
where $libro/precio > 15
return $libro/titulo
```
**Pregunta 3.** Lista los autores y sus países de origen.
```
for $libro in doc("biblioteca.xml")/biblioteca/libro 
return ($libro/autor) | ($libro/autor/@pais)
```
**Pregunta 4.** Calcula el precio promedio de los libros.
```
let $promedio := doc("biblioteca.xml")/biblioteca/libro/precio
return avg($promedio)
```
**Pregunta 5.** Devuelve los títulos ordenados alfabéticamente.
```
for $libro in doc("biblioteca.xml")/biblioteca/libro 
order by $libro/titulo ascending
return $libro/titulo
```
**Pregunta 6.** Devuelve los títulos y precios de los libros en formato XML.
```
for $libro in doc("biblioteca.xml")/biblioteca/libro 
return <libro>
    <titulo>{$libro/titulo}</titulo>
    <precio>{$libro/precio}</precio>
</libro>
```
**Pregunta 7.** Encuentra libros del género "Ficción".
```
for $libro in doc("biblioteca.xml")/biblioteca/libro 
where $libro/@genero = "Ficción"
return $libro
```
**Pregunta 8.** Devuelve los libros cuyo autor sea de "EE.UU.".
```
for $libro in doc("biblioteca.xml")/biblioteca/libro 
where $libro/autor/@pais = "EE.UU."
return $libro
```
**Pregunta 9.** Lista los libros y su precio total (precio + 5 USD de impuesto).
```
for $libro in doc("biblioteca.xml")/biblioteca/libro 
let $total := $libro/precio + 5
return <libro>
    <titulo>{$libro/titulo}</titulo>
    <total>{$total}</total>
</libro>
```
**Pregunta 10.** Devuelve el libro más caro en el catálogo.
```
for $libro in doc("biblioteca.xml")/biblioteca/libro 
where $libro/precio = max(//libro/precio)
return ($libro/titulo) | ($libro/precio)
```
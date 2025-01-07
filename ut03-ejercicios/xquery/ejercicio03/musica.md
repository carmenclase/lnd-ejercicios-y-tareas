# Ejercicio 3. Musica

**Pregunta 1.** Devuelve todos los títulos de los álbumes.
```
for $album in doc("musica.xml")/catalogo/album
return $album/titulo
```
**Pregunta 2.** Devuelve los álbumes cuyo precio es mayor a 18.
```
for $album in doc("musica.xml")/catalogo/album
where $album/precio > 18
return $album
```
**Pregunta 3.** Lista los títulos y géneros de todos los álbumes.
```
for $album in doc("musica.xml")/catalogo/album
return ($album/titulo) | ($album/@genero)
```
**Pregunta 4.** Calcula el precio promedio de los álbumes (usa let).
```
let $promedio := doc("musica.xml")/catalogo/album/precio
return avg($promedio)
```
**Pregunta 5.** Encuentra los álbumes de género "Rock".
```
for $album in doc("musica.xml")/catalogo/album
where $album/@genero = "Rock"
return $album
```
**Pregunta 6.** Ordena los álbumes por año de lanzamiento.
```
for $album in doc("musica.xml")/catalogo/album
order by $album/anio ascending
return $album
```
**Pregunta 7.** Devuelve el álbum más caro.
```
for $album in doc("musica.xml")/catalogo/album
where $album/precio = max(//precio)
return $album
```
**Pregunta 8.** Devuelve los títulos y los precios con un descuento del 20%.
```
for $album in doc("musica.xml")/catalogo/album
let $descuento := $album/precio * 0.8
return <album>
	<titulo>{$album/titulo}</titulo>
    <descuento>{$descuento}</descuento>
</album>
```
**Pregunta 9.** Devuelve los álbumes lanzados antes de 1975.
```
for $album in doc("musica.xml")/catalogo/album
where $album/anio < 1975
return $album
```
**Pregunta 10.** Calcula el precio total de todos los álbumes.
```
let $precios := doc("musica.xml")/catalogo/album/precio
return sum($precios)
```
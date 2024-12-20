# Ejercicio Resuelto

Dado el archivo catalogo.xml:
```
<catalogo>
  <producto id="1" categoria="Electrónica">
    <nombre>Portátil</nombre>
    <precio>800</precio>
  </producto>
  <producto id="2" categoria="Electrónica">
    <nombre>Monitor</nombre>
    <precio>200</precio>
  </producto>
  <producto id="3" categoria="Accesorios">
    <nombre>Ratón</nombre>
    <precio>25</precio>
  </producto>
</catalogo>
```

## Ejercicio 1: devuelve los nombres de los productos.

Consulta:
```
for $producto in doc("catalogo.xml")/catalogo/producto
return $producto/nombre
```

Resultado:
```
<nombre>Portátil</nombre>
<nombre>Monitor</nombre>
<nombre>Ratón</nombre>
```

## Ejercicio 2: filtra productos con precio mayor a 100.

Consulta:
```
for $producto in doc("catalogo.xml")/catalogo/producto
where $producto/precio > 100
return $producto/nombre
```

Resultado:
```
<nombre>Portátil</nombre>
<nombre>Monitor</nombre>
```

## Ejercicio 3: ordena los productos por precio de menor a mayor.

Consulta:
```
for $producto in doc("catalogo.xml")/catalogo/producto
order by $producto/precio ascending
return $producto/nombre
```

Resultado:
```
<nombre>Ratón</nombre>
<nombre>Monitor</nombre>
<nombre>Portátil</nombre>
```

## Ejercicio 4: calcula el precio total de todos los productos. 

Consulta:
`sum(doc("catalogo.xml")/catalogo/producto/precio)`

Resultado:
1025

## Ejercicio 5: devuelve los nombres y categorías de los productos.

Consulta:
```
for $producto in doc("catalogo.xml")/catalogo/producto
return <item>
  <nombre>{$producto/nombre}</nombre>
  <categoria>{$producto/@categoria}</categoria>
</item>
```

Resultado:
```
<item>
  <nombre>Portátil</nombre>
  <categoria>Electrónica</categoria>
</item>
<item>
  <nombre>Monitor</nombre>
  <categoria>Electrónica</categoria>
</item>
<item>
  <nombre>Ratón</nombre>
  <categoria>Accesorios</categoria>
</item>
```
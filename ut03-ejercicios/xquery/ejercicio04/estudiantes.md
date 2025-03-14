# Ejercicio 4. Estudiantes

**Pregunta 1.** Devuelve los nombres de los estudiantes.
```
for $estudiante in doc("estudiantes.xml")/estudiantes/estudiante
return $estudiante/nombre
```
**Pregunta 2.** Filtra los estudiantes con una nota mayor a 8.
```
for $estudiante in doc("estudiantes.xml")/estudiantes/estudiante
where $estudiante/nota > 8
return $estudiante
```
**Pregunta 3.** Devuelve los nombres y las carreras de los estudiantes.
```
for $estudiante in doc("estudiantes.xml")/estudiantes/estudiante
return ($estudiante/nombre) | ($estudiante/@carrera)
```
**Pregunta 4.** Calcula la nota promedio de los estudiantes (usa let).
```
let $notas := doc("estudiantes.xml")/estudiantes/estudiante/nota
return avg($notas)
```
**Pregunta 5.** Devuelve los estudiantes de la carrera "Ingeniería".
```
for $estudiante in doc("estudiantes.xml")/estudiantes/estudiante
where $estudiante/@carrera = "Ingeniería"
return $estudiante
```
**Pregunta 6.** Ordena a los estudiantes por edad.
```
for $estudiante in doc("estudiantes.xml")/estudiantes/estudiante
order by $estudiante/edad 
return $estudiante
```
**Pregunta 7.** Devuelve el estudiante más joven.
```
for $estudiante in doc("estudiantes.xml")/estudiantes/estudiante
where $estudiante/edad = min(//edad)
return $estudiante
```
**Pregunta 8.** Devuelve los nombres y las notas incrementadas en 0.5.
```
for $estudiante in doc("estudiantes.xml")/estudiantes/estudiante
let $nota := $estudiante/nota + 0.5
return <estudiante>
    <nombre>{$estudiante/nombre}</nombre>
    <nota>{$nota}</nota>
</estudiante>
```
**Pregunta 9.** Devuelve los estudiantes cuya nota es mayor a 8 y pertenecen a Ingeniería.
```
for $estudiante in doc("estudiantes.xml")/estudiantes/estudiante
where $estudiante/@carrera = "Ingeniería" and $estudiante/nota > 8
return $estudiante
```
**Pregunta 10.** Cuenta cuántos estudiantes hay en total.
```
let $estudiantes := doc("estudiantes.xml")/estudiantes/estudiante
return count($estudiantes)
```
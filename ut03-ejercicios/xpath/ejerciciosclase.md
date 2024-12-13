# Ejercicio 1: Tienda de Libros

Copiar código
```
<bookstore>
  <book id="101">
    <title>Clean Code</title>
    <author>Robert C. Martin</author>
    <genre>Programming</genre>
    <price currency="USD">32.99</price>
    <stock>20</stock>
  </book>
  <book id="102">
    <title>The Pragmatic Programmer</title>
    <author>Andrew Hunt</author>
    <genre>Programming</genre>
    <price currency="USD">40.50</price>
    <stock>15</stock>
  </book>
  <book id="103">
    <title>1984</title>
    <author>George Orwell</author>
    <genre>Fiction</genre>
    <price currency="USD">12.99</price>
    <stock>50</stock>
  </book>
  <book id="104">
    <title>The Art of War</title>
    <author>Sun Tzu</author>
    <genre>Philosophy</genre>
    <price currency="USD">9.99</price>
    <stock>30</stock>
  </book>
  <book id="105">
    <title>Thinking, Fast and Slow</title>
    <author>Daniel Kahneman</author>
    <genre>Psychology</genre>
    <price currency="USD">20.00</price>
    <stock>10</stock>
  </book>
</bookstore>
```

Preguntas

1. Selecciona todos los títulos de los libros. `//title/text()`
2. Selecciona los autores de los libros en el género "Programming". `//book[genre="Programming"]/author/text()`
3. Selecciona el precio del libro "The Art of War". `//book[title="The Art of War"]/price/text()`
4. Cuenta cuántos libros tienen más de 20 en stock. `count(//book[stock > 20])`
5. Selecciona todos los géneros únicos disponibles en la tienda. `distinct-values(//genre/text())`
6. Selecciona el autor cuyo libro cuesta más. `//book[price=max(//price)]/author/text()`
7. Selecciona el título del libro más barato. `//book[price=min(//price)]/title/text()`
8. Selecciona todos los libros cuyo precio esté entre 10 y 30. `//book[price > 10 and price <30]` 
9. Selecciona todos los libros que tengan menos de 20 unidades en stock. `//book[stock<20]`
10. Selecciona el atributo id de todos los libros. `//@id`

# Ejercicio 2: Tienda de Electrónica

Copiar código:
```
<electronics>
  <item id="201">
    <name>Smartphone</name>
    <brand>BrandX</brand>
    <price currency="USD">699</price>
    <stock>50</stock>
  </item>
  <item id="202">
    <name>Laptop</name>
    <brand>BrandY</brand>
    <price currency="USD">999</price>
    <stock>10</stock>
  </item>
  <item id="203">
    <name>Tablet</name>
    <brand>BrandX</brand>
    <price currency="USD">399</price>
    <stock>25</stock>
  </item>
  <item id="204">
    <name>Headphones</name>
    <brand>BrandZ</brand>
    <price currency="USD">199</price>
    <stock>100</stock>
  </item>
</electronics>
```

Preguntas:

 1. Selecciona todos los nombres de productos. `//name/text()`
 2. Selecciona los productos de la marca "BrandX". `//item[brand="BrandX"]`
 3. Selecciona el producto más barato. `//item[price = min(//price)]`
 4. Selecciona el producto más caro. `//item[price = max(//price)]`
 5. Selecciona los nombres y precios de productos con más de 30 unidades en stock. `//item[stock>30]/(name/text() | price/text())`
 6. Selecciona el atributo currency de todos los precios. `//price/@currency`
 7. Cuenta cuántos productos hay en stock con menos de 20 unidades. `count(//item[stock<20])`
 8. Selecciona los nombres de todos los productos cuyo precio sea mayor a 500. `//item[price>500]/name/text()`
 9. Selecciona los nombres de productos con el atributo id mayor a 202. `//item[@id>202]/name/text()`
10. Selecciona todos los nodos completos de productos con "BrandZ". `//item[brand="BrandZ"]`

# Ejercicio 3: Biblioteca Digital

```
<library>
  <book id="301">
    <title>The Catcher in the Rye</title>
    <author>J.D. Salinger</author>
    <genre>Fiction</genre>
    <available>true</available>
  </book>
  <book id="302">
    <title>To Kill a Mockingbird</title>
    <author>Harper Lee</author>
    <genre>Fiction</genre>
    <available>false</available>
  </book>
  <book id="303">
    <title>The Great Gatsby</title>
    <author>F. Scott Fitzgerald</author>
    <genre>Fiction</genre>
    <available>true</available>
  </book>
  <book id="304">
    <title>1984</title>
    <author>George Orwell</author>
    <genre>Dystopian</genre>
    <available>true</available>
  </book>
  <book id="305">
    <title>Moby Dick</title>
    <author>Herman Melville</author>
    <genre>Adventure</genre>
    <available>false</available>
  </book>
</library>
```

Preguntas:

01. Selecciona todos los títulos de los libros. `//title`
02. Selecciona todos los libros disponibles (con available="true"). `//book[available="true"]/title`
03. Selecciona el autor del libro "1984". `//book[title="1984"]/author`
04. Selecciona todos los géneros de libros únicos. `distinct-values(//genre)`
05. Cuenta cuántos libros están disponibles. `count(//book[available="true"])`
06. Selecciona los títulos de los libros que no están disponibles. `//book[available="false"]/title`
07. Selecciona los autores cuyos libros están disponibles. `//book[available="true"]/author`
08. Selecciona el ID del libro "The Great Gatsby". `//book[title="The Great Gatsby"]/@id`
09. Selecciona todos los libros del género "Fiction". `//book[genre="Fiction"]`
10. Selecciona los títulos de los libros cuyo autor es "Herman Melville". `//book[author="Herman Melville"]/title`
# QuickCommerce

## Live Demo:
http://quick-commerce.com.es/

## Índice
- [1.1 Introducción](#introduccion) 															
- [1.2 Justificación del proyecto](#justificacion)  						       	   	  
- [1.3 Planificación](#planificacion)
- [1.4 Parte experimental](#parte_experimental) 
    - [1.4.1 Análisis](#analisis)
    - [1.4.2 Diseño](#diseño)
    - [1.4.3 Implementación y pruebas](#implementacion_pruebas)
    - [1.4.4 Implantación y documentación](#implantacion_documentacion)
    - [1.4.5 Resultados y discusión](#resultados_discusion)     
- [1.5 Conclusión](#conclusion) 
- [1.6 Bibliografía y referencias](#referencias) 


<a name="introduccion"></a>						     		
## 1.1 Introducción 

El tiempo que pasa un usuario en un portal de e-commerce normalmente es breve, por eso es muy importante facilitarle la información y la opción de compra lo máximo posible para convertir una visita breve en una venta. 

### Entorno Servidor

            • Python
            • Django
            • Servicios Rest
            
Esta aplicación realizada en Python, usando programación orientada a objetos. La base de datos está gestionada a través de django, y cuenta con las tablas user, cliente, producto, pedido,direccionpedido, productopedido.

### Entorno Cliente

            ▪ JavaScript

Se utilizará un motor de plantillas para implementar la interfaz visual. Por otro lado, se filtran el historial de coches reservados por un cliente a través de AJAX.

### Diseño de interfaces

            ▪ Bootstrap
            ▪ HTML5
            ▪ CSS
            ▪ JavaScript
            
### Despliegue de aplicaciones web

            ▪ Heroku

            ▪ Apache

<a name="justificacion"></a>
## 1.2 Justificación del proyecto y objetivos

 sin necesidad de registrarse en la plataforma. Contará con un carrito que añade y elimina productos del mismo, y además se integrará una pasarela de pago a través de paypal para replicar lo que sería un negocio en internet. Contará con 5 vistas: Catálogo de productos, carrito ,pasarela de pago,login y pagina de registro. 
 Respecto al modelo de base de datos, el portal contará con 6 tablas: usuario, cliente, pedido, producto_pedido, producto, dirección_pedido. 

<a name="planificacion"></a>
## 1.3 Planificación

              • Como usuario se requiere poder comprar articulos sin necesidad de loguear en la plataforma.
              • Como usuario, se requiere poder guardar el carrito con los productos que se añadieron mediante cookies.
              • Como administrador se requiere poder hacer CRUD de todos los productos, además de manejo general de la base de datos.
              • Como usuario, se requiere poder loguear en la plataforma y utilizar el carrito de forma dinámica, es decir añadir o quitar artículos del mismo según convenga.
              • Como usuario, se requiere poder pagar con tarjeta de crédito a través de paypal.
              • Como usuario se requiere poder consultar la cantidad de productos que se encuentran en el carrito desde el icono de carrito en la esquina superior derecha de la interfaz.
              • Como usuario se requiere poder modificar la cantidad de un mismo producto desde la vista “cart” de manera sencilla y dinámica.
              • Si un carrito contiene solo productos digitales que no precisan de envío, el formulario de dirección le será ocultado al usuario.
              • Por otro lado, si el usuario añade productos físicos al carrito, el formulario de envío será mostrado.

<a name="parte_experimental"></a>
## 1.4 Parte experimental           
  <a name="analisis"></a>
  ### 1.4.1 Análisis
  
  ### Casos de uso
  
  ![Imagen](https://user-images.githubusercontent.com/117280411/208066707-b22098c9-4371-445d-80af-8f10d4139da2.png)

  
  Imagen 1. Resumen de los casos de uso de la plataforma con dos tipos de usuarios: Cliente y administrador.
  
  ![Imagen](https://user-images.githubusercontent.com/117280411/208067039-a0584dfd-0780-4f15-ad92-aa4e3311bc86.png)
  
  Imagen 2. Detalles de casos de uso de cada tipo de usuario.
  
  ### Diagrama E/R
  
  ![Imagen](https://user-images.githubusercontent.com/117280411/208067254-a86031d7-e587-4a32-9ab2-a429569ae6b5.png)
 
 Imagen 3. Detalles de las tablas principales usadas en la plataforma junto con sus relaciones.
  
     • La tabla User es parte del modelo de Django.
    • Por otro lado, un User puede convertirse en cliente una vez que realiza una compra y está registrado en la plataforma. Cliente y User mantienen una relación OneToOne.
    • La tabla Producto representa los productos actuales que se encuentran en stock.
    • La tabla Pedido representa una transacción que se ha llevado a cabo o se va a llevar a cabo. Contiene un codigo de transacción, y mantiene una relación con cliente de ManyToOne.
    • La tabla ProductoPedido contiene productos que un cliente ha ido pidiendo y añadiendo al carrito. Por tanto, estos productos pedidos se añaden a la tabla pedido una vez que el usuario desea finalizar la compra. Mantiene una relacion ManyToOne con la tabla Pedido.
    • Por otro lado, la tabla Producto contiene información sobre los productos disponibles. Tiene una relación ManyToOne con ProductoPedido.
    • Finalmente, la tabla DireccionPedido se encarga de almacenar la información sobre la direccion de reparto de un pedido. No todos los pedidos requieren de reparto, ya que algunos productos tienen formato digital. Mantiene una relación ManyToOne con Pedido. 

### Prototipado

### Home

  ![Imagen](https://user-images.githubusercontent.com/117280411/208067573-6236b711-7d61-4227-9787-5c0b868ca346.png)
  
  Imagen 4. Representación de pantalla principal de la plataforma con varios enlaces y botones que redirigen a otras secciones.

        • Un usuario puede añadir productos al carrito mediante el botón “add to cart”, además de ver detalles de los productos mediante el botón “view”.
        • Un usuario tiene la opción de loguearse en la plataforma, y comprar productos. Sin embargo, no es necesario estar logueado en la plataforma para comprar productos.
        • En la parte superior derecha, el usuario puede consultar el numero de productos totales que tiene en su carrito, además de dirigirse al mismo al realizar un click sobre este.

### Carrito

  ![Imagen](https://user-images.githubusercontent.com/117280411/208067788-e7d55e4a-9cea-4b56-b1ee-7dbc05ee8245.png)
  
  Imagen 5. Representación de vista de carrito en la cual se muestra un resumen de los productos a añadir al pedido
  
        • Un usuario puede modificar la cantidad de productos que quiere agregar al pedido mediante las correspondientes flechas.
        • El usuario puede volver a la pantalla de inicio, o dirigirse a la pantalla de checkout.
    
 ### Checkout

  ![Imagen](https://user-images.githubusercontent.com/117280411/208068072-bf416a15-eb4a-45b7-b373-222d8e59cd72.png)

 Imagen 6. Representación de vista de checkout en la que el cliente puede consultar su pedido final antes de confirmar el mismo.
 
      • Un usuario puede confirmar un pedido, además de agregar una dirección de envío a la que le pueden llegar los productos.
      • Por otro lado, el usuario puede elegir un método de pago para realizar la compra.
    
 ### Paypal Payment Integration

  ![Imagen](https://user-images.githubusercontent.com/117280411/208068370-5f4c12b3-6480-42c6-8aef-f9cd849dfa99.png)
  
  Imagen 7.1. Representación de vista de checkout en la que el cliente puede consultar su pedido final antes de confirmar el mismo.
     
       • Un usuario puede elegir su forma de pago a través de PayPal, tarjeta de crédito, o una combinación de ambas y dividir el importe total.
       
    ![Imagen](https://user-images.githubusercontent.com/117280411/208068892-bd909bf6-08b3-4fac-aa93-1d3531b0ddf9.png)
  
  Imagen 7.2. Imagen que muestra el pago de los artículos por parte de un usuario en la plataforma.
  
      • PayPal permite dividir los pagos entre una cuenta y una tarjeta de crédito/débito.
      • También incluye la opción de cambiar la dirección de envío.
      
      ![Imagen](https://user-images.githubusercontent.com/117280411/208069198-55aa2c1c-c4d2-43dc-9a9b-2fc37448a764.png)
  
  Imagen 7.3. Representación de pago alternativo por medio de tarjeta en un pedido
  
      • El usuario puede optar por pago a través de tarjeta mediante este formulario desplegable.
      • De esta forma, se le permite al usuario disponer de varias opciones a la hora de comprar, lo que resulta en una mayor conversión de venta.
 

   <a name="diseño"></a>
   ### 1.4.2 Diseño
   
   ![Imagen](https://user-images.githubusercontent.com/117280411/208069468-088d5f56-b9ea-44c3-b6bd-e918569a731b.png)
   
   Imagen 8.1. Detalles de las tablas utilizadas. Imagen obtenida de DBeaver.direccion_pedido, pedido, user y cliente.
   
   ![Imagen](https://user-images.githubusercontent.com/117280411/208069638-0b0c7320-fda1-4746-b6fa-7f0e1104a964.png)
   
   Imagen 8.2. Detalles de las tablas utilizadas. Imagen obtenida de DBeaver.direccion_pedido,producto_pedido, pedido y cliente.
   
   ![Imagen](https://user-images.githubusercontent.com/117280411/208069772-49a83b13-591a-48ff-97b6-6fe507ba3a4c.png)
   
   Imagen 8.3. Detalles de las tablas utilizadas. Imagen obtenida de DBeaver.producto_pedido, producto y pedido.
   
     • La plataforma contiene 6 tablas las cuales contiene la información necesaria para el correcto funcionamiento de la mismo.
     • Con referencia a la imagen 7.1, se puede distinguir la relación entre user y cliente, ya que una vez que un pedido ha sido confirmado, un user pasa a ser un cliente de la plataforma. Al mismo tiempo, se le asignará una dirección de pedido dependiendo del campo “digital” en la tabla producto.
     • Por otro lado, en las imágenes 7.2 y 7.3, se muestra la relación entre los productos que se añaden a un carrito mediante la tabla producto_pedido, y estos mismos que se añaden a un pedido una vez confirmado el mismo, creándose así un registro de cliente y de dirección de pedido si se cumplen los requisitos.

 ### Tecnologías utilizadas
 
 La aplicación se desarrolla en su mayor parte en lenguaje Python, aunque contiene ciertas partes realizadas en JavaScript.
Python es probablemente el lenguaje de programación más usado en la actualidad, además de estar presente en los Sistemas Operativos de Mac y Ubuntu que son los elegidos para el desarrollo de esta plataforma. Además, python es conocido por su migración sin problemas a versiones más nuevas y su sintaxis simple y fácil de aprender, que mejora la legibilidad y también reduce los costes de mantenimiento del software. Finalmente, el hecho de poder utilizar virtualenvs para el desarrollo de la plataforma, ha supuesto una gran ventaja, ya que ha permitido aislar el proyecto de los paquetes y las versiones de python existentes en los sistemas operativos utilizados, y así poder trabajar en el mismo proyecto desde dos equipos diferentes. 

Para el desarrollo de este proyecto, se ha utilizado el framework Django ya que es utilizado junto a python para el desarrollo de aplicaciones bajo el modelo vista controlador. Se barajó la posibilidad de utilizar otro framework de python como es Flask junto con su motor de plantillas Jinja2, pero este fue descartado ya que no admite páginas HTML dinámicas. La organización del proyecto con Django es la siguiente:
      
    • Models.py => Contiene las clases las cuales son mapeadas en forma de tablas por el ORM de Django hacia la base de datos.
    • Views.py => Permite obtener una web request y devolver una web response que en este caso son los elementos HTML de los templates. 
    
    Además, en este proyecto se utilizarán funciones en views que devuelven una JsonResponse.
    
    • Urls.py => Contiene código python que permite el mapeo entre URL path expressions a las funciones situadas en views.py
    • Templates => Este fichero aloja los archivos HTML que sirven como interfaz de usuario.
    • Migrations => Contiene archivos.py con creacion de tablas, cambios en tablas, etc.  
    
Por otro lado, la introducción de JavaScript se encarga del manejo de datos de manera dinámica en la interfaz a través de funciones propias de este lenguaje como por ejemplo la recogida de datos de los formularios en html (shippingInfo.direccion = form.direccion.value). Esta información se almacena en variables para después ser enviada a views.py a través de JSONs, y ser procesadas en este archivo para finalmente ser alojada en BBDD.

Finalmente, cabe destacar la introducción de Paypal como método de pago a la hora de realizar pedidos, ya sea a través de usuarios registrados, o a través de usuarios no registrados mediante cookies. Esta API nos permite simular lo que sería una transacción entre un cliente y una web, gracias a la previa introduccion de fecth API de JavaScript. El usuario puede elegir cómodamente sus métodos de pago, pudiendo incluso dividir el importe total del pedido entre su cuenta de Paypal, y su tarjeta de crédito. Esta implementación, le permite a Quickcommerce convertirse en una aplicación muy cómoda y fiable para el usuario en la que puede comprar tantas veces como desee. 

El motor de base de datos escogido es SQLite, dado que presenta grandes ventajas frente a otros motores disponibles actualmente. Adicionalmente, se usa el ORM de Django como se ha comentado anteriormente que facilita el mapeo de atributos en una base de datos relacional, de modo que agiliza la relación entre una aplicación y una base de datos, optimizando el flujo de trabajo.
      
      ◦ Su adquisición es gratuita, lo que permite reducción de costes para el cliente.
      ◦ Es multiplataforma para Windows, Linux y Mac, con lo cual se podrá usar en cualquiera de estos sistemas operativos.
      ◦ Al ser un motor muy extendido entre la comunidad de desarrolladores, es sencillo encontrar ayuda.
      ◦ La labor de mantenimiento de una base de datos SQLite es relativamente sencilla frente a sus competidores, ya que presenta menos funciones. Lejos         de ser una desventaja, esto se presenta como un punto a favor, ya que supone que el mantenimiento de la aplicación lo puede llevar el propio             desarrollador, sin tener que recurrir a un administrador de bases de datos.
      
      ◦ Finalmente, es escalable, lo cual lo convierte en una gran ventaja si se quiere ampliar la extensión del proyecto.
        
 <a name="implementacion_pruebas"></a>
   ### 1.4.3 Implementación y pruebas 
   
La plataforma cuenta con varios métodos definidos en el archivo views.py que permiten renderizar las principales vistas de la interfaz de usuario. El siguiente método permite al usuario visualizar los principales productos a la venta:
   
    
   ![Imagen](https://user-images.githubusercontent.com/117280411/208071061-3acc257b-3da9-4a5f-ac21-651b0e6e6274.png)
   
   Imagen 9.1. Representación de la interfaz principal “store” que permite visualizar los productos al posible comprador.

Por un lado, se comienza a gestionar la inserción de registros en sus correspondientes tablas: cliente, producto_pedido y pedido. Por otro lado, si el usuario no está idenficado, se comienza la gestión del pedido mediante cookies. 

En este código de html, se crear un loop en los productos disponibles, en los cuales se añade funcionalidad al boton “Add to cart” mediante clases y JavaScript.

 ![Imagen](https://user-images.githubusercontent.com/117280411/208071484-b43ac7ea-e729-429f-81d1-9aea0a0aef3e.png)
   
   Imagen 9.2. Representación de la interfaz principal “store” que permite visualizar los productos al posible comprador.
   
   ![Imagen](https://user-images.githubusercontent.com/117280411/208071691-55b16bf8-b992-471c-b742-79e3aca09707.png)
   
   Imagen 9.3. For loop que recoge los principales atributos de la clase producto.Este bucle recorre los botones previamente mencionados en la anterior      captura y los guarda en variable
   
     ![Imagen](https://user-images.githubusercontent.com/117280411/208071940-72562b3c-9d38-4c01-9cab-3e549fa74e19.png)
   
   Imagen 9.4. Esta imagen representa  la función que añade productos al carrito según el tipo de usuario(addCookieItem para usuarios no logueados y updateUserOrder  para usuarios logueados).
   
   Finalmente, mediante Fetch API de JavaScript, se envía la información recogida en la vista mediante un metodo post, a una vista intermedia: “update_item”.
   
  ![Imagen](https://user-images.githubusercontent.com/117280411/208072208-e04728a2-0777-445a-b406-a460e5a2ed1c.png)
   
   Imagen 9.5. Esta imagen representa la creación de una cookie que se encargará de gestionar la información de  un usuario no logueado. 

Por otro lado, se requiere de la creación de una cookie para los usuarios que no desean registrarse en la plataforma para poder comprar.

    ![Imagen](https://user-images.githubusercontent.com/117280411/208072494-046c820c-7785-4cd5-b914-90c32c3b0791.png)
   
   Imagen 9.6. Función que añade productos al carrito a través de la cookie. 
   
 Con esta función podemos añadir un producto al carrito a través de la cookie creada previamente. De la misma manera, se puede eliminar productos del   carrito, hasta el punto de eliminarlos por completo del mismo
 
 ![Imagen](https://user-images.githubusercontent.com/117280411/208072692-5285ddc2-cf9c-4571-8312-4e4cac7dcbf3.png)
   
   Imagen 9.7. Representación de la clase pedido junto con sus metodos. 
   
   En la clase Pedido se añaden dos métodos los cuales permiten calcular el numero total de productos pedidos que contiene un pedido, además de la cantidad total del mismo. El decorador @property, actua como un atributo mas del objeto “pedido”.
   
   ![Imagen](https://user-images.githubusercontent.com/117280411/208073095-b6cc58fa-30be-4a6e-b1b3-f5ea9e914677.png)
   
   Imagen 9.8. Función que añade productos a la cesta de un usuario logueado. 
   
   En este método, se recoge la información que se guarda en archivo .json a través de Fetch API, lo cual permite modificar de manera dinámica la cantidad de productos que se encuentran en el carrito, a la vez que se guarda la información en la base de datos.
   
    ![Imagen](https://user-images.githubusercontent.com/117280411/208073261-b085fb00-3d16-4533-a55e-7d1b7a6e5871.png)
   
   Imagen 9.9. Función del archivo cart.js que permite  ejecuta la funcion submitFormData. 
   
   En estas lineas de JavaScript, se encuentra el codigo necesario para esconder el formulario de envío requerido si el carrito solo contiene productos digitales, además de mostrar el boton de pago si el cliente está decidido a comprar.

   

    ![Imagen](https://user-images.githubusercontent.com/117280411/208073583-45702ae9-a890-43d5-b741-a63a0271609b.png)
   
   Imagen 9.10. Representación de la  funcion submitFormData. 

Al igual que se hizo con los productos que se añadían al carrito, en esta función de JavaScript, se procesa un pedido realizado por un cliente, además de una dirección de envío si procede a través de fetch API. El resultado es la creación de un pedido asignado a una dirección de pedido que ha introducido el cliente para ser recibido.

 ![Imagen](https://user-images.githubusercontent.com/117280411/208073805-e056112c-cc48-495f-a9f6-dd18a6191c2a.png)
   
   Imagen 9.11. Representación de la  funcion  python processOrder. 
   
   La implementación de funciones relacionadas con los pedidos tramitados mediante la cookie previamente creada, nos permite aislar estos métodos para después ser importados desde views. En este caso, cookieCart muestra los productos que el usuario ha ido añadiendo al carrito.
   
    ![Imagen](https://user-images.githubusercontent.com/117280411/208073998-334a9df1-82a8-4057-9c36-d68eed6ac697.png)
   
   Imagen 9.12. Representación de la  funcion cookieCart. 
   
   Por otro lado, la funcion cartData permite acceder a toda la información recopilada en el metodo anterior, para después ser procesada en una última funcion que confirma el pedido realizado por un usuario sin ser logueado. 
   
   
   ![Imagen](https://user-images.githubusercontent.com/117280411/208074212-55bdab68-746d-4e4b-b0b3-ebafbc5a109b.png)
    
   Imagen 9.13. Imagen que representa la función cartData 
   
   Finalmente, la función guestOrder nos permite confirmar el pedido de un usuario no logueado mediante el acceso a la información guardada en la variable “cookieData”. En esta función se guarda en base de datos a un cliente junto con su nombre e email, para poder obtener información sobre los pedidos que ha realizado en la plataforma anteriormente. Por otro lado, se asocia a este mismo cliente a un pedido, junto con los productos pertenecientes al mismo.
   
 ![Imagen](https://user-images.githubusercontent.com/117280411/208074379-c12eddcc-9c56-4848-9b2d-af5f45253ad7.png)
    
   Imagen 9.14. Imagen que representa la función cartData 
   
### Pruebas
   
Durante el desarrollo del proyecto se han llevado a cabo pruebas manuales, a medida que el proyecto precisaba de cambios o nuevas funcionalidades.

![Imagen](https://user-images.githubusercontent.com/117280411/208074952-f697ccd5-e5e5-4b89-84c4-e0eafbf3fe8f.png)
    
   Imagen 10. Representación de la  updateUserOrder
   
   Mediante el uso de FetchAPI se consiguó que el usuario pudiera añadir a su carrito, productos de manera dinámica. Durante la implementación de esta función, se presentaron ciertas complicaciones como por ejemplo el apartado headers el cual requería la línea “'Content-Type':'application/json'” para envíar el id de un producto a la siguiente vista. Por otro lado, para recargar la página y añadir los productos de manera dinámica, se decidió usar la función “location.reload”. Esta función ofrece la recarga de la página cada vez que se añade un producto al carrito por parte de un usuario. En definitiva, se ha elegido esta opción sobre otras posibles opciones como por ejemplo jQuery.ajax() o el propio Django, ya que ofrece la posibilidad de enviar JSON data, lo cual se presentaba más conveniente junto con la manera de tramitar pedidos con cookies.
   
Por otro lado, como se ha comentado antes, la posibilidad de un usuario de comprar productos en la plataforma sin necesidad de registrarse se ha llevado a cabo mediante cookies. De la misma manera que se utiliza formato JSON para navegar por las diferentes vistas con los productos deseados, y finalmente confirmar el pedido como lo haría un usuario registrado,  se han utilizado varios métodos en el archivo views.py, así como métodos nativos de JS, que nos permiten tramitar pedidos de una forma similar a la que se haría con un usuario registrado en la plataforma. 
   
   
![Imagen](https://user-images.githubusercontent.com/117280411/208075135-3a640f55-f6dc-4b47-9e05-9aeb4716400f.png)

   Imagen 10.1 Representación de la  funcion getCookie. 
   
   Esta función crea una cookie llamada “cart”, y la convierte a JSON string para ser enviado a través de las diferentes vistas.
   
   ![Imagen](https://user-images.githubusercontent.com/117280411/208075438-3f3997cf-9abd-4552-9f37-598a97222e49.png)

   Imagen 10.2 Representación de la  funcion addCookieItem. 
   
   Con esta función podemos añadir productos a “cart” para luego ser renderizados en la vista de manera que un cliente guest puede saber lo que lleva en    su cesta temporal. De nuevo, el método JS “stringify” convierte un objeto JS en un JSON string.
   ```
    Test:

    Make order with guest user
    Result => Cookie reloads coming back empty string and order is being placed in database
    Make order with registered user
    Result => Data registered in database
    Make order with same id
    Result => field complete not ticked as true, OrderItems contain transaction id, orders are saved with transaction id
    Assign orders to id instead of transaction id def __str__(self): return str(self.id)
    Result => Orders are assigned to ids and orderItems are assigned to certain order ids
    Make order being a registered user
    Result => Order is created with an id and products are assigned to it. Complete checkbox is checked
```
Sin embargo, una de las partes más interesantes de este proyecto es la idea de establecer una jerarquía de usuarios, que está proporcionada por la parte admin propia de Django. La ventaja de esto, es que una vez la plataforma creciese, se podrían crear grupos que tuvieran diferentes permisos, según el grupo al que perteneciesen. En este caso, se han establecido dos grupos: admin y customer, con la intención de que el grupo admin tenga acceso a secciones privilegiadas de la plataforma, como un historial de pedidos de la plataforma, así como información de clientes, para poder establecer una estrategia de marketing digital.

 ![Imagen](https://user-images.githubusercontent.com/117280411/208075709-59dfa0f9-b34d-4b6e-80fa-cc268ca97693.png)

   Imagen 10.3.Representación de la  las funciones que organizan a usuarios en grupos 
    Con estas tres funciones podemos manejar el flujo de acceso de un usuario a la plataforma dependiendo de a qué grupos pertenezca.
    
    ```
        Test:
        Create a user through register.html
        Result => User created successfully
        Create a user with email
        Result => User created successfully and email saved
        Type a user that is not registered
        Result => Error message in interface
        Log in with user registered
        Result => Name of user shows up in navbar
```
Process order with logged in user 
Cookie not required for logged in user so conditional added just before cookie is created 

![Imagen](https://user-images.githubusercontent.com/117280411/208076030-863f38df-9e13-47a6-8251-9b4cfdd9dcb1.png)

![Imagen](https://user-images.githubusercontent.com/117280411/208076095-831f18c4-f652-42b5-a591-dd0d30880327.png)

Result => Order was not being processed as part of a query error 
Process order with non logged-in user
Result => Success
Conclusion: Orders were not being processed correctly with logged-in users 

![Imagen](https://user-images.githubusercontent.com/117280411/208076248-9e55b192-cff2-4013-90db-7510f2c1c9a6.png)

In order to know whether user orders were being completed, a few prints were added so that we could see if pedido.get_cart_total that comes from python Pedido matches that of the total that comes from JS. Only then, the order is processed properly. 


<a name="implantacion_documentacion"></a>	
### 1.4.4 Implantación y documentación

Para windows se descargará un ejecutable con la version 3.10.6 de python que permite poder utilizar este lenguaje de progamación. En el caso de Ubuntu 22.04.1 LTS, python forma parte del sistema operativo, y no hay necesidad de instalarlo. 

El siguiente paso sería crear el directorio del proyecto

mkdir quick_commerce

Después creariamos un virtualenv que nos permite aislar nuestro proyecto de la version de python y los paquetes de python que tenemos

python3.7 -m venv ~/venv-ecommerce

Se activa el virtualenv

source ~/venv-ecommerce/bin/activate

instalamos django

pip install django

creamos un archivo con los paquetes de python que 

touch requirements.txt

Django==3.2.12
django-filter==22.1
docker==6.0.0
docker-compose==1.29.2
dockerpty==0.4.1
gunicorn==20.1.0
httplib2==0.20.2
jsonschema==3.2.0
oauthlib==3.2.0
olefile==0.46
Pillow==9.0.1
python-dateutil==2.8.1
six==1.16.0
sqlparse==0.4.2
toml==0.10.2
urllib3==1.26.5
virtualenv==20.16.6
whitenoise==6.2.0
django-storages==1.13.1
boto3==1.26.27

finalmente creamos el proyecto 

python3 manage.py startapp store

para crear la base de datos en sqlite basta con ejecutar los siguientes comandos:

python3 manage.py migrate

python3 manage.py makemigrations

create superuser by python manage.py createsuperuser

Para arrancar el servidor de django

python3 manage.py runserver

### Entorno en produccion
Primero empezaremos con la contratación de un servidor y un dominio. En este caso, el servidor será clouding.io el cual nos servirá la web en producción. El dominio contratado será http://quick-commerce.com.es/
Se obtiene la IP del servidor y se accede mediante ssh root@161.22.41.179
Una vez dentro, empezaremos a configurar apache para el proyecto django

For apache, just do this: sudo apt-get install apache2, you can also add this
sudo apt-get apache2.2-common apache2-mpm-prefork apache2-utils libexpat1
For mod_wsgi, if you are using python 3, you should install mod_wsgi using
sudo apt-get install libapache2-mod-wsgi-py3
Una vez instalados todos estos paquetes, se configura el virtualhost para el proyecto
sudo nano django.conf
```
    <VirtualHost *:80>
        ServerName quick-commerce.com.es
        ServerAlias www.quick-commerce.com.es

        Alias /static /var/www/QuickCommerce-rama_prueba/static/
        Alias /images /var/www/QuickCommerce-rama_prueba/static/images
        Alias /static/admin/css /usr/local/lib/python3.8/dist-packages/django/c>
        Alias /static/admin/js /usr/local/lib/python3.8/dist-packages/django/co>

        WSGIScriptAlias / /var/www/QuickCommerce-rama_prueba/quick_commerce/wsg>

        <Directory /var/www/QuickCommerce-rama_prueba/>
                Order deny,allow
                Allow from all
        </Directory>

        DocumentRoot /var/www/QuickCommerce-rama_prueba
     <VirtualHost>
 ```

Having understood, the code, you must disable the default virtual host config file i.e 000.default.conf, and enable the newly created virtual host config file and restart as shown below.
A2dissite 000.default.conf
sudo a2ensite django.conf
service apache2 restart

Once you get the “OK” message, you have more one thing to do, and that is telling apache to import your python project. The WSGIPythonPath line ensures that your project package is available for import on the Python path; in other words, that import my_project works.
sudo nano /etc/apache2/apache2.conf
WSGIPythonPath /var/www/QuickCommerce-rama_prueba
sudo nano /etc/hosts que apunte desde la ip de servidor a la web 

<a name="resultados_discusion"></a>	
### 1.4.5 Resultados y discusión

El desarrollo de la aplicación comenzó con el desarrollo de varias interfaces con el fin de mostrar una serie de productos disponibles para compra. Después, se implementó la lógica de negocio que permitía la creación del carrito y el checkout. Seguidamente, se pasó al lado del diseño para ajustar márgenes y estilos, de manera que se consiguiera una interfaz llamativa e intuitiva para el usuario. A continuación, se pasó a la parte de la lógica de nuevo, para añadirle varias funcionalidades como es el sistema login que funciona con decoradores, el cual nos permite acceder a ciertas partes de la plataforma solo si tenemos las credenciales necesarias, de lo contrario, solo podemos ver ciertas secciones de usuario. Además de esto, en la barra de navegación encontramos un buscador el cual se ayuda de consultas para mostrar los productos digitales o fisicos. Seguido de estos desarrollos, se implementó la opción de que usuarios no registrados pudiesen comprar productos en la plataforma sin necesidad de loguearse. Esta última funcionalidad se llevó a cabo a través de cookies. Finalmente, se incluye una implementación de pago a través de paypal, la cual da mucha comodidad a los clientes a la hora de comprar productos. Con lo que respecta a los tiempos de finalización, se han cumplido los plazos estimados para la realización del proyecto, sin contar con las mejoras posteriores previas a la planificación del proyecto. La parte que más ha demorado la finalización del proyecto, involucraba  la distincion de los pedidos realizados por usuarios logueado o no logueados.  El problema venía en que para el cliente logueado, no se podía procesar un pedido de manera completa.  Esto se solventó sustituyendo una query de python por otra:  Pedido.objects.filter(cliente=cliente, completo=False).first(). Por otro lado, el despliegue de la aplicación en un entorno de desarrollo ha resultado ser un gran reto, habiendo probrado con 3 maneras distintas: heroku, pythonanywhere y apache. En la primera, los archivos estáticos no se servían correctamente, y se intentaron servir con s3 buckets de AWS sin éxito. Finalmente se consiguió el despliegue de las 3 maneras, pero se optó por apache, ya que no presentaba errores en los archivos estáticos en ningún momento, mientras que en los otros dos método si presentaba estos fallos da manera seguida.

De cara al futuro se pretenden añadir mejoras en la aplicación, como la inserción de un filtro de precios que se realice mediante jquery y ajax, para mejorar la experiencia de usuario. También se pretende introducir un sistema de pago real a través de paypal. Por otro lado, se contempla incluir un dashboard para administradores del sitio web el cual permite consultar el listado de pedidos realizados de manera sencilla. Finalmente, el cliente también contaría con su propio dashboard para consultar el historial de pedidos realizados. 

<a name="conclusion"></a>
## 1.5 Conclusiones

El lenguaje de programación Python junto con el framework Django, representan dos de las tecnologías más usadas a la hora de realizar desarrollo web. Esto junto con el motor de base de datos escogido y el lenguaje de marcas HTML junto con hojas de estilos CSS y herramientas de despliegue en remoto, hacen de esta aplicación, un proyecto completo a la hora de obtener unas bases sólidas en programación. Durante el primer año realizado de este curso, se utilizaron las tecnologías previamente mencionadas, con la excepción de Python y Django. Durante la realización de este proyecto de manera autodidacta, y desviandose de tecnologías previamente utilizadas durante el curso, se ha pretendido innovar respecto a proyectos ya evaluados y gracias a esta apuesta por tecnologías alternativas se han podido integrar todos los conocimientos previos en un proyecto de funcionalidad que se asemeja a plataformas actuales encontradas en la red. Esto quiere decir que se han obtenido conocimientos y habilidades enfocadas a un usuario, tanto en el apartado de funcionalidad para facilitar el uso de la plataforma, junto con el lado de diseño para así conseguir una buena experiencia de usuario. Asimismo, la realización del proyecto por etapas o “sprints” gracias al uso de la herramienta Taiga, ha supuesto un aprendizaje adicional respecto al lado de administración y organización, ya que actualmente la realización de proyectos basado en la metodología Scrum está muy presente en los equipos de desarrollo.




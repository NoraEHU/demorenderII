(más abajo en castellano)
# IoT sistema baten demoa Render.com zerbitzuarekin (adibide arina)

Demo honen bidez IoT sistemaren funtzionamendua modu sinple batean ikusiko dugu: datu simulatuak jasotzen dira, datu-base batean gordetzen dira eta webgune batean bistaratzen dira. Horri esker, IoT kate osoa —datuen jasoketa, prozesamendua eta bistaratzea— praktikan nola gauzatu daitekeen ulertuko dugu.

Helburua lortzeko, Flask erabiliko dugu API bat sortzeko. API horren bidez, sentsore edo bezeroek datuak bidali ahal izango dituzte, eta Flask-ek datu horiek SQLite datu-base batean gordeko ditu. SQLite fitxategi bakarreko datu-base sinple baina eraginkorra da gure kasuan.

Gainera, API honek dashboard sinple bat eskaintzen du web orri baten bidez, sentsoreen datuak taula batean erakutsiz.

Azkenik, Render.com zerbitzuari esker, Github-en dagoen kodea martxan jarrikoda eta API zerbitzua erabilgarri bihurtu.

Egileak: Aitzol Ezeiza, Nora Barroso

# Demo de un sistema IoT con el servicio Render.com (ejemplo sencillo)

Con esta demo veremos de forma sencilla cómo funciona un sistema IoT: se recogen datos simulados, se almacenan en una base de datos y se muestran en una página web. Gracias a ello, podremos entender cómo se puede llevar a la práctica toda la cadena IoT —captura de datos, procesamiento y visualización—.

Para lograrlo, utilizaremos Flask para crear una API. A través de esta API, los sensores o clientes podrán enviar datos, y Flask los guardará en una base de datos SQLite. En nuestro caso, SQLite es un sistema de base de datos muy simple pero eficaz, basado en un único archivo.

Además, esta API ofrece un dashboard sencillo accesible desde una página web, donde se muestran los datos de los sensores en una tabla.

Por último, gracias al servicio Render.com, el código alojado

Aitoría: Aitzol Ezeiza, Nora Barroso

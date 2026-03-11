# Urban Routes - Pruebas Automatizadas

## Descripción del Proyecto

Este proyecto contiene pruebas automatizadas para verificar el proceso completo de solicitar un taxi en la aplicación Urban Routes.

Las pruebas simulan el comportamiento de un usuario dentro de la aplicación y validan que cada paso funcione correctamente.

El flujo probado incluye:
- Configuración de la ruta
- Selección de la tarifa Comfort
- Agregar número de teléfono
- Agregar tarjeta de crédito
- Enviar mensaje al conductor
- Solicitar extras
- Pedir un taxi

El proyecto está organizado utilizando el patrón **Page Object Model (POM)**.

---

## Tecnologías Utilizadas

- Python 3
- Selenium WebDriver
- PyTest
- ChromeDriver

---

## Estructura del Proyecto

Clases principales utilizadas:

**main_page.py**  
Contiene los métodos para interactuar con la página principal de Urban Routes.

**helpers.py**  
Contiene funciones auxiliares utilizadas en las pruebas.

**test_urban_routes.py**  
Contiene las pruebas automatizadas del flujo de solicitud de taxi.

---

## Cambio de URL (Servidor Temporal)

Durante las pruebas se utiliza un servidor temporal proporcionado por TripleTen.  
La URL puede cambiar dependiendo de la sesión de pruebas, por lo que es necesario actualizarla antes de ejecutar las pruebas.

---

## Cómo ejecutar las pruebas

### 1. Instalar dependencias

```
pip install selenium
pip install pytest
```

### 2. Ejecutar las pruebas

Desde la terminal ejecutar:

```
pytest
```
# Proyecto de Automatización de Pruebas para Urban Grocers

Este proyecto consiste en automatizar las pruebas para la funcionalidad de creación de kits de productos en la aplicación Urban Grocers. El objetivo principal es convertir una lista de comprobación manual en pruebas automatizadas utilizando Python y pytest.
___
## Sobre el proyecto

El proyecto automatiza las pruebas del campo `name` en la solicitud de creación de kits de productos, verificando:

- Validación de longitud de caracteres (1-511 caracteres permitidos)
- Manejo de caracteres especiales, espacios y números
- Comportamiento con parámetros faltantes o tipos incorrectos
- Códigos de respuesta HTTP correctos (201 para casos exitosos, 400 para errores)

## Componentes principales:

- Pruebas automatizadas que cubren casos positivos y negativos
- Integración con API de Urban Grocers para crear usuarios y kits
- Gestión de autenticación con tokens
- Estructura de proyecto organizada con archivos separados para configuración, datos y pruebas

## Fuente de documentación utilizada:
* _**apiDoc**_ - Documentación de la API de Urban Grocers disponible en: https://cnt-c6329488-07f3-4c44-8bbf-aa83a479fa49.containerhub.tripleten-services.com/docs/

    La documentación específica utilizada se encuentra en la sección "Main.Kits" > "Crear un kit."

## Tecnologías utilizadas:

- _**Python**_  como lenguaje de programación
- _**pytest**_ como framework de testing
- _**requests**_ para realizar llamadas HTTP a la API
- _**Git/GitHub**_ para control de versiones


- Necesitas tener instalados los paquetes pytest y request para ejecutar las pruebas.
- Ejecuta todas las pruebas con el comando pytest.

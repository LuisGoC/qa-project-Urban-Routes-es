# 🚕 Urban Routes - Automatización de Pruebas E2E

## 📋 Descripción del proyecto

Este proyecto contiene un conjunto de **pruebas automatizadas de extremo a extremo (E2E)** para la aplicación **Urban Routes**, desarrolladas con el objetivo de validar el flujo completo de solicitud de un servicio de transporte desde la perspectiva del usuario final.

Las pruebas automatizadas cubren los siguientes escenarios:

* 📍 Configuración de direcciones de origen y destino.
* 🚖 Selección de la tarifa **Comfort**.
* 📱 Ingreso y verificación del número de teléfono.
* 💳 Registro y selección de una tarjeta de crédito.
* 💬 Escritura de un mensaje para el conductor.
* 🧸 Solicitud de artículos adicionales:

  * Manta y pañuelos.
  * Dos helados.
* 🔎 Verificación del modal de búsqueda de taxi.

---

## 🛠️ Tecnologías utilizadas

| Tecnología             | Descripción                                                                      |
| ---------------------- | -------------------------------------------------------------------------------- |
| **Python**             | Lenguaje de programación utilizado para desarrollar las pruebas automatizadas.   |
| **pytest**             | Framework empleado para la organización y ejecución de los casos de prueba.      |
| **Selenium WebDriver** | Herramienta utilizada para automatizar las interacciones con el navegador web.   |
| **Git / GitHub**       | Sistema de control de versiones y repositorio para la gestión del código fuente. |

---

## 🧪 Técnicas y buenas prácticas aplicadas

### 📂 Page Object Model (POM)

Patrón de diseño utilizado para mejorar la mantenibilidad y escalabilidad del proyecto, encapsulando los elementos y acciones de cada página en clases independientes.

### 🔄 Pruebas End-to-End (E2E)

Automatización y validación del flujo completo del usuario, simulando escenarios reales de uso de la aplicación.

### ⏱️ Esperas explícitas

Implementación de esperas explícitas para manejar elementos dinámicos y sincronizar correctamente la ejecución de las pruebas con el comportamiento de la interfaz.

### 🎯 Estrategias de localización de elementos

Uso de distintos tipos de selectores para identificar elementos de manera eficiente y robusta:

* `ID`
* `Class Name`
* `XPath`

---

## 🎯 Objetivo del proyecto

Fortalecer las habilidades prácticas en **automatización de pruebas web**, aplicando principios de diseño de pruebas y buenas prácticas de desarrollo para garantizar la calidad y confiabilidad de aplicaciones orientadas al usuario final.

---

## ▶️ Ejecución de las pruebas

Para ejecutar el conjunto de pruebas, utiliza el siguiente comando:

```bash
pytest
```

Para obtener una salida más detallada durante la ejecución:

```bash
pytest -v
```

---

## 📌 Habilidades demostradas

* Diseño y automatización de pruebas funcionales.
* Implementación del patrón **Page Object Model**.
* Manejo de elementos dinámicos con Selenium.
* Aplicación de buenas prácticas de automatización.
* Organización de suites de prueba con pytest.
* Uso de Git para el control de versiones.


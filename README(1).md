# Taller 2: Integración de IA Generativa con Google Gemini API 🤖

Este proyecto implementa una solución en Python para interactuar con el
modelo **Gemini 2.5 Flash** de Google.

El archivo principal del proyecto es:

`app_1.py`

El script demuestra el uso de la librería **google-genai** para tareas
de inferencia, procesamiento de lenguaje natural (NLP) con roles
definidos y la creación de un chatbot contextual con memoria.

------------------------------------------------------------------------

## 📋 Descripción de las Actividades

El código (`app_1.py`) resuelve tres ejercicios prácticos:

1.  **Inferencia Básica:**\
    Conexión inicial con la API para generar explicaciones conceptuales
    breves sobre inferencia en IA.

2.  **Procesador de Textos Inteligente:**\
    Sistema que recibe un texto y, dependiendo de la instrucción
    ("resumir" o "profesionalizar"), adapta su respuesta actuando bajo
    el rol de un **Editor Editorial de prestigio**.

3.  **Chatbot de Soporte Técnico:**\
    Asistente virtual para una tienda de tecnología que utiliza
    **Few-Shot Prompting** para mantener un estilo de respuesta amable y
    técnico con memoria conversacional.

------------------------------------------------------------------------

## 🛠️ Requisitos e Instalación

Para ejecutar este proyecto necesitas:

-   Python 3.9 o superior
-   Librerías:

``` bash
pip install google-genai python-dotenv
```

Opcionalmente puedes crear un archivo `requirements.txt` con:

    google-genai
    python-dotenv

------------------------------------------------------------------------

## 🔐 Variables de Entorno

El proyecto utiliza un archivo `.env` para proteger la credencial de
acceso.

Debes crear un archivo `.env` en la raíz del proyecto con el siguiente
contenido:

    GENAI_API_KEY=tu_clave_api_aqui

⚠️ No subir este archivo al repositorio.

------------------------------------------------------------------------

## 💻 Explicación Técnica del Código

El script está estructurado de manera modular y ejecuta secuencialmente
los tres ejercicios.

### 1️⃣ Configuración Inicial

-   Carga variables de entorno con `load_dotenv()`
-   Obtiene la clave con `os.getenv()`
-   Inicializa el cliente con `genai.Client()`

Esto permite autenticarse correctamente contra la API de Gemini.

------------------------------------------------------------------------

### 2️⃣ Ejercicio 1 -- Inferencia Básica

Se utiliza:

``` python
client.models.generate_content()
```

Características:

-   Llamada sin memoria (stateless)
-   Envío directo de prompt
-   Devuelve la respuesta en `response.text`

Valida la conexión correcta con el modelo.

------------------------------------------------------------------------

### 3️⃣ Ejercicio 2 -- Procesador de Textos

Se implementa la función:

``` python
procesar_articulo(texto, tarea)
```

Utiliza:

``` python
types.GenerateContentConfig()
```

Con una **System Instruction**:

    "Eres un Editor Editorial de prestigio..."

Esto obliga al modelo a mantener un estilo formal, técnico y
estructurado.

Dependiendo de la tarea:

-   `"resumir"` → Genera un resumen ejecutivo
-   `"profesionalizar"` → Reescribe en tono formal y técnico

------------------------------------------------------------------------

### 4️⃣ Ejercicio 3 -- Chat de Soporte Técnico

Se utiliza:

``` python
client.chats.create()
```

Diferencias clave frente a la inferencia simple:

-   Mantiene memoria conversacional (stateful)
-   Permite historial precargado (Few-Shot Prompting)
-   Define rol de vendedor amable

Se incluye:

``` python
time.sleep(2)
```

Para evitar el error:

    429 Resource Exhausted

------------------------------------------------------------------------

## 📁 Estructura del Proyecto

    Taller2/
    │── app_1.py
    │── README.md
    │── requirements.txt
    │── .env
    │── img/
        ├── prueba1.png
        └── prueba2.png

------------------------------------------------------------------------

## 🚀 Ejecución

Desde la raíz del proyecto:

``` bash
python app_1.py
```

El script ejecutará automáticamente:

-   Ejercicio 1 -- Inferencia básica
-   Ejercicio 2 -- Procesamiento de texto
-   Ejercicio 3 -- Chat interactivo

Para salir del chat escribir:

    finalizar

------------------------------------------------------------------------

## 📷 Evidencias de Ejecución

### 🔹 Prueba 1 -- Ejercicios 1 y 2

Incluye:

-   Respuesta de inferencia básica\
-   Resultado del resumen\
-   Texto profesionalizado

![Prueba 1](img/prueba1.png)

------------------------------------------------------------------------

### 🔹 Prueba 2 -- Ejercicio 3 (Chat de Soporte)

Incluye:

-   Inicio del chat\
-   Interacción cliente-vendedor\
-   Respuestas generadas por el modelo

![Prueba 2](img/prueba2.png)

------------------------------------------------------------------------

## ⚠️ Posibles Errores

### Error 401

Clave API inválida o mal configurada en el archivo `.env`.

### Error 429

Límite de cuota gratuita alcanzado.\
Solución: esperar unos minutos antes de volver a ejecutar.

### ModuleNotFoundError

Instalar dependencias con:

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## 🧠 Conceptos Aplicados

-   Inferencia en modelos generativos
-   System Instructions
-   Few-Shot Prompting
-   Contexto conversacional
-   Manejo básico de rate limiting

------------------------------------------------------------------------

## 📌 Conclusión

Este proyecto demuestra la integración práctica de un modelo de IA
generativa en un entorno real de desarrollo, aplicando control de
comportamiento mediante roles, memoria contextual y gestión básica de
cuota.

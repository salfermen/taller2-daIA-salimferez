# Taller 2: Integración de IA Generativa con Google Gemini API 🤖

Este proyecto implementa una solución en Python para interactuar con el modelo **Gemini 2.0 Flash** de Google. El script demuestra el uso de la librería `google-genai` para tareas de inferencia, procesamiento de lenguaje natural (NLP) con roles definidos y la creación de un chatbot contextual.

## 📋 Descripción de las Actividades

El código (`app_1.py`) resuelve tres ejercicios prácticos de desarrollo con IA:

1.  **Inferencia Básica:** Conexión inicial con la API para generar explicaciones conceptuales breves.
2.  **Procesador de Textos Inteligente:** Un sistema capaz de recibir un texto y, dependiendo de la instrucción ("resumir" o "profesionalizar"), adaptar su respuesta actuando bajo el rol de un **Editor Editorial**.
3.  **Chatbot de Soporte Técnico:** Un asistente virtual para una tienda de tecnología que utiliza **Few-Shot Learning** (aprendizaje con pocos ejemplos) para mantener un estilo de respuesta amable y técnico.

---

## 🛠️ Requisitos e Instalación

Para ejecutar este proyecto, solo necesitas las librerías estándar definidas en el entorno virtual.

1.  **Entorno Python:** Asegúrate de tener Python 3.9 o superior.
2.  **Librerías:**
    ```bash
    pip install google-genai python-dotenv
    ```
3.  **Variables de Entorno:**
    El proyecto utiliza un archivo `.env` para proteger la credencial de acceso. Debes crear un archivo `.env` en la raíz con el siguiente contenido:
    ```env
    GENAI_API_KEY=tu_clave_api_aqui
    ```

---

## 💻 Explicación Técnica del Código

El script funciona de manera modular ejecutando secuencialmente los tres ejercicios. A continuación, se detalla la lógica implementada:

### 1. Configuración de Roles (System Instructions)
Para los ejercicios 2 y 3, no usamos un prompt simple. Utilizamos `types.GenerateContentConfig` para inyectar una **Instrucción de Sistema**.
* *¿Qué hace?* Define la personalidad de la IA antes de que empiece a hablar.
* *Ejemplo en código:*
    ```python
    system_instruction="Eres un Editor Editorial de prestigio..."
    ```
    Esto garantiza que, sin importar lo que el usuario envíe, la IA mantenga su personaje formal.

### 2. Historial y Contexto (Few-Shot Prompting)
En el **Ejercicio 3 (Chat)**, implementamos una técnica llamada "Few-Shot". En lugar de un chat vacío, le pasamos una lista `history` con ejemplos de conversaciones ideales (Usuario -> Modelo).
* **Beneficio:** El modelo "aprende" qué tipo de productos vendemos y qué tono usar antes de recibir la primera pregunta real del usuario.

### 3. Manejo de Cuotas (Rate Limiting)
Dado que utilizamos la versión gratuita de la API, el código incluye pausas estratégicas (`time.sleep`) entre ejecuciones. Esto evita el error `429 Resource Exhausted` y asegura que el script corra de principio a fin sin interrupciones.

---

## 🚀 Ejecución y Pruebas

Para correr el script completo, utiliza el comando:

```bash
.\app_1.py

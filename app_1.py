import os
import time
from dotenv import load_dotenv
from google import genai
from google.genai import types

# --- CONFIGURACIÓN INICIAL ---
load_dotenv()
API_KEY = os.getenv("GENAI_API_KEY") # Asegúrate que en tu .env la variable se llame así
client = genai.Client(api_key=API_KEY)

# Usamos flash por ser rápido y eficiente con la cuota gratuita
MODELO = "gemini-2.0-flash"

# ==========================================
# EJERCICIO 1: Conexión y Petición Básica (20%)
# ==========================================
def ejercicio_1_inferencia():
    print("\n--- EJERCICIO 1: Concepto de Inferencia ---")
    prompt = "Explica qué es la 'Inferencia en IA' en menos de 50 palabras."
    
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        print(f"Respuesta del modelo:\n{response.text}")
    except Exception as e:
        print(f"Error en Ejercicio 1: {e}")

# ==========================================
# EJERCICIO 2: Procesador de Textos (30%)
# ==========================================
def procesar_articulo(texto, tarea):
    print(f"\n--- EJERCICIO 2: Procesando '{tarea}' ---")
    
    # Restricción: System Instruction de "Editor Editorial de prestigio"
    config_editor = types.GenerateContentConfig(
        system_instruction="Eres un Editor Editorial de prestigio. Tu redacción es impecable, sofisticada y técnica.",
        max_output_tokens=500
    )

    # Lógica según la tarea
    if tarea == "resumir":
        prompt_final = f"Genera un resumen ejecutivo del siguiente texto: {texto}"
    elif tarea == "profesionalizar":
        prompt_final = f"Reescribe el siguiente texto para que suene formal y técnico: {texto}"
    else:
        return "Tarea no reconocida."

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt_final,
            config=config_editor
        )
        return response.text
    except Exception as e:
        return f"Error: {e}"

# ==========================================
# EJERCICIO 3: Chat de Soporte (50%)
# ==========================================
def iniciar_chat_soporte():
    print("\n--- EJERCICIO 3: Chat de Soporte Técnico ---")
    print("(Escribe 'finalizar' para salir)\n")

    # Configuración del Rol: Vendedor Amable
    config_vendedor = types.GenerateContentConfig(
        system_instruction="Eres un vendedor amable de una tienda de tecnología. Tu objetivo es ayudar al cliente a encontrar el mejor producto.",
        max_output_tokens=150 # Respuestas cortas para ahorrar cuota
    )

    # Historial Few-shot (Contexto precargado)
    historial = [
        {"role": "user", "parts": [{"text": "Hola, busco una laptop para juegos."}]},
        {"role": "model", "parts": [{"text": "¡Hola! Claro que sí. Te recomiendo mucho la ASUS ROG Zephyrus. Tiene una tarjeta gráfica excelente y muy buena refrigeración."}]},
        {"role": "user", "parts": [{"text": "¿Y tienen audífonos con cancelación de ruido?"}]},
        {"role": "model", "parts": [{"text": "Sí, tenemos los Sony WH-1000XM5. Son líderes en el mercado y muy cómodos para usar todo el día."}]}
    ]

    try:
        # Inicialización del chat
        chat = client.chats.create(
            model="gemini-2.5-flash",
            config=config_vendedor,
            history=historial
        )

        while True:
            user_input = input("Cliente: ")
            
            if user_input.lower() == "finalizar":
                print("Vendedor: ¡Gracias por tu visita! Que tengas un excelente día.")
                break
            
            # Envío del mensaje
            response = chat.send_message(user_input)
            print(f"Vendedor: {response.text}\n")
            
            # Pausa de seguridad para evitar error 429
            time.sleep(2)

    except Exception as e:
        print(f"Error en el chat: {e}")

# ==========================================
# BLOQUE PRINCIPAL DE EJECUCIÓN
# ==========================================
if __name__ == "__main__":
    # 1. Ejecutamos Ejercicio 1
    ejercicio_1_inferencia()
    time.sleep(2) # Pausa para respirar
    
    # 2. Ejecutamos Ejercicio 2
    texto_ejemplo = "La inteligencia artificial sirve para que las compus aprendan cosas solas y nos ayuden en el trabajo."
    
    resultado_resumen = procesar_articulo(texto_ejemplo, "resumir")
    print(f"Resultado Resumen:\n{resultado_resumen}")
    time.sleep(2)

    resultado_prof = procesar_articulo(texto_ejemplo, "profesionalizar")
    print(f"Resultado Profesional:\n{resultado_prof}")
    time.sleep(2)

    # 3. Ejecutamos Ejercicio 3
    iniciar_chat_soporte()
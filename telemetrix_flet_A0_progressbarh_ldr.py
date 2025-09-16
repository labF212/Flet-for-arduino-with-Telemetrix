from telemetrix import telemetrix
import flet as ft
import threading
import time
import asyncio

# Defina os pinos analógicos
ANALOG_PIN0 = 0

# Crie uma instância do Telemetrix
board = telemetrix.Telemetrix()

# Dicionário para armazenar os valores analógicos
analog_values = {ANALOG_PIN0: 0}

# Função de callback para atualizar os valores analógicos
def callback(data):
    pin = data[1]
    value = data[2]
    analog_values[pin] = value

# Configurar os pinos analógicos com callback
board.set_pin_mode_analog_input(ANALOG_PIN0, callback=callback)

# Função para ler e atualizar os valores analógicos
def read_analog_values():
    while True:
        time.sleep(0.1)

# Iniciar a thread para ler os valores analógicos em segundo plano
read_analog_thread = threading.Thread(target=read_analog_values, daemon=True)
read_analog_thread.start()

# Função principal do Flet
async def main(page: ft.Page):
    page.title = "Leitura Analógica com Telemetrix e Flet - LDR"

    # Barra de progresso mais "gorda"
    progress_bar_a0 = ft.ProgressBar(value=0, width=400, height=30, color="blue")

    # Texto para mostrar a tensão
    progress_text_a0 = ft.Text(value="None", size=20)

    # Botão de saída
    exit_button = ft.ElevatedButton(
        text="Exit",
        on_click=lambda _: (board.shutdown(), page.window.destroy())
    )

    # Layout
    page.add(
        ft.Row(
            [
                ft.Text("Leitura de Luminosidade ambiente atráves de um sensor LDR na porta A0"),
            ],
            alignment="center"
        ),
        ft.Row(
            [
                ft.Text("Claro", size=16),
                progress_bar_a0,
                ft.Text("Escuro", size=16),
            ],
            alignment="center"
        ),
        ft.Row(
            [progress_text_a0],
            alignment="center"
        ),
        ft.Row(
            [exit_button],
            alignment="center"
        ),
    )

    # Loop de atualização periódica
    while True:
        progress_bar_a0.value = analog_values[ANALOG_PIN0] / 1024
        progress_text_a0.value = f'{analog_values[ANALOG_PIN0] * (5.0 / 1023):.2f} V'

        page.update()
        await asyncio.sleep(0.1)

    board.shutdown()

# Inicializa a aplicação Flet
ft.app(target=main)

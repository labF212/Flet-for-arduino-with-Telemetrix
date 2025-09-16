import time
import asyncio
import flet as ft
import matplotlib.pyplot as plt
from flet.matplotlib_chart import MatplotlibChart
from telemetrix import telemetrix

# -------------------------------
# CONFIGURAÇÃO DO SENSOR
# -------------------------------
DHT_PIN = 4  # Pino digital confiável no Arduino
board = telemetrix.Telemetrix()

temperature = 0.0
humidity = 0.0

def dht_callback(data):
    global temperature, humidity
    pin, device_type, error, hum, temp = data
    if error == 0:
        humidity = hum
        temperature = temp
    else:
        print(f"[DHT22] Erro de leitura no pino {pin}")

# Inicializa DHT22
board.set_pin_mode_dht(DHT_PIN, dht_type=22, callback=dht_callback)

# -------------------------------
# FUNÇÃO PRINCIPAL FLET
# -------------------------------
async def main(page: ft.Page):
    page.title = "Temperatura e Humidade - Flet + Telemetrix"
    page.theme_mode = ft.ThemeMode.DARK

    bar_width, bar_height = 280, 50

    temp_text = ft.Text(value="Temperatura: 0.0 ºC", size=16)
    humid_text = ft.Text(value="Humidade: 0.0 %", size=16)

    temp_value_text = ft.Text(value="0.0 ºC", size=14)
    humid_value_text = ft.Text(value="0.0 %", size=14)

    temp_bar = ft.Container(
        content=ft.Stack([
            ft.Container(width=bar_width, height=bar_height, bgcolor="grey"),
            ft.Container(width=0, height=bar_height, bgcolor="red", alignment=ft.alignment.top_left),
            ft.Container(content=temp_value_text, alignment=ft.alignment.center),
        ]),
        width=bar_width,
        height=bar_height,
    )

    humid_bar = ft.Container(
        content=ft.Stack([
            ft.Container(width=bar_width, height=bar_height, bgcolor="grey"),
            ft.Container(width=0, height=bar_height, bgcolor="blue", alignment=ft.alignment.top_left),
            ft.Container(content=humid_value_text, alignment=ft.alignment.center),
        ]),
        width=bar_width,
        height=bar_height,
    )

    # Dados do gráfico
    times = list(range(100))
    temp_data = [0] * 100
    humid_data = [0] * 100

    fig, ax = plt.subplots(figsize=(6, 3))
    ax.set_ylim(0, 100)
    ax.set_title("Leituras em tempo real")
    ax.set_xlabel("Amostras")
    ax.set_ylabel("Valor")
    line_temp, = ax.plot(times, temp_data, label="Temperatura (ºC)", color='red')
    line_humid, = ax.plot(times, humid_data, label="Humidade (%)", color='blue')
    ax.legend()
    ax.grid(True)

    chart = MatplotlibChart(fig, expand=True)

    exit_btn = ft.ElevatedButton(
        text="Sair", 
        on_click=lambda _: page.window.close(),
        icon=ft.Icons.EXIT_TO_APP,
    )

    page.add(
        ft.Column([
            temp_text,
            temp_bar,
            humid_text,
            humid_bar,
            ft.Container(content=chart, padding=10, width=600, height=300),
            exit_btn
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

    # Loop principal
    while True:
        # Atualiza textos
        temp_text.value = f"Temperatura: {temperature:.1f} ºC"
        humid_text.value = f"Humidade: {humidity:.1f} %"
        temp_value_text.value = f"{temperature:.1f} ºC"
        humid_value_text.value = f"{humidity:.1f} %"

        # Atualiza barras (normalização segura)
        temp_bar.content.controls[1].width = max(0, min((temperature / 50) * bar_width, bar_width))
        humid_bar.content.controls[1].width = max(0, min((humidity / 100) * bar_width, bar_width))

        # Atualiza gráfico
        temp_data.append(temperature)
        humid_data.append(humidity)
        temp_data.pop(0)
        humid_data.pop(0)
        line_temp.set_ydata(temp_data)
        line_humid.set_ydata(humid_data)
        chart.update()

        page.update()
        await asyncio.sleep(2)  # intervalo entre leituras

# -------------------------------
# EXECUÇÃO DO APP
# -------------------------------
ft.app(target=main)

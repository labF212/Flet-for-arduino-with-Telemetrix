import flet as ft
from telemetrix import telemetrix
import threading

# --- configuração hardware ---
PIN_RELE = 7   # pino do relé
PIN_PIR  = 2   # pino do PIR

# Cria a ligação ao Arduino
board = telemetrix.Telemetrix()
board.set_pin_mode_digital_output(PIN_RELE)

# Função para controlar o relé (active-HIGH)
def control_relay(state: str):
    if state == "ON":
        board.digital_write(PIN_RELE, 1)  # Liga
    elif state == "OFF":
        board.digital_write(PIN_RELE, 0)  # Desliga


def main(page: ft.Page):
    page.title = "Relé com PIR (5s delay)"
    page.theme_mode = ft.ThemeMode.DARK

    # UI widgets
    pir_icon = ft.Icon(ft.Icons.CIRCLE, color="red", size=60)
    pir_status = ft.Text("Sem movimento", size=16)
    rele_icon = ft.Icon(ft.Icons.CIRCLE, color="red", size=60)

    # Timer global para desligar
    off_timer = {"t": None}

    # Callback do PIR
    def pir_callback(msg):
        if not isinstance(msg, (list, tuple)) or len(msg) < 3:
            print("Mensagem estranha do PIR:", msg)
            return

        value = int(msg[2])  # 1 = movimento, 0 = sem movimento

        if value == 1:  # Movimento DETETADO
            # Cancela desligar agendado
            if off_timer["t"] is not None:
                off_timer["t"].cancel()
                off_timer["t"] = None

            control_relay("ON")
            pir_icon.color = "green"
            pir_status.value = "Movimento!"
            rele_icon.color = "green"

        else:  # Sem movimento → espera 5s antes de desligar
            pir_icon.color = "red"
            pir_status.value = "Sem movimento"

            def delayed_off():
                control_relay("OFF")
                rele_icon.color = "red"
                page.update()

            off_timer["t"] = threading.Timer(5.0, delayed_off)
            off_timer["t"].start()

        page.update()

    # Regista o PIR como entrada com callback
    board.set_pin_mode_digital_input(PIN_PIR, callback=pir_callback)

    # Layout
    page.add(
        ft.Row(
            [
                ft.Column([pir_icon, pir_status], alignment=ft.MainAxisAlignment.CENTER),
                ft.Column([rele_icon, ft.Text("Relé (controlado pelo PIR)")], alignment=ft.MainAxisAlignment.CENTER),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=40
        ),
        ft.Row([
            ft.ElevatedButton(
                'Exit',
                icon=ft.Icons.EXIT_TO_APP,
                on_click=lambda e: (board.shutdown(), page.window.destroy())
            )
        ], alignment=ft.MainAxisAlignment.CENTER)
    )

    def on_window_close(e):
        if off_timer["t"] is not None:
            off_timer["t"].cancel()
        board.shutdown()
    page.on_window_close = on_window_close


if __name__ == "__main__":
    ft.app(target=main)

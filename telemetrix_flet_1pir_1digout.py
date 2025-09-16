import flet as ft
from telemetrix import telemetrix
import threading

# --- configuração hardware ---
board = telemetrix.Telemetrix()
PIN_RELE = 7   # pino do relé
PIN_PIR = 2    # pino do PIR
RELAY_ACTIVE_LOW = True   # True se o relé liga com LOW

# garante pino do relé como saída e estado inicial (desligado)
board.set_pin_mode_digital_output(PIN_RELE)
initial_off = 1 if RELAY_ACTIVE_LOW else 0
try:
    board.digital_write(PIN_RELE, initial_off)
except Exception as e:
    print("Aviso!: inicial digital_write falhou:", e)


def main(page: ft.Page):
    page.title = "Relé com PIR"
    page.theme_mode = ft.ThemeMode.DARK

    # UI widgets
    pir_icon = ft.Icon(ft.Icons.CIRCLE, color="red", size=60)
    pir_status = ft.Text("Sem movimento", size=16)
    rele_icon = ft.Icon(ft.Icons.CIRCLE, color="red", size=60)

    # Timer global para desligar o relé
    off_timer = {"t": None}

    # função utilitária para escrever no relé
    def write_relay(on: bool):
        try:
            if on:
                out = 0 if RELAY_ACTIVE_LOW else 1
            else:
                out = 1 if RELAY_ACTIVE_LOW else 0
            board.digital_write(PIN_RELE, out)
        except Exception as e:
            print("digital_write error:", e)

    # botões de teste manual
    ligar_btn = ft.ElevatedButton("Ligar (teste)", on_click=lambda e: (write_relay(True), rele_icon.update()))
    desligar_btn = ft.ElevatedButton("Desligar (teste)", on_click=lambda e: (write_relay(False), rele_icon.update()))

    # callback para o PIR
    def pir_callback(msg):
        if not isinstance(msg, (list, tuple)) or len(msg) < 3:
            print("Mensagem estranha do PIR:", msg)
            return

        value = int(msg[2])  # valor do PIR

        if value == 1:  # Movimento detetado
            # Cancela qualquer timer anterior
            if off_timer["t"] is not None:
                off_timer["t"].cancel()
                off_timer["t"] = None

            write_relay(True)
            pir_icon.color = "green"
            pir_status.value = "Movimento!"
            rele_icon.color = "green"

        else:  # PIR deixou de detetar
            pir_icon.color = "red"
            pir_status.value = "Sem movimento"
            rele_icon.color = "red"

            # Cria um timer de 5s para desligar o relé
            def delayed_off():
                write_relay(False)
                rele_icon.color = "red"
                page.update()

            off_timer["t"] = threading.Timer(5.0, delayed_off)
            off_timer["t"].start()

        # Atualiza interface
        page.update()

    # regista o pino do PIR como entrada com callback
    try:
        board.set_pin_mode_digital_input(PIN_PIR, callback=pir_callback)
    except Exception as e:
        print("Erro ao registar callback digital input:", e)

    # layout
    page.add(
        ft.Row(
            [
                ft.Column([pir_icon, pir_status], alignment=ft.MainAxisAlignment.CENTER),
                ft.Column([rele_icon, ft.Text("Relé (controlado pelo PIR)")], alignment=ft.MainAxisAlignment.CENTER),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=40
        ),
        ft.Row([ligar_btn, desligar_btn], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
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

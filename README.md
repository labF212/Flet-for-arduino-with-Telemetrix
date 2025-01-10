# Flet for Arduino
## English

### About Flet
Flet is a graphical programming module where developers can easily create real-time web, mobile, and desktop applications in Python.

- **Programming Examples**: [Flet Controls Gallery](https://flet-controls-gallery.fly.dev/layout)
- **Documentation**: [Flet Documentation](https://flet.dev/docs/)

### Installation

Create a virtual environment by running the following commands in your terminal:

```bash
mkdir first-flet-app
cd first-flet-app
python3 -m venv .venv
source .venv/bin/activate
```

Once the virtual environment is activated, you'll see a `(.venv)` prefix in your terminal prompt.

Install the latest version of Flet within the virtual environment:

```bash
pip install flet
```

Check the installed Flet version:

```bash
flet --version
```

### Additional Dependencies for Audio and Video

#### GStreamer for Audio
If your Flet app uses the Audio control, install GStreamer libraries. For Ubuntu/Debian, run:

**Minimal Installation:**

```bash
sudo apt install libgtk-3-dev libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev
```

**Full Installation:**

```bash
sudo apt install libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgstreamer-plugins-bad1.0-dev gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-doc gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio
```

#### MPV for Video
If your Flet app uses the Video control, install `libmpv` libraries. For Ubuntu/Debian, run:

```bash
sudo apt install libmpv-dev mpv
```
## Telemetrix

The **Telemetrix Project** is a modern replacement for Arduino StandardFirmata, equipped with many more built-in features than StandardFirmata. The project consists of Python APIs to create Python client applications and C++ servers that communicate with the Python client via serial port or Wi-Fi.

### Installing Telemetrix

To install Telemetrix on Linux (including Raspberry Pi) and macOS:

```bash
sudo pip3 install telemetrix
```

For Windows users:

```bash
pip install telemetrix
```

To communicate between Python and Arduino, you need to upload a program to the Arduino following the instructions at:  
[Telemetrix Instructions for Arduino](https://mryslab.github.io/telemetrix/telemetrix4arduino/)



# Flet para Arduino (Português)
O Flet é um módulo de programação gráfica em que os programadores criam facilmente aplicações Web, móveis e de desktop em tempo real em Python.

 **Exemplos de Programação**: [Galeria de Controles Flet](https://flet-controls-gallery.fly.dev/layout)
- **Documentação**: [Documentação Flet](https://flet.dev/docs/)

### Instalação

Crie um ambiente virtual executando os seguintes comandos no terminal:

```bash
mkdir first-flet-app
cd first-flet-app
python3 -m venv .venv
source .venv/bin/activate
```

Depois de ativar o ambiente virtual, verá o prefixo `(.venv)` no seu terminal.

Instale a versão mais recente do Flet no ambiente virtual:

```bash
pip install flet
```

Verifique a versão instalada do Flet:

```bash
flet --version
```

### Dependências Adicionais para Áudio e Vídeo

#### GStreamer para Áudio
Se a sua aplicação Flet utiliza o controle de Áudio, instale as bibliotecas GStreamer. Para Ubuntu/Debian, execute:

**Instalação Mínima:**

```bash
sudo apt install libgtk-3-dev libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev
```

**Instalação Completa:**

```bash
sudo apt install libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgstreamer-plugins-bad1.0-dev gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-doc gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio
```

#### MPV para Vídeo
Se a sua aplicação Flet utiliza o controle de Vídeo, instale as bibliotecas `libmpv`. Para Ubuntu/Debian, execute:

```bash
sudo apt install libmpv-dev mpv
```

## Telemetrix
O **Projeto Telemetrix** é uma substituição moderna para o Arduino StandardFirmata, equipado com muitos mais recursos integrados do que o StandardFirmata. O projeto consiste em APIs Python para criar aplicações cliente em Python e servidores C++ que comunicam com o cliente Python via porta série ou Wi-Fi.

### Instalação do Telemetrix

Para instalar o Telemetrix no Linux (incluindo Raspberry Pi) e macOS:

```bash
sudo pip3 install telemetrix
```

Para utilizadores de Windows:

```bash
pip install telemetrix
```

Para comunicar o Python com o Arduino, será necessário transferir um programa para o Arduino seguindo as instruções em:  
[Telemetrix Instructions for Arduino](https://mryslab.github.io/telemetrix/telemetrix4arduino/)

---

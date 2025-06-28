# V2X BSM Decoder (Standalone Python Version)

This is a **standalone Python script** for decoding V2X BSM (Basic Safety Message) data broadcast over DSRC.  
It extracts and decodes J2735 Message ID `0x14` (BSM) in real time, using live network capture without requiring ROS or any robotic middleware.

---

## Features

- **Live capture** of V2X messages from a network interface
- **Searches for J2735 Message ID = 0x14** in UDP packets (BSM)
- **Decodes** using ASN.1 J2735 definitions (via `pycrate`)
- **Prints structured BSM data** (e.g. latitude, longitude, speed) as formatted JSON
- Fully standalone, **no ROS required**

---

## 📁 Project Structure

v2x_project/
├── bsm_decoder_standalone.py # Main script (run this)
├── out.py # Auto-generated J2735 ASN.1 decoder (via pycrate)

---

## ⚙️ Requirements

- Python 3.7+
- [pyshark](https://github.com/KimiNewt/pyshark) – for packet sniffing
- [pycrate](https://github.com/P1sec/pycrate) – for ASN.1 decoding
- Wireshark must be installed (for pyshark to work)

```bash
pip install pyshark pycrate

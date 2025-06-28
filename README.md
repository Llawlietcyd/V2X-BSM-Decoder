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

```
v2x_project/
├── bsm_decoder_standalone.py   # Main script (run this)
└── out.py                      # Auto-generated J2735 ASN.1 decoder (via pycrate)
```

---

## ⚙️ Requirements

- Python 3.7+
- [pyshark](https://github.com/KimiNewt/pyshark) – for packet sniffing
- [pycrate](https://github.com/P1sec/pycrate) – for ASN.1 decoding
- Wireshark must be installed (for pyshark to work)


Install with:

```bash
pip install pyshark pycrate
```

---

## 🚀 Usage

### 1. Connect your DSRC-capable device (e.g. OBU)
Make sure it's visible as a network interface (e.g. `enp0s31f6`, `wlan0`, etc.)
### 2. Run the decoder
```
python3 bsm_decoder_standalone.py
```
decoder = BSMDecoder(interface_name='your_interface_here')

##  Output
Messages containing "0014" (BSM) are captured, decoded, and printed every second.

Output format: structured JSON

Example:
```
{
  "messageId": 20,
  "value": {
    "coreData": {
      "msgCnt": 58,
      "lat": 401042907,
      "long": -831334996,
      "speed": 10,
      ...
    }
  }
}
```
### 📌 Notes
The out.py file is generated from SAE J2735 ASN.1 definitions using pycrate_asn1c. If needed, you can regenerate it from SPAT.asn / J2735.asn.

This version only supports BSM (Message ID 20 / 0x14), but can be extended to support SPaT, MAP, etc.

### 🧠 Author
Developed by Yidian Chen
Originally adapted from a ROS 2 project v2x_send_spat.



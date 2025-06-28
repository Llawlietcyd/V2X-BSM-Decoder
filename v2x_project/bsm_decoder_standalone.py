# bsm_decoder_standalone.py
import os
import binascii
import json
import threading
import time
import pyshark

from out import DSRC

class BSMDecoder:
    def __init__(self, interface_name='enp0s31f6'):
        self.interface_name = interface_name
        self.decoded_bsm_list = []
        self.lock = threading.Lock()
        self.stop_flag = False

    def start(self):
        self.capture_thread = threading.Thread(target=self.capture_dsrc_packets)
        self.capture_thread.start()

        try:
            while not self.stop_flag:
                self.timer_callback()
                time.sleep(1.0)
        except KeyboardInterrupt:
            print("[INFO] Stopping capture...")
            self.stop_flag = True
            self.capture_thread.join()

    def capture_dsrc_packets(self):
        cap = pyshark.LiveCapture(interface=self.interface_name, display_filter='udp')
        print(f"[INFO] Started capture on {self.interface_name} (UDP only)")

        for pkt in cap:
            if self.stop_flag:
                break
            try:
                if hasattr(pkt, 'data'):
                    raw_hex = pkt.data.data.replace(':', '')
                else:
                    continue

                index = raw_hex.find("0014")
                if index != -1:
                    j2735_hex = raw_hex[index:]
                    decoded_json_str = self.decode_j2735(j2735_hex)
                    if decoded_json_str:
                        decoded_dict = json.loads(decoded_json_str)
                        with self.lock:
                            self.decoded_bsm_list.append(decoded_dict)
            except Exception as e:
                print(f"[ERROR] Capture error: {e}")

    def decode_j2735(self, hex_string):
        try:
            msg_frame = DSRC.MessageFrame
            decoded = msg_frame.from_uper(binascii.unhexlify(hex_string))
            return msg_frame.to_json(decoded)
        except Exception as e:
            print(f"[ERROR] Decode error: {e}")
            return None

    def timer_callback(self):
        with self.lock:
            local_list = self.decoded_bsm_list
            self.decoded_bsm_list = []

        for item in local_list:
            print(json.dumps(item, indent=2))


if __name__ == '__main__':
    decoder = BSMDecoder(interface_name='enp0s31f6')
    decoder.start()

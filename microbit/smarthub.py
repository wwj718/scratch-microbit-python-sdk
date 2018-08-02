import pygatt
from pygatt.backends.bgapi.bgapi import *
# from microbit.bluetooth.bluetooth_io import BluetoothIO
# from microbit.bluetooth.connect_info import IOType
# from microbit.bluetooth.service_manager import ServiceManager


adapter = None


class Smarthub:
    '''
    usage:
    from microbit.smarthub import Smarthub
    hub = Smarthub()
    '''
    def __init__(self):
        global adapter
        if adapter is None:
            adapter = _Patched_BGAPIBackend()
            adapter.start()

        self.io = None
        self.service_manager = None
        self.device = None

        devices = adapter.scan(1)
        devices = sorted(devices, key=lambda k: k['rssi'], reverse=True)
        # print("devices:",devices)
        device_address = devices[0]['address']
        ADDRESS_TYPE = pygatt.BLEAddressType.random
        self.device = adapter.connect(device_address, address_type=ADDRESS_TYPE)
        # self.io = BluetoothIO(self.device)
        # self.service_manager = ServiceManager(self.io)

    def disconnect(self):
        adapter.stop()

# A temporary pygatt patch
class _Patched_BGAPIBackend(BGAPIBackend):

    def _open_serial_port(self):
        """
        Open a connection to the named serial port, or auto-detect the first
        port matching the BLED device. This will wait until data can actually be
        read from the connection, so it will not return until the device is
        fully booted.

        Raises a NotConnectedError if the device cannot connect after 10
        attempts, with a short pause in between each attempt.
        """
        for attempt in range(MAX_RECONNECTION_ATTEMPTS):
            try:
                serial_port = self._serial_port or self._detect_device_port()
                self._ser = None

                log.debug("Attempting to connect to serial port after "
                          "restarting device")
                self._ser = serial.Serial(serial_port, baudrate=115200,
                                          timeout=0.25)
                # Wait until we can actually read from the device
                self._ser.read()
                break
            except (BGAPIError, serial.serialutil.SerialException,
                    serial_exception):
                if self._ser:
                    self._ser.close()
                """
                elif attempt == 0:
                    raise NotConnectedError(
                        "No BGAPI compatible device detected")
                """
                self._ser = None
                time.sleep(0.25)
        else:
            raise NotConnectedError("Unable to reconnect with USB "
                                    "device after rebooting")
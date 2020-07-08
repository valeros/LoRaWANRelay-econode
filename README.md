[![Build Status](https://github.com/valeros/LoRaWANRelay-econode/workflows/Run/badge.svg)](https://github.com/valeros/LoRaWANRelay-econode/actions)

How to build PlatformIO based project
=====================================

1. Install PlatformIO Core http://docs.platformio.org/page/core.html
2. Run the following commands:

```bash
# Clone project
> git clone --recursive https://github.com/valeros/LoRaWANRelay-econode.git

# Change working directory
> cd LoRaWANRelay-econode

# Build project
> platformio run

# Upload firmware
> platformio run --target upload

# Clean build files
> platformio run --target clean
```

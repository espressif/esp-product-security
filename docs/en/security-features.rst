.. _security_features:

Security Features
=================

Espressif SoCs are designed with a comprehensive set of security features to protect devices, data, and communications throughout their lifecycle. Espressif's portfolio includes both **Xtensa** and **RISC-V** based architectures, each offering robust security capabilities with some advanced features like ESP-TEE being exclusive to RISC-V platforms.

This guide provides an overview of the key security mechanisms available across Espressif platforms, with references to the ESP-IDF Programming Guide, SoC Technical Reference Manuals (TRMs), and datasheets for further details.

Espressif SoC Security & Crypto Feature Matrix
-----------------------------------------------

.. list-table:: Espressif SoC Security & Crypto Feature Matrix
   :header-rows: 1
   :widths: 14 6 6 6 6 6 6 6 6 6 6

   * - Feature
     - ESP32
     - S2
     - S3
     - C3
     - C2
     - C6
     - H2
     - P4
     - C5
     - C61
   * - AES
     - ✓
     - ✓
     - ✓
     - ✓
     -
     - ✓
     - ✓
     - ✓
     - ✓
     -
   * - SHA
     - ✓
     - ✓
     - ✓
     - ✓
     - ✓
     - ✓
     - ✓
     - ✓
     - ✓
     - ✓
   * - RSA
     - ✓
     - ✓
     - ✓
     - ✓
     -
     - ✓
     - ✓
     - ✓
     - ✓
     -
   * - Secure Boot (RSA)
     - ✓
     - ✓
     - ✓
     - ✓
     -
     - ✓
     - ✓
     - ✓
     - ✓
     -
   * - Secure Boot (ECDSA)
     -
     -
     -
     -
     - ✓
     - ✓
     - ✓
     - ✓
     - ✓
     - ✓
   * - Secure Boot (Revocation)
     -
     - ✓
     - ✓
     - ✓
     -
     - ✓
     - ✓
     - ✓
     - ✓
     - ✓
   * - Flash Encryption
     - ✓
     - ✓
     - ✓
     - ✓
     - ✓
     - ✓
     - ✓
     - ✓
     - ✓
     - ✓
   * - PSRAM Encryption
     -
     - ✓
     - ✓
     - NA
     - NA
     - NA
     - NA
     - ✓
     - ✓
     - ✓
   * - HMAC
     -
     - ✓
     - ✓
     - ✓
     -
     - ✓
     - ✓
     - ✓
     - ✓
     -
   * - Digital Signature (RSA)
     -
     - ✓
     - ✓
     - ✓
     -
     - ✓
     - ✓
     - ✓
     - ✓
     -
   * - ECC
     -
     -
     -
     -
     - ✓
     - ✓
     - ✓
     - ✓
     - ✓
     - ✓
   * - ECDSA
     -
     -
     -
     -
     -
     -
     - ✓
     - ✓
     - ✓
     - ✓
   * - APM/TEE
     -
     -
     -
     -
     -
     - ✓
     - ✓
     - ✓
     - ✓
     - ✓
   * - Key Manager
     -
     -
     -
     -
     -
     -
     -
     - ✓
     - ✓
     - ✓
   * - DPA Protection
     -
     -
     -
     -
     -
     - ✓
     - ✓
     -
     - ✓
     - ✓
   * - AES Pseudo-Round Protection
     -
     -
     -
     -
     -
     -
     - ✓
     -
     - ✓
     - ✓

.. note::
   ✓ indicates the feature is supported in hardware. For documentation and SoC capability details, see the ESP-IDF Security Guide and the respective ``soc_caps.h`` files for each SoC family.

Platform Security
-----------------

Secure Boot
~~~~~~~~~~~
Secure Boot ensures that only authenticated firmware is executed on the device, forming a chain of trust from the bootloader to the application. Signature verification occurs at boot and during OTA updates.

- **Key documentation:**

  - `ESP-IDF Secure Boot Guide <https://docs.espressif.com/projects/esp-idf/en/latest/esp32c6/security/secure-boot-v2.html>`_

Flash/PSRAM Encryption
~~~~~~~~~~~~~~~~~~~~~~
Flash Encryption protects the confidentiality of code and data stored in off-chip flash and PSRAM memory by encrypting contents transparently.

- **Key documentation:**
  
  - `ESP-IDF Flash Encryption Guide <https://docs.espressif.com/projects/esp-idf/en/latest/esp32c6/security/flash-encryption.html>`_
  - See the "External Memory Encryption and Decryption" chapter in the SoC TRM and datasheet for supported algorithms and configuration.

Device Identity & Digital Signature
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Espressif SoCs provide hardware-accelerated digital signature peripherals (RSA, ECDSA) for secure device identity and cryptographic operations. Private keys can be stored in eFuse and are inaccessible to software.

- **Key documentation:**
  
  - `ESP-IDF Digital Signature (DS) Guide <https://docs.espressif.com/projects/esp-idf/en/latest/esp32c6/security/ds.html>`_
  - `ESP-IDF ECDSA Guide <https://docs.espressif.com/projects/esp-idf/en/latest/esp32c5/security/ecdsa.html>`_
  - Refer to the "Digital Signature" and "eFuse" sections in the SoC TRM.

Memory Protection
~~~~~~~~~~~~~~~~~
Memory protection mechanisms (e.g., PMS, PMP) enforce access permissions on memory regions, helping prevent code injection and privilege escalation.

- **Key documentation:**
  
  - `ESP-IDF Security Overview: Memory Protection <https://docs.espressif.com/projects/esp-idf/en/latest/esp32c6/security/security.html#memory-protection>`_
  - See the "Permission Control" chapter in the SoC TRM.

Protection Against Side-Channel Attacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Features such as DPA (Differential Power Analysis) protection and AES pseudo-rounds are implemented to mitigate side-channel attacks on cryptographic operations.

- **Key documentation:**
  
  - `ESP-IDF Security Overview: Side-Channel Protection <https://docs.espressif.com/projects/esp-idf/en/latest/esp32c5/security/security.html#protection-against-side-channel-attacks>`_

Debug Interface Control
~~~~~~~~~~~~~~~~~~~~~~~
JTAG and UART download interfaces can be permanently or temporarily disabled via eFuse or HMAC, reducing the attack surface on production devices.

- **Key documentation:**
  
  - `ESP-IDF Security Overview: Debug Interfaces <https://docs.espressif.com/projects/esp-idf/en/latest/esp32c6/security/security.html#debug-interfaces>`_
  - See the "Debug" and "eFuse" chapters in the SoC TRM.

Network Security
----------------

Espressif’s SDK ensures encrypted and authenticated communication over Wi-Fi, Bluetooth, and Thread. With support for Transport Layer Security (TLS), devices can communicate with cloud services and other network peers in secure and authenticated manner.

- **Key documentation:**
  
  - `Network Security Guide <https://docs.espressif.com/projects/esp-idf/en/latest/esp32c6/security/security.html#network-security>`_

Product Security
----------------

Secure OTA Updates
~~~~~~~~~~~~~~~~~~
Over-the-air updates are supported with secure transport (HTTPS), image signing, and optional anti-rollback protection to ensure only trusted firmware is installed.

- **Key documentation:**
  
  - `ESP-IDF Secure OTA Guide <https://docs.espressif.com/projects/esp-idf/en/latest/esp32c6/security/ota.html>`_
  - `ESP-IDF Anti-Rollback Guide <https://docs.espressif.com/projects/esp-idf/en/latest/esp32c6/security/anti-rollback.html>`_

Secure Storage
~~~~~~~~~~~~~~
Sensitive data (e.g., Wi-Fi credentials) can be stored in encrypted NVS partitions, leveraging the platform's flash encryption.

- **Key documentation:**
  
  - `ESP-IDF NVS Encryption Guide <https://docs.espressif.com/projects/esp-idf/en/latest/esp32c6/security/nvs_encryption.html>`_

Secure Device Control
~~~~~~~~~~~~~~~~~~~~~
ESP-IDF provides secure local and remote device control over Wi-Fi/Ethernet (HTTP) or BLE, using the ESP Local Control component.

- **Key documentation:**
  
  - `ESP-IDF ESP Local Control Guide <https://docs.espressif.com/projects/esp-idf/en/latest/esp32c6/api-reference/protocols/esp_local_ctrl.html>`_

Security Policy & Updates
-------------------------

Espressif maintains a proactive security policy, publishing advisories and providing regular software updates to address vulnerabilities.

- **Key documentation:**
  
  - `ESP-IDF Security Policy <https://github.com/espressif/esp-idf/blob/master/SECURITY.md>`_
  - `Espressif Security Advisories <https://github.com/espressif/esp-idf/security/advisories>`_

Further Reading
---------------

- `ESP-IDF Security Overview <https://docs.espressif.com/projects/esp-idf/en/latest/esp32c6/security/security.html>`_
- Refer to the ESP SoC Technical Reference Manuals and datasheets for hardware-specific details.

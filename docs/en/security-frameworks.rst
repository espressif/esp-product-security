.. _security_frameworks:

Security Frameworks
===================

Espressif provides comprehensive security frameworks designed to establish strong security foundations for IoT devices. These frameworks implement defense-in-depth strategies, combining hardware security features with software-based protection mechanisms to ensure robust device security throughout the product lifecycle.

ESP-TEE: Trusted Execution Environment
--------------------------------------

The **ESP-TEE** (Espressif Trusted Execution Environment) is a **RISC-V exclusive security framework** that provides hardware-enforced isolation and robust protection for sensitive operations and data on Espressif's RISC-V based SoCs. ESP-TEE is currently supported on ESP32-C6 (the world's first PSA Certified Level 2 microcontroller), with future support planned for additional RISC-V based Espressif SoCs including ESP32-C5 and ESP32-C61.

Target SoC Support
~~~~~~~~~~~~~~~~~~~

.. list-table:: ESP-TEE Framework Target SoC Support
   :header-rows: 1
   :widths: 25 25 50

   * - SoC Series
     - Support Status
     - Notes
   * - ESP32-C6
     - ✅ Supported
     - Available in ESP-IDF v5.5+, PSA-L2 certified
   * - ESP32-H2
     - 🔍 Preview
     - Early access support available
   * - ESP32-C5
     - 🔄 In Pipeline
     - Planned for future release
   * - ESP32-C61
     - 🔄 In Pipeline
     - Planned for future release

Key Features
~~~~~~~~~~~~

- **Hardware-Enforced Isolation:** ESP-TEE creates a secure environment (TEE) completely separate from the main application environment (REE), ensuring that sensitive computations and data remain protected even if the main application is compromised.
- **Secure Storage:** Sensitive data, including cryptographic keys and certificates, are stored in encrypted flash partitions accessible only to the TEE, providing confidentiality and integrity protection.
- **Device Attestation:** Devices can generate cryptographically signed attestation tokens to prove their identity, security status, and integrity to remote services.
- **Secure OTA Updates:** ESP-TEE supports secure firmware updates for both TEE and REE components, including rollback protection and signature verification to prevent downgrade attacks.
- **Certification Compliance:** ESP-TEE helps products meet modern IoT security standards and certifications (such as PSA Certified) by providing strong isolation boundaries and secure service mechanisms.

Architecture Overview
~~~~~~~~~~~~~~~~~~~~~

ESP-TEE implements a dual-domain architecture that provides clear separation between trusted and untrusted execution environments:

**TEE (Trusted Execution Environment):**

- Runs in Machine mode with the highest privilege level
- Handles all sensitive operations including cryptographic key management
- Manages secure services and enforces security policies
- Protected by hardware-based memory isolation mechanisms

**REE (Rich Execution Environment):**

- Runs the main user application in User mode with restricted privileges
- Interacts with TEE through well-defined secure APIs
- Cannot directly access TEE memory regions or sensitive resources

**Security Features:**

- Separate memory regions with hardware-enforced access controls
- Cryptographic isolation between TEE and REE domains
- Integration with Secure Boot and Flash Encryption for complete system protection
- PMP/APM/TEE enforced isolation boundaries

Implementation Guide
~~~~~~~~~~~~~~~~~~~~

**Prerequisites:**

- ESP32-C6 or supported RISC-V based Espressif SoC
- ESP-IDF v5.5 or later with ESP-TEE support
- Secure Boot and Flash Encryption enabled (recommended)

**Configuration Steps:**

1. Enable ESP-TEE in the ESP-IDF project configuration (``idf.py menuconfig``)
2. Configure memory regions and partition tables for TEE and secure storage
3. Implement TEE services using the provided secure APIs
4. Build and flash both TEE and REE firmware images
5. Verify isolation and security boundaries during testing

**Development Resources:**

- Use ESP-TEE APIs to access secure services from the REE
- Leverage provided examples for common use cases
- Follow security best practices for TEE application development
- Refer to ESP-IDF documentation for detailed implementation guidance

Security Framework Integration
------------------------------

ESP-TEE integrates seamlessly with other Espressif security features to provide comprehensive protection:

- **Secure Boot Integration:** TEE firmware is verified during boot process
- **Flash Encryption Support:** TEE code and data are encrypted in flash memory  
- **Hardware Security Modules:** Integration with dedicated crypto accelerators
- **Key Management:** Secure key derivation and storage within TEE boundaries
- **Attestation Services:** Hardware-backed device identity and integrity verification

Use Cases and Applications
--------------------------

ESP-TEE is particularly beneficial for applications requiring:

- **Secure Key Management:** Protection of cryptographic keys and certificates
- **Device Identity:** Hardware-backed device authentication and attestation
- **Secure Communications:** TLS/DTLS endpoint authentication and key exchange
- **Firmware Protection:** Secure storage and validation of critical firmware components  
- **Compliance Requirements:** Meeting security certification standards (PSA, Common Criteria)
- **Edge AI Security:** Protection of ML models and inference data

Further Reading
---------------

**Technical Documentation:**

- `ESP-TEE User Guide <https://docs.espressif.com/projects/esp-idf/en/latest/esp32c6/security/tee/index.html>`_ - Comprehensive implementation guide and API documentation

**Resources and Examples:**

- `ESP-TEE Examples Repository <https://github.com/espressif/esp-idf/tree/master/examples/security/tee>`_ - Code examples and tutorials
- `Announcing ESP-TEE Framework for ESP32-C6 <https://developer.espressif.com/blog/2025/02/announcing-esp-tee/>`_ - Official announcement and overview

**Security Guides:**

- `ESP-IDF Security Overview <https://docs.espressif.com/projects/esp-idf/en/latest/esp32c6/security/security.html>`_ - Complete security feature guide
- :ref:`security_features` - Detailed security feature matrix and capabilities

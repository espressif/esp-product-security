.. _security_certifications:

Security Certifications
=======================

Espressif Systems is committed to delivering secure-by-design solutions for the Internet of Things (IoT). As part of this commitment, we pursue and maintain multiple security certifications across our product portfolio spanning both Xtensa and RISC-V architectures. These certifications validate the robustness of our platform security and assure customers that Espressif SoCs meet recognized industry security standards.

This section highlights the key security certifications achieved across Espressif SoCs and Products:

.. list-table:: Espressif Security Certifications Summary
   :header-rows: 1
   :widths: 20 10 15 15 15 15

   * - SoC/Product
     - Architecture
     - PSA Level 1
     - PSA Level 2
     - CLS-Ready
     - CSA Verified Mark
   * - ESP32-C3 Series (includes ESP-Zerocode Light Bulb)
     - RISC-V
     - ✓
     -
     - ✓
     - ✓
   * - ESP32-S3 Series
     - Xtensa
     - ✓
     -
     -
     -
   * - ESP32-H2 Series
     - RISC-V
     - ✓
     -
     -
     -
   * - ESP32-C6 Series
     - RISC-V
     -
     - ✓
     -
     -

Platform Security Certifications
--------------------------------

**PSA Certified Level 1**
~~~~~~~~~~~~~~~~~~~~~~~~~

*PSA Certified Level 1 (PSA-L1) is an industry-recognized certification that demonstrates a platform's adherence to best security practices and the implementation of essential security features. It assures that the platform includes critical security mechanisms such as secure boot, software update, secure storage, and cryptographic services.*

The following Espressif SoCs have achieved **PSA Certified Level 1 (PSA-L1)** certification:

- `ESP32-H2 Series <https://products.psacertified.org/products/esp32-h2-series>`_
- `ESP32-C3 Series <https://products.psacertified.org/products/esp32-c3-series>`_
- `ESP32-S3 Series <https://products.psacertified.org/products/esp32-s3-series-esp32-s3-esp32-s3fn8-esp32-s3r2-esp32-s3r8-esp32-s3r8v-esp32-s3fh4r2>`_

**PSA Certified Level 2**
~~~~~~~~~~~~~~~~~~~~~~~~~

*PSA Certified Level 2 (PSA-L2) provides advanced assurance by validating a platform's resistance to scalable software attacks and the robustness of its secure execution environment. This level involves independent evaluation of runtime security features and isolation boundaries.*

The following Espressif SoCs have achieved **PSA Certified Level 2 (PSA-L2)** certification:

- `ESP32-C6 Series <https://products.psacertified.org/products/esp32-c6>`_ - **World's first PSA-L2 Certified RISC-V MCU**

**CLS-Ready Certification**
~~~~~~~~~~~~~~~~~~~~~~~~~~~

*CLS-Ready certification, issued by the Cyber Security Agency of Singapore (CSA), confirms that a platform meets the security component evaluation criteria of the CLS-Ready framework. This certification streamlines the process for downstream product certifications and demonstrates compliance with regional security standards.*

The following Espressif SoCs have achieved **CLS-Ready** certification:

- `ESP32-C3 Series (CLS Ready) <https://www.csa.gov.sg/our-programmes/certification-and-labelling-schemes/cls-ready/platform-list/>`_

**CSA PSWG Verified Mark**
~~~~~~~~~~~~~~~~~~~~~~~~~~

*The CSA Product Security Working Group (PSWG) Verified Mark is awarded to products that have been evaluated against the CSA PSWG's global IoT security baseline. This mark indicates adherence to best practices in IoT security and provides assurance to customers regarding the product's security posture.*

The following Espressif product has received the **CSA PSWG Verified Mark**:

- `ESP-Zerocode Light Bulb (based on ESP32-C3) <https://verified.csa-iot.org/fkk-q3mk/>`_

RED-DA Compliance Support
-------------------------

**EU Radio Equipment Directive Delegated Act (RED-DA)**

*The EU RED Delegated Act establishes mandatory cybersecurity requirements for radio equipment sold in the EU market, with compliance required by August 1, 2025. Espressif provides comprehensive support to help manufacturers achieve RED-DA compliance through platform security features and streamlined documentation processes.*

**Key Compliance Requirements:**

- **Network Connection Protection**: Secure communication protocols and access controls
- **Personal Data Privacy**: Data protection mechanisms and privacy safeguards  
- **Financial Fraud Prevention**: Authentication and authorization security measures

**Espressif RED-DA Support:**

- **Pre-Certified Firmware Platforms**: ESP-AT, ESP-ZeroCode, and AWS IoT ExpressLink with built-in compliance features
- **Three Compliance Pathways**: Self-declaration using Espressif templates, consultancy-assisted assessment, or full conformity assessment via approved testing labs
- **Documentation Templates**: Ready-to-use risk assessment and technical specification templates
- **Partner Ecosystem**: Collaboration with Brightsight and CyberWhiz for end-to-end compliance support
- **Hardware Security Foundation**: Secure boot, flash encryption, and cryptographic accelerators aligned with EN 18031 standards

**Implementation Resources:**

- `ESP32 RED-DA EN18031 Compliance Guide (Part 1) <https://developer.espressif.com/blog/2025/04/esp32-red-da-en18031-compliance-guide/>`_ - Compliance overview and manufacturer responsibilities
- `ESP32 RED-DA EN18031 Compliance Guide (Part 2) <https://developer.espressif.com/blog/2025/07/esp32-red-da-en18031-compliance-guide-part2/>`_ - Practical compliance strategies and partner support
- `Espressif + Brightsight RED-DA Webinar <https://www.youtube.com/watch?v=j-qSfqoy_Wg>`_ - Preparing for RED DA (EN 18031) Compliance

.. note::

   Certification details are subject to updates. Please contact Espressif support channel for the most recent status.

Related Resources
-----------------

- `PSA Certification <https://www.psacertified.org>`_ — Official site for PSA Certified, including certification details and product listings.
- `CLS-Ready  <https://www.csa.gov.sg/our-programmes/certification-and-labelling-schemes/cls-ready/about>`_ — Information about the CLS-Ready framework by the Cyber Security Agency of Singapore.
- `CSA Product Security Certification <https://csa-iot.org/newsroom/the-connectivity-standards-alliance-product-security-working-group-launches-the-iot-device-security-specification-1-0/>`_ — Details on the CSA Product Security Working Group and IoT device security specification.

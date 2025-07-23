.. _security_response:

Security Response Process
=========================

Espressif is committed to the security of its products and software solutions. The company follows a well-defined `Security Incident Response Process (PDF) <https://www.espressif.com/sites/default/files/Espressif%20Security%20Incident%20Response%20Process%20v1.0_EN.pdf>`_ to address and mitigate security incidents in a timely and effective manner.

Key Components of the Security Response Process
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Vulnerability Reporting**

- Security vulnerabilities can be reported via Espressif's Bug Bounty Program, customer support, or internal discovery
- Reports should include as much detail as possible including affected SoC families (Xtensa or RISC-V based)
- For sensitive information, reports should be encrypted using Espressif's PGP/GPG key

**Evaluation and Assessment**

- Espressif evaluates the report and assigns priority based on severity
- Technical analysis is performed to validate and assess the impact across affected platforms
- Security team determines if the vulnerability affects hardware features, ESP-IDF software, or both

**Corrective Actions**

- If a vulnerability is confirmed, Espressif develops and deploys fixes or mitigations
- Communication is maintained with the reporter throughout the process
- CVE registration is performed when appropriate for public vulnerabilities

**Public Disclosure**

- After remediation, Espressif publishes a public advisory with details of the issue, impact, and remediation steps
- Advisories are available on the `Espressif Advisories page <https://www.espressif.com/en/support/documents/advisories>`_

.. note::
   ESP-IDF platform software specific advisories are listed at https://github.com/espressif/esp-idf/security/advisories

Coordinated Disclosure Policy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Espressif encourages coordinated vulnerability disclosure and maintains strict confidentiality during the investigation and remediation process. Public disclosure is made only after a fix is available, and Espressif notifies affected customers as needed.

For more details, please see:

- `Espressif Security Incident Response Process (PDF) <https://www.espressif.com/sites/default/files/Espressif%20Security%20Incident%20Response%20Process%20v1.0_EN.pdf>`_
- `Espressif Security Advisories <https://www.espressif.com/en/support/documents/advisories>`_
- `ESP-IDF Security Advisories <https://github.com/espressif/esp-idf/security/advisories>`_

ESP-IDF Security Support Policy
-------------------------------

**Support Timeline**

Each ESP-IDF major and minor release version receives security fixes for 30 months after its initial stable release date. After this support period, the release is considered End of Life (EOL) and no longer receives security updates.

**Platform Coverage**

Security updates cover all supported Espressif SoC architectures:
- **Xtensa-based platforms:** ESP32, ESP32-S2, ESP32-S3
- **RISC-V-based platforms:** ESP32-C2, ESP32-C3, ESP32-C5, ESP32-C6, ESP32-C61, ESP32-H2, ESP32-P4

**Recommendation**

Users are strongly encouraged to upgrade to a supported ESP-IDF release to ensure continued receipt of security fixes and access to the latest security features like ESP-TEE on RISC-V platforms.

For more details, see the `ESP-IDF Support Periods documentation <https://docs.espressif.com/projects/esp-idf/en/latest/esp32/versions.html#support-periods>`_.


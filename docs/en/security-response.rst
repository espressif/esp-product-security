Security Response Process
=========================

Espressif is committed to the security of its products and software solutions. The company follows a well-defined `Security Incident Response Process (PDF) <https://www.espressif.com/sites/default/files/Espressif%20Security%20Incident%20Response%20Process%20v1.0_EN.pdf>`_ to address and mitigate security incidents in a timely and effective manner.

**Key points from the process:**
- **Reporting:** Security vulnerabilities can be reported via Espressif's Bug Bounty Program, customer support, or internal discovery. Reports should include as much detail as possible and, for sensitive information, should be encrypted using Espressif's PGP/GPG key.
- **Evaluation:** Espressif evaluates the report, assigns priority, and performs technical analysis to validate and assess the impact.
- **Corrective Actions:** If a vulnerability is confirmed, Espressif develops and deploys fixes or mitigations, communicates with the reporter, and may register a CVE if appropriate.
- **Public Disclosure:** After remediation, Espressif publishes a public advisory, including details of the issue, impact, and remediation steps. Advisories are available on the `Espressif Advisories page <https://www.espressif.com/en/support/documents/advisories>`_

  .. note::
     ESP-IDF platform software specific advisories are listed at https://github.com/espressif/esp-idf/security/advisories

**Disclosure Policy:**
Espressif encourages coordinated vulnerability disclosure and maintains strict confidentiality during the investigation and remediation process. Public disclosure is made only after a fix is available, and Espressif notifies affected customers as needed.

For more details, see:
- `Espressif Security Incident Response Process (PDF) <https://www.espressif.com/sites/default/files/Espressif%20Security%20Incident%20Response%20Process%20v1.0_EN.pdf>`_
- `Espressif Security Advisories <https://www.espressif.com/en/support/documents/advisories>`_
- `ESP-IDF Security Advisories <https://github.com/espressif/esp-idf/security/advisories>`_

ESP-IDF Security Fixes Policy
=============================

Each ESP-IDF major and minor release version receives security fixes for 30 months after its initial stable release date. After this support period, the release is considered End of Life (EOL) and no longer receives security updates. Users are strongly encouraged to upgrade to a supported ESP-IDF release to ensure continued receipt of security fixes.

For more details, see the [ESP-IDF Support Periods documentation](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/versions.html#support-periods).


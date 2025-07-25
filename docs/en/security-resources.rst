Security Resources
==================

ESP-IDF Security Dashboard
--------------------------

The `ESP-IDF Security Dashboard <https://espressif.github.io/esp-idf-security-dashboard/>`_ is a public vulnerability database that provides comprehensive tracking of security issues across ESP-IDF versions. This essential tool helps developers and manufacturers maintain secure firmware throughout their product lifecycle.

**Key Features:**

- **CVE Mapping**: Maps all known CVEs to their impacted ESP-IDF versions
- **Version Tracking**: Quickly identifies affected releases and patched versions  
- **Risk Assessment**: Enables periodic firmware audits for ongoing compliance
- **Compliance Support**: Essential for regulatory requirements under CRA, RED-DA and similar frameworks

**Usage Recommendations:**

- **Pre-Launch**: Verify firmware against known vulnerabilities before shipping
- **Post-Launch**: Periodically scan firmware versions against the latest dashboard data
- **Update Planning**: Use dashboard information to prioritize security updates and OTA deployments
- **Compliance Documentation**: Reference dashboard findings in regulatory audit documentation

The security dashboard is integrated with ESP-IDF's long-term support policy, ensuring that critical security fixes are tracked and delivered through LTS branches for at least 30 months.

ESP-IDF Security Vulnerabilities Summary
----------------------------------------

.. list-table:: ESP-IDF Security Vulnerabilities
   :header-rows: 1
   :widths: 20 20 25 25

   * - CVE Number
     - Espressif Advisory
     - Impact
     - Advisory Pointer
   * - CVE-2025-52471
     - NA (Published on GitHub)
     - Applicable for ESP-IDF
     - `GHSA-hqhh-cp47-fv5g <https://github.com/espressif/esp-idf/security/advisories/GHSA-hqhh-cp47-fv5g>`_
   * - CVE-2024-53845
     - NA (Published on GitHub)
     - Applicable for ESP-IDF
     - `GHSA-wm57-466g-mhrr <https://github.com/espressif/esp-idf/security/advisories/GHSA-wm57-466g-mhrr>`_
   * - CVE-2024-30949
     - NA
     - ESP-IDF does not use system call implementations from Newlib
     - NA
   * - CVE-2024-28183
     - NA (Published on GitHub)
     - Applicable for ESP-IDF
     - `GHSA-22x6-3756-pfp8 <https://github.com/espressif/esp-idf/security/advisories/GHSA-22x6-3756-pfp8>`_
   * - CVE-2023-35818
     - AR2023-005
     - ESP32 Chip Revision v3.0/v3.1
     - `AR2023-005 <https://www.espressif.com/sites/default/files/advisory_downloads/AR2023-005%20Security%20Advisory%20Concerning%20Bypassing%20Secure%20Boot%20and%20Flash%20Encryption%20Using%20EMFI%20EN.pdf>`_
   * - CVE-2023-24023
     - AR2023-010
     - Applicable for ESP-IDF
     - `AR2023-010 <https://www.espressif.com/sites/default/files/advisory_downloads/AR2023-010%20Security%20Advisory%20Concerning%20the%20Bluetooth%20BLUFFS%20Vulnerability%20EN.pdf>`_
   * - CVE-2023-52160
     - AR2024-003
     - Applicable for ESP-IDF
     - `AR2024-003 <https://www.espressif.com/sites/default/files/advisory_downloads/AR2024-003%20Security%20Advisory%20for%20PEAP%20Phase-2%20authentication%20EN.pdf>`_
   * - CVE-2022-24893
     - NA (Published on GitHub)
     - Applicable for ESP-IDF
     - `GHSA-7f7f-jj2q-28wm <https://github.com/espressif/esp-idf/security/advisories/GHSA-7f7f-jj2q-28wm>`_
   * - CVE-2021-32020
     - NA
     - ESP-IDF uses its own heap allocator; not applicable
     - NA
   * - CVE-2021-43997
     - NA
     - Not applicable for Espressif chips
     - NA
   * - CVE-2021-3420
     - AR2021-005
     - Not applicable for ESP-IDF
     - NA
   * - CVE-2021-31571
     - AR2021-005
     - Applicable for ESP-IDF
     - `AR2021-005 <https://www.espressif.com/sites/default/files/advisory_downloads/AR2021-005%20Security%20Advisory%20on%20BadAlloc%20Vulnerabilities.pdf>`_
   * - CVE-2021-31572
     - AR2021-005
     - Applicable for ESP-IDF
     - `AR2021-005 <https://www.espressif.com/sites/default/files/advisory_downloads/AR2021-005%20Security%20Advisory%20on%20BadAlloc%20Vulnerabilities.pdf>`_
   * - CVE-2021-28139
     - AR2021-004
     - Applicable for ESP-IDF
     - `AR2021-004 <https://www.espressif.com/sites/default/files/advisory_downloads/AR2021-004%20Bluetooth%20Security%20Advisory.pdf>`_
   * - CVE-2020-22283
     - NA
     - Applicable for ESP-IDF
     - Fix in ESP-IDF >= v4.4.1
   * - CVE-2020-22284
     - NA
     - Applicable for ESP-IDF
     - Fix in ESP-IDF >= v4.4.1
   * - CVE-2020-26142
     - AR2023-008
     - Applicable for ESP-IDF
     - `AR2023-008 <https://www.espressif.com/sites/default/files/advisory_downloads/AR2023-008%20Security%20Advisory%20Concerning%20FragAttacks%20EN.pdf>`_
   * - CVE-2020-12638
     - AR2020-002
     - Applicable for ESP-IDF
     - `AR2020-002 <https://www.espressif.com/sites/default/files/advisory_downloads/AR2020-002%20Security%20Advisory%20Concerning%20Wi-Fi%20Authentication%20Bypass%20V1.1%20EN.pdf>`_

Additional Resources
--------------------

**Security Blog & Updates**

Visit the `Espressif Security Blog <https://developer.espressif.com/tags/security/>`_ for implementation guides, compliance updates, technical deep dives, and the latest security insights for Espressif platforms.


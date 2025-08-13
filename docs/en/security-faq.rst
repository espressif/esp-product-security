Security FAQ
============

This section addresses frequently asked questions about Espressif product security features, certifications, and best practices.

General Security
-----------------

**Q: What security features are available across Espressif products?**

A: Espressif products offer comprehensive security features including hardware-based root of trust, secure boot, flash encryption, secure storage, crypto acceleration, and trusted execution environments. For a complete overview, see :doc:`security-features`.

**Q: Which Espressif products have received security certifications?**

A: Many Espressif products have achieved PSA Certified, CLS-Ready status, and CSA verification marks. Check the :doc:`security-certifications` page for specific product certifications and compliance details.

**Q: How do I implement security-by-design in my product development?**

A: Follow our security implementation workflow that includes threat modeling, secure architecture design, security testing, and vulnerability management. Detailed guidance is available in :doc:`security-implementation`.

Secure Boot & Flash Encryption
-------------------------------

**Q: What is secure boot and why should I use it?**

A: Secure boot ensures only authenticated firmware can run on the device by cryptographically verifying the bootloader and application signatures. This prevents unauthorized code execution and firmware tampering.

**Q: How does flash encryption protect my firmware?**

A: Flash encryption encrypts the firmware stored in external flash memory using hardware-accelerated AES encryption. Even if an attacker gains physical access to the device, they cannot read the encrypted firmware without the encryption keys.

**Q: Can I use secure boot and flash encryption together?**

A: Yes, secure boot and flash encryption are complementary security features that should be used together for maximum protection. Secure boot verifies firmware authenticity while flash encryption protects firmware confidentiality.

**Q: What are the performance implications of enabling security features?**

A: Security features have minimal performance impact due to hardware acceleration. Secure boot adds a small delay during boot time for signature verification. Flash encryption uses dedicated hardware so runtime performance impact is negligible.

Cryptographic Features
-----------------------

**Q: What cryptographic algorithms are supported?**

A: Espressif products support industry-standard cryptographic algorithms including AES-128/256, RSA, ECC (ECDSA, ECDH), SHA-256, and hardware random number generation. Many operations are hardware-accelerated for optimal performance.

**Q: How do I securely store cryptographic keys?**

A: Use eFuse blocks or secure storage APIs for key storage. Keys stored in eFuses are write-protected and can be read-protected. For application keys, use the secure storage partition with encryption and authentication.

**Q: Does Espressif provide crypto libraries?**

A: Yes, ESP-IDF includes mbedTLS crypto library with hardware acceleration support. Additional crypto APIs are available for direct hardware crypto accelerator access.

Trusted Execution Environment (TEE)
------------------------------------

**Q: What is ESP-TEE and when should I use it?**

A: ESP-TEE provides a trusted execution environment with hardware-enforced isolation between secure and non-secure worlds. Use ESP-TEE when you need to protect sensitive code, keys, or data processing from the main application. Learn more at :doc:`security-frameworks`.

**Q: What can run in the secure world of ESP-TEE?**

A: The secure world can run trusted applications (TAs) for key management, secure communications, biometric processing, payment operations, and other security-critical functions that require isolation from the main OS.

**Q: Is ESP-TEE compatible with existing applications?**

A: ESP-TEE is designed for easy integration. Existing applications can call secure world functions through a standardized API without major architectural changes.

Vulnerability Management
-------------------------

**Q: How does Espressif handle security vulnerabilities?**

A: Espressif follows a responsible disclosure process with coordinated vulnerability disclosure (CVD). We provide security advisories, CVE tracking, and timely patches. Details are available in :doc:`security-response`.

**Q: How can I report a security vulnerability?**

A: Report security vulnerabilities to our security team at security@espressif.com. We appreciate responsible disclosure and will work with you to address valid security issues.

**Q: Where can I find security advisories and CVE information?**

A: Security advisories and CVE information are available in our :doc:`security-resources` section, which includes links to our CVE database and vulnerability management resources.

**Q: How often should I update ESP-IDF for security patches?**

A: We recommend staying current with ESP-IDF releases and security patches. Subscribe to our security advisories to be notified of critical updates that may affect your products.

Compliance & Certifications
----------------------------

**Q: What is PSA Certified and why is it important?**

A: PSA Certified is a security certification scheme that validates IoT device security against industry standards. PSA Certified products meet rigorous security requirements for root of trust, secure storage, cryptography, and secure communications.

**Q: How do certifications help with my product compliance?**

A: Security certifications like PSA Certified can accelerate your product's compliance with industry standards and regulations, reduce certification costs, and provide assurance to customers and partners about your product's security posture.

**Q: Do I need additional certifications beyond what Espressif provides?**

A: Espressif's certifications cover the silicon and platform level. Depending on your market and application, you may need additional product-level certifications. Our certified platforms provide a strong foundation for your certification process.

Best Practices
---------------

**Q: What are the essential security practices for IoT products?**

A: Essential practices include enabling secure boot and flash encryption, implementing secure communications (TLS/SSL), regular security updates, proper key management, input validation, and following the principle of least privilege.

**Q: How do I secure communication between my device and cloud services?**

A: Use TLS/SSL with certificate validation for all communications. Implement proper certificate management, consider mutual authentication (mTLS), and ensure secure credential provisioning during manufacturing.

**Q: What should I consider for secure manufacturing and provisioning?**

A: Implement secure key provisioning, unique device identities, secure firmware installation, and proper test key removal. Consider using secure manufacturing services and Hardware Security Modules (HSMs) for key generation and management.
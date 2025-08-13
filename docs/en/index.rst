ESP Product Security
====================

This repository contains **Product Security** resources, documentation and guidelines to help build secure, certification compliant and robust end products using Espressif solutions.

.. raw:: html

    <style>
    .security-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 20px;
        margin: 30px 0;
    }
    .security-card {
        border: 1px solid #e1e4e8;
        border-radius: 8px;
        padding: 20px;
        text-align: center;
        background: #f8f9fa;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        text-decoration: none;
        color: inherit;
    }
    .security-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        text-decoration: none;
        color: inherit;
    }
    .security-icon {
        font-size: 48px;
        margin-bottom: 15px;
        display: block;
    }
    .security-title {
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 10px;
        color: #2c3e50;
    }
    .security-description {
        font-size: 14px;
        color: #6c757d;
        line-height: 1.4;
    }
    </style>

    <div class="security-grid">
        <a href="security-features.html" class="security-card">
            <div class="security-icon">🔒</div>
            <div class="security-title">Security Features</div>
            <div class="security-description">Comprehensive security matrix, platform protection and crypto capabilities</div>
        </a>
        
        <a href="security-certifications.html" class="security-card">
            <div class="security-icon">🏆</div>
            <div class="security-title">Certifications & Compliance</div>
            <div class="security-description">PSA Certified, CLS-Ready, CSA verified marks and industry standards</div>
        </a>
        
        <a href="security-frameworks.html" class="security-card">
            <div class="security-icon">🛡️</div>
            <div class="security-title">Security Frameworks</div>
            <div class="security-description">ESP-TEE and trusted execution environments for hardware-enforced isolation</div>
        </a>
        
        <a href="security-implementation.html" class="security-card">
            <div class="security-icon">⚙️</div>
            <div class="security-title">Implementation Guide</div>
            <div class="security-description">Security-by-design workflow, threat modeling and testing frameworks</div>
        </a>
        
        <a href="security-response.html" class="security-card">
            <div class="security-icon">🚨</div>
            <div class="security-title">Security Response</div>
            <div class="security-description">Incident response process, vulnerability disclosure and security policy</div>
        </a>
        
        <a href="security-resources.html" class="security-card">
            <div class="security-icon">📚</div>
            <div class="security-title">Security Resources</div>
            <div class="security-description">CVE database, security advisories and vulnerability management</div>
        </a>
        
        <a href="security-faq.html" class="security-card">
            <div class="security-icon">❓</div>
            <div class="security-title">Security FAQ</div>
            <div class="security-description">Frequently asked questions about security features, certifications and best practices</div>
        </a>
        
        <a href="disclaimer-and-copyright.html" class="security-card">
            <div class="security-icon">⚖️</div>
            <div class="security-title">Legal & Disclaimer</div>
            <div class="security-description">Copyright notice, disclaimers and legal information</div>
        </a>
    </div>

.. toctree::
   :hidden:
   :maxdepth: 1

   security-features
   security-certifications
   security-frameworks
   security-implementation
   security-response
   security-resources
   security-faq
   disclaimer-and-copyright


Linux Server Security & Compliance Auditor
A lightweight, production-ready Python diagnostic tool designed for system administrators and developers to instantly perform security compliance audits on Ubuntu and Debian servers.

Features
File Permission Audit: Automatically scans critical system files (/etc/shadow, /etc/passwd, /etc/gshadow, /etc/crontab) against secure octal permission benchmarks.

Surgical Port Scanner: Inspects active network ports using strict pattern matching to eliminate false positives and detect obsolete unsecured protocols (FTP/Telnet).

Robust Exception Handling: Built-in granular error catching to prevent runtime crashes during permission denials.

How to Run
Note: Root privileges are strictly required to audit sensitive system files.

sudo python3 medico.py

Upgrade to the Full Security & Hardening Pack
Need automated protection and active defense? Get the CyberScaffolding Full Security Pack, which includes:

armatura.py (Active Hardening Core): Installs and configures UFW Firewall (handling ports 80 and 443), deploys Fail2Ban for active brute-force protection, isolates SSH to port 2222, and features a built-in auto-rollback safety net to prevent accidental server lockouts.

sentinella.py (Log Threat Parser): Lightweight real-time Nginx/Apache access log monitor that detects WordPress scans, SQL Injections, and Directory Traversal attempts, generating exact automated commands to instantly ban hostile IPs.

Comprehensive Documentation: Full deployment and troubleshooting guide in both English and Italiano.
 
Click here to get the Full Security Pack on Gumroad: https://cyberscaffolding.gumroad.com/l/fseih
License
Provided "as-is" for educational and administrative compliance auditing.

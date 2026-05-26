# Linux Server Security & Compliance Auditor 🛡️

A lightweight, production-ready Python diagnostic tool designed for system administrators and developers to instantly perform security compliance audits on Ubuntu and Debian servers.

## Features
* **File Permission Audit:** Automatically scans critical system files (`/etc/shadow`, `/etc/passwd`, `/etc/gshadow`, `/etc/crontab`) against secure octal permission benchmarks.
* **Surgical Port Scanner:** Inspects active network ports using strict pattern matching (`:21 `, `:23 `) to eliminate false positives and detect obsolete unsecured protocols (FTP/Telnet).
* **Robust Exception Handling:** Built-in granular error catching to prevent runtime crashes during permission denials.

## How to Run

> ⚠️ **Note:** Root privileges are strictly required to audit sensitive system files.

```bash
sudo python3 medico.py

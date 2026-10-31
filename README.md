# devsecops-pipeline-demo

# Automated DevSecOps CI/CD Pipeline

## Overview
This repo demonstrates an automated DevSecOps pipeline utilising GitHub Actions. The idea is to shift security left by blocking insecure code and exposed credentials from reaching production environments.

## Automated Security Gates
*   **Static Application Security Testing (SAST):** Integrated **Semgrep** to structurally analyse Python source code. The scanner is configured to detect OWASP Top 10 vulnerabilities, specifically flagging dangerous sinks (e.g., `os.system`, `pickle.loads`).
*   **Secret Scanning:** Integrated **TruffleHog** to deeply scan commit history for hardcoded high-entropy secrets (AWS Keys, JWTs, API tokens), failing the build if verified credentials are found.

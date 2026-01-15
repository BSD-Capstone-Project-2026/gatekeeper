# gatekeeper
## Team Members

| Name | GitHub Handle | Seneca Email | Role |
|-----|--------------|--------------|------|
| Navish | @navish-username | navish@myseneca.ca | Back-End Developer |
| Gurjeet Singh Sodhi | @gurjeet-username | gurjeet@myseneca.ca | Front-End Developer |
| Minhaz Abedin | @minhaz-username | minhaz@myseneca.ca | Product Manager |
| Rohith Haridas | @rohith-username | rohith@myseneca.ca | Database Specialist |

## Project Overview

This capstone project focuses on designing and developing a secure, local-first residential access management system that replaces traditional physical keys and fobs with encrypted virtual keys stored on residents’ devices.

The system operates entirely within a building’s internal network without reliance on external cloud services. Access is granted only when strict security conditions are met, including proximity validation and connection to a secured local network.

### Key Features
- Encrypted virtual key generation
- Proximity-based access validation (Wi-Fi + location presence)
- Role-based access control (Resident, Concierge, Management)
- Emergency override with full audit logging
- Centralized access logs for traceability
- Autonomous alerts for suspicious access attempts
- Concierge and management dashboard


## Technology Stack (Preliminary)

- Front-End:
  - Web dashboard (React or similar)
  - Mobile interface (Android or cross-platform)

- Back-End:
  - Local server (Node.js / Python / Java – TBD)
  - RESTful API
  - Role-based authentication

- Database:
  - Local relational database (PostgreSQL / SQLite)
  - Encrypted storage for sensitive data

- Security:
  - Encryption for virtual keys
  - Secure authentication and authorization
  - Audit logging

- DevOps / Tools:
  - GitHub for version control
  - GitHub Projects for backlog management

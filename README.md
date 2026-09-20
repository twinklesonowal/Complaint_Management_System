# IT Service Desk & Complaint Management System, NHPC

A centralized, web-based complaint and IT asset management system built for the Information Technology & Communication Department at **Subansiri Lower Hydroelectric Project (SLHEP), NHPC Limited**. The system replaces manual complaint handling with a role-based digital workflow for Employees, IT Staff, and IT Managers.

## Overview

The IT Department at NHPC previously handled employee complaints manually, which made it difficult to maintain records, track status, and monitor pending requests. This application centralizes that process — allowing employees to raise and track IT complaints, IT staff to manage and resolve service tickets, and managers to oversee operations, users, and IT assets from a single dashboard.

## Features

- **Role-based dashboards** for Employees, IT Staff, and IT Managers
- **Complaint/ticket management** — raise complaints, assign, update status, add resolution notes
- **Unique ticket referencing** (e.g. `NHPC-00007`) for tracking every complaint
- **User management** — add, edit, and manage system users (Manager access)
- **Asset Management module** — maintain an inventory of IT assets (asset code, category, brand, location, status)
- **Excel import** for bulk-loading asset records using Pandas/OpenPyXL
- **Secure authentication** with session-based, role-restricted access
- Clean, responsive UI built with Bootstrap

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| Database | MySQL |
| ORM | SQLAlchemy |
| Frontend | HTML5, CSS3, Bootstrap 5, Jinja2 |
| Data Import | Pandas, OpenPyXL |
| Version Control | Git & GitHub |

## User Roles

- **Employee** — Raise complaints and track their status/history
- **IT Staff** — View, assign, and resolve assigned complaints; add resolution notes
- **IT Manager** — Monitor all complaints, manage users, and maintain IT asset records

## System Architecture

```
Employee / IT Staff / IT Manager
              │
      Flask Web Application
              │
 ┌────────────┼─────────────┬───────────────┐
 │            │              │               │
Auth    Complaint Mgmt   Asset Mgmt     User Mgmt
Module     Module          Module         Module
 │            │              │               │
 └────────────┴──────────────┴───────────────┘
              │
        MySQL Database
      (Users, Tickets, Assets)
```

## Core Modules

- `Authentication Module` — login and role-based session handling
- `Complaint Management Module` — complaint creation, assignment, status tracking, resolution
- `Asset Management Module` — asset inventory, search, and Excel-based bulk import
- `User Management Module` — user creation, editing, and role assignment

## Database Entities

- **User** — id, full_name, username, password, role, department, email, status
- **Service Ticket** — ticket_number, employee_name, department, category, priority, problem, status, assigned_to, resolution_notes, created_at, closed_at
- **Asset** — asset_code, asset_name, category, brand, location, assigned_to, status

## Project Background

This project was developed during a one-month internship (July 2026) in the IT & Communication Department at NHPC Limited, Subansiri Lower Hydroelectric Project, under the guidance of the department's IT team, as part of a Bachelor of Computer Applications program.

## Author

**Twinkle Sonowal**
Developed as part of an internship project at NHPC Limited (SLHEP).

---
*This project is intended for internal organizational use.*

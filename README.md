# Blood Bank Management System

Django web app connecting blood donors with receivers in Nepal.

## What It Does

* Donors register and donate blood
* Receivers request blood by type
* Hospitals manage inventory
* Users can be both donor AND receiver
* Role-based dashboards and access control
* Profile management with password change

## Current Status

**Completed:**

* Project setup with 5 apps (accounts, donor, receiver, hospital, core)
* Custom user model (email/phone login)
* UI templates with Bootstrap 5
* URL routing with namespacing
* Database setup and migrations
* User registration (auto-login after signup)
* Authentication (login/logout)
* Role-based access control (custom decorators for donor/receiver/hospital)
* Profile management (view, edit, add roles, change password)
* Donor features:
  * Donation model
  * Record donation form
  * Donation history
  * Live dashboard stats (total donations, next eligible date, lives saved)
* Receiver features:
  * Blood request model
  * Create blood request form
  * Request history
  * Live dashboard stats (total, pending, fulfilled, rejected requests)

**In Progress:**

* Hospital features (blood inventory management)
* Admin dashboard (approve/reject requests, system statistics)

## Key Features

**Custom User Model:**

* Login with email OR phone
* Blood type, age, address
* Dual roles (donor + receiver), with hospital role requiring admin approval

**Authorization:**

* Custom decorators (`@donor_required`, `@receiver_required`, `@hospital_required`)
* Users restricted to their own role's dashboard

**Nepal-Specific:**

* Nepal phone validation (98X, 97X, 96X)
* Addresses for Kathmandu valley

## Tech Stack

* Django (backend)
* SQLite (database)
* Bootstrap 5 (frontend)
* Custom authentication backend (email/phone login)

## Author

Mitrata Bhandari
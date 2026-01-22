# n8n Workflow: WordPress Role Sync

## Overview

This n8n workflow automatically synchronizes WordPress user roles with student status data from Google Sheets.

## Workflow File

- **File:** `sheets > panel.idemab.com.json`
- **Purpose:** Sync student roles from Google Sheets to WordPress

## Configuration

### Google Sheets
- **Document:** IDEMAB - Alumnos (activos/inactivos)
- **Sheet:** panel.idemab.com
- **URL:** https://docs.google.com/spreadsheets/d/1SISJlMo40LnZ8DGux2nlnbnS52T_1ABg8cmUQoj8qHg/edit?usp=sharing

### WordPress
- **Site:** https://panel.idemab.com/
- **API:** WordPress REST API v2

### Role Logic
- **Active Students (Status = "activo"):** Assigned role from "Rol" column
- **Inactive Students (Status = "inactivo"):** Assigned "sinpago" role

## How It Works

1. **Schedule Trigger** runs every minute (configurable)
2. **Read Student Status** fetches all rows from Google Sheet
3. **Loop Rows** processes each student individually
4. **Find WP User by Email** searches for WordPress user
5. **User Found?** checks if user exists
6. **Check Status** determines if student is active or inactive
7. **Update Role** assigns appropriate WordPress role
8. **Continue Loop** moves to next student

## Import Instructions

1. Open n8n
2. Go to **Workflows** → **Import from File**
3. Select `sheets > panel.idemab.com.json`
4. Verify credentials are connected:
   - Google Sheets OAuth2: `diseno4.impulsomarketing@gmail.com`
   - WordPress API: `https://panel.idemab.com/`
5. Test with manual execution
6. Activate workflow

## Features

✅ Processes all students without stopping  
✅ Handles missing users gracefully  
✅ Automatic role updates based on status  
✅ Scheduled execution (every minute by default)

## Version

- **Created:** 2026-01-21
- **n8n Version:** Compatible with v1.121.3+

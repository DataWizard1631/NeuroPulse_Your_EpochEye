# NeuroPulse

> Your EpochEye
> **Real-time telemetry for every pulse of your machine learning.**

[![Status](https://img.shields.io/badge/status-building-yellow.svg)](#)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Docker](https://img.shields.io/badge/docker-ready-blue.svg)](#)
[![Made with FastAPI](https://img.shields.io/badge/backend-FastAPI-green)](#)
[![Frontend](https://img.shields.io/badge/frontend-Next.js-black)](#)

---

## Overview

**NeuroPulse** is a plug-and-play, multi-tenant ML monitoring SaaS that enables you to track model training metrics (loss, accuracy, gradients, etc.) in real-time. It's built for ML practitioners who want actionable, live insights during model training—without writing custom dashboards or metrics pipelines.

---

## Features

-  **Lightweight REST API** to ingest metrics (loss, accuracy, LR, gradients, etc.)
-  **Live-updating dashboard** (Next.js) per project and user
-  **Python SDK** – `pip install neuropulse` and log in 2 lines
-  **Multi-tenant isolation** via API keys and project IDs
-  **Scalable, containerized**: FastAPI + PostgreSQL (Timescale) + Docker
-  Real-time line charts, heatmaps, and trend analytics
-  Alerts (coming soon) for plateauing, anomalies, early stopping triggers

---

## Tech Stack

| Layer       | Tech                  |
|-------------|-----------------------|
| Frontend    | Next.js (Tailwind + Recharts) |
| Backend API | FastAPI (Python)      |
| Database    | PostgreSQL + TimescaleDB |
| SDK         | Python                |
| Infra       | Docker, Docker Compose |
| Security    | API key auth + rate limiting |

## License
This project is licensed under the MIT License – see the LICENSE file for details.

## Maintainers
Developed and maintained by [Deep Patel](https://www.linkedin.com/in/deeppateldw1611/).



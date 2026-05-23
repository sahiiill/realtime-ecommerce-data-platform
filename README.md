# Real-Time E-Commerce Data Platform

Production-style real-time data engineering platform built using Kafka, Spark Structured Streaming, Airflow, dbt, Snowflake, and AWS.

## Project Goal

This project simulates a modern e-commerce analytics platform that ingests real-time user events, processes streaming data, stores raw and transformed datasets, and powers analytical reporting pipelines.

The platform demonstrates production-level data engineering practices including:

- Real-time event streaming
- Distributed data processing
- Workflow orchestration
- Data lake architecture
- Warehouse modeling
- Data quality validation
- Monitoring and observability
- Containerized infrastructure
- Cloud-ready deployment

---

## Architecture

```text
Event Producer
    ↓
Kafka / Redpanda
    ↓
Spark Structured Streaming
    ↓
Raw Storage (S3 / MinIO)
    ↓
dbt Transformations
    ↓
Snowflake Warehouse
    ↓
Analytics Dashboard

## Status

Project initialization in progress.

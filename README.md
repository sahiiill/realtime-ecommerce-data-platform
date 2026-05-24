# 🚀 Real-Time E-Commerce Data Platform

A real-time streaming data engineering platform built using **Kafka, Airflow, Docker, Python, and Streamlit**.

This project simulates an e-commerce analytics pipeline that ingests streaming events, validates schemas, processes ETL transformations, orchestrates workflows with Airflow, and visualizes analytics through an interactive dashboard.

---

# 📌 Architecture

```text
Producer
   ↓
Kafka Topic
   ↓
Consumer
   ↓
Raw Storage Layer
   ↓
Airflow DAG
   ↓
Transformation Pipeline
   ↓
Processed Storage Layer
   ↓
Streamlit Dashboard
```

---

# ✨ Features

## ⚡ Real-Time Streaming
- Kafka-based event streaming pipeline
- Simulated e-commerce activity events
- Producer/Consumer architecture

## ✅ Data Validation
- JSON schema validation
- Invalid event handling
- Failed event storage

## 🔄 ETL Processing
- Raw → Processed transformation pipeline
- Revenue calculations
- Structured processed storage layer

## 🛠 Workflow Orchestration
- Airflow DAG scheduling
- Automated ETL execution
- Monitoring workflows

## 📊 Dashboard Analytics
- Revenue KPIs
- Product analytics
- Country analytics
- Device analytics
- Interactive Plotly visualizations

## 🐳 Infrastructure
- Dockerized services
- Kafka + Zookeeper containers
- Persistent Airflow orchestration setup

---

# 🧰 Tech Stack

| Category | Technologies |
|---|---|
| Streaming | Apache Kafka |
| Orchestration | Apache Airflow |
| Backend | Python |
| Infrastructure | Docker |
| Dashboard | Streamlit, Plotly |
| Validation | JSONSchema |
| Testing | Pytest |
| Storage | JSONL Files |

---

# 📂 Project Structure

```text
realtime-ecommerce-data-platform/
│
├── airflow/
│   ├── dags/
│   ├── logs/
│   └── plugins/
│
├── dashboard/
│   └── app.py
│
├── scripts/
│   ├── run_consumer.ps1
│   ├── run_producer.ps1
│   └── run_tests.ps1
│
├── storage/
│   ├── raw/
│   ├── processed/
│   └── failed/
│
├── streaming/
│   ├── consumer.py
│   ├── producer.py
│   ├── transform.py
│   ├── schema.py
│   ├── logger.py
│   └── config.py
│
├── tests/
│   └── test_schema.py
│
├── docker-compose.yml
├── requirements.txt
├── pytest.ini
└── README.md
```

---

# ⚙️ Setup Instructions

## 1️⃣ Clone Repository

```bash
git clone <YOUR_GITHUB_REPO_URL>
cd realtime-ecommerce-data-platform
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Start Docker Services

```bash
docker compose up -d
```

---

## 5️⃣ Create Kafka Topic

```bash
docker exec -it kafka kafka-topics --create --topic ecommerce-events --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```

---

## 6️⃣ Start Producer

```bash
python -m streaming.producer
```

---

## 7️⃣ Start Consumer

Open another terminal:

```bash
python -m streaming.consumer
```

---

## 8️⃣ Start Streamlit Dashboard

```bash
streamlit run dashboard/app.py
```

Dashboard URL:

```text
http://localhost:8501
```

---

# 🌬 Airflow Setup

## Initialize Database

```bash
docker compose run airflow-webserver airflow db migrate
```

---

## Create Admin User

```bash
docker compose run airflow-webserver airflow users create --username admin --firstname admin --lastname admin --role Admin --email admin@example.com --password admin
```

---

## Access Airflow UI

```text
http://localhost:8080
```

Credentials:

```text
Username: admin
Password: admin
```

---

# 📸 Dashboard Preview

## Streamlit Dashboard

_Add dashboard screenshot here_

```markdown
![Dashboard](docs/dashboard.png)
```

---

## Airflow DAG Monitoring

_Add Airflow screenshot here_

```markdown
![Airflow](docs/airflow.png)
```

---

# 🧪 Testing

Run tests:

```bash
pytest
```

---

# 🔑 Key Engineering Concepts Demonstrated

- Real-time streaming pipelines
- Event-driven architecture
- Workflow orchestration
- ETL pipeline engineering
- Dockerized infrastructure
- Data validation pipelines
- Modular Python architecture
- Analytics dashboarding
- Monitoring workflows
- Fault handling strategies

---

# 🚀 Future Improvements

- PostgreSQL warehouse layer
- Incremental ETL processing
- Parquet-based storage
- Real-time dashboard refresh
- Kubernetes deployment
- CI/CD pipeline
- Cloud deployment
- Data quality monitoring
- Streaming analytics
- Redis caching layer

---

# 👨‍💻 Author

**Sahil Shaikh**  
Master’s Student — Web & Data Science  
University of Koblenz, Germany

---

# ⭐ If you found this project useful

Give it a star on GitHub ⭐

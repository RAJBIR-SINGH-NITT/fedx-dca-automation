# fedx-dca-automation
Automated debt collection decision engine using Python and n8n

 # FedEx DCA Automation – Python Decision Engine

This project is an automated decision system for managing overdue payment cases handled by Debt Collection Agencies (DCAs).

 # Project Overview 
- Python ingests raw overdue case data
- Data is cleaned and standardized
- Priority scores are calculated using business logic
- Each case is classified as High / Medium / Low priority
- The best DCA is recommended
- Output is used by n8n for automation

 # Technology Stack 
- Python (pandas, numpy)
- n8n (workflow automation)
- CSV data sources

 # Folder Structure 
fedx_dca/
├── src/decision_engine.py
├── data/
│   ├── overdue_cases.csv
│   └── dca_performance.csv
├── output/
│   └── python_output.csv

# How to Run the Python Engine 
python -c "from src.decision_engine import run_decision_engine; run_decision_engine()"

# Output 
The script generates:
output/python_output.csv

Containing:
- case_id
- priority_level
- recommended_dca

# Team Contribution 
- Python Decision Engine: Rajbir Singh
- Automation (n8n): Kaustubh
- Data & Dashboards: Ayan

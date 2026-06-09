# DataScienceService

Data Science service that extracts expense information from transaction messages using Large Language Models (LLMs) and automatically records them in an expense ledger through an event-driven architecture.

## Overview
The service receives transaction messages from users, processes them using LangChain and an LLM to extract structured expense information, and publishes the extracted data to Apache Kafka. The expense ledger service consumes these events and save into DataBase.

## Workflow

```text
┌─────────────┐
│  POST /API  │
│ Transaction │
│   Message   │
└──────┬──────┘
       │
       ▼
┌─────────────────┐
│  DS Service     │
│  (Python API)   │
└──────┬──────────┘
       │
       ▼
┌─────────────────┐
│   LangChain     │
│ Prompt Handling │
└──────┬──────────┘
       │
       ▼
┌─────────────────┐
│      LLM        │
│ Extracts:       │
│ • Merchant      │
│ • Amount        │
│ • Currency      │
└──────┬──────────┘
       │
       ▼
┌─────────────────┐
│  Apache Kafka   │
│ Expense Events  │
└──────┬──────────┘
       │
       ▼
┌─────────────────┐
│ Ledger Service  │
│ Stores Expenses │
└──────┬──────────┘
       │
       ▼
┌─────────────────┐
│ Expense Database│
└─────────────────┘
```

## Example

### Input

```text
Dear Customer, Rs. 1,250.00 spent on your HDFC Bank Credit Card ending 4589 at AMAZON PAY INDIA on 09-Jun-2026.
```

### Extracted Output

```json
{
  "merchant": "AMAZON PAY INDIA",
  "amount": 1250.00,
  "currency": "INR"
}
```

## Technology Stack

- Python
- Flask
- LangChain
- Mistral AI
- Apache Kafka
- Pydantic
# Cloud 101 with AWS – Serverless AI Workshop

This repository contains the code and resources used in the **Cloud 101 with AWS** workshop.
The goal is to help beginners understand cloud computing by building a real, serverless application.

## What we built

A simple web app where:
- The frontend is hosted on Amazon S3
- APIs are exposed via Amazon API Gateway
- Backend logic runs on AWS Lambda (Python)
- An AWS AI service is used for sentiment analysis

Architecture:
Browser -> S3 -> API Gateway -> Lambda -> AWS AI Service

![Architecture](architecture/architecture.png)

## Tech stack

- Amazon S3 (Static Website Hosting)
- Amazon API Gateway
- AWS Lambda (Python)
- AWS AI Service
- HTML, CSS, JavaScript

## Folder structure

cloud-101-aws-workshop/
│
├── frontend/
│   ├── index.html
│
├── lambda/
│   ├── quote_function/
│   │   └── lambda_function.py
│   └── sentiment_function/
│       └── lambda_function.py
│
├── architecture/
│   └── architecture.png
│
├── setup/
│   ├── api-gateway.md
│   ├── s3-setup.md
│   └── lambda-setup.md
│
└── README.md

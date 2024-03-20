#!/bin/bash

# Run any setup steps or pre-processing tasks here
echo "Starting UCL 2023-2024 RAG FastAPI service..."

# Start the main application
uvicorn main:app --host 0.0.0.0 --port 8000
#!/bin/bash

# Create Streamlit config directory and config file for deployment
mkdir -p ~/.streamlit/

echo "\
[server]
headless = true
port = \$PORT
enableCORS = false
" > ~/.streamlit/config.toml

# Install required Python packages
pip install -r requirements.txt

# Launch the Streamlit app
streamlit run app.py

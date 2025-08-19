#!/bin/bash

# Create Streamlit config directory and config file for deployment
mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
port = \$PORT\n\
enableCORS = false\n\
" > ~/.streamlit/config.toml

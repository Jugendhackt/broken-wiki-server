#!/bin/sh
# This script needs to be placed inside the server repo
# The frontend repo has to be placed in the same folder as the backend repo
source venv/bin/activate
gnome-terminal -- python3 scraper/server.py &
gnome-terminal -- python3 ../broken-wiki-frontend/start.py &

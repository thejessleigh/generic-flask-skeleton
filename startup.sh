#!/bin/bash

source venv/bin/activate
gunicorn -w 4 -b 0.0.0.0:5000 application_name.app:app


#!/bin/bash
gunicorn -b :5000 --access-logfile - --error-logfile - 'api:create_app("prod")' --reload
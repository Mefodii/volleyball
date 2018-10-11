#!/bin/bash
source ../volleyball-venv/bin/activate
python manage.py runserver 173.212.252.36:8000 --settings=volleyball.settings_server
import os
import sys
import django
from multiprocessing import Pool
from django.db import close_old_connections
from datetime import datetime

# Django setup
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wall_tracker_app.settings')
django.setup()

from construction.models import Section

MAX_HEIGHT = 30
LOG_FILE = "work_log.txt"
NUM_TEAMS = 4

def process_section_with_team(args):
    section_id, team_id, day = args
    close_old_connections()

    try:
        section = Section.objects.get(id=section_id)

        if section.current_height < MAX_HEIGHT:
            section.current_height += 1
            section.save()
            log_entry = f"[Day {day}] Team {team_id} processed Section {section.id} -> Height {section.current_height}"
        else:
            log_entry = f"[Day {day}] Team {team_id} relieved – Section {section.id} already complete"

    except Exception as e:
        log_entry = f"[Day {day}] Team {team_id} ERROR on Section {section_id}: {str(e)}"

    with open(LOG_FILE, "a") as log:
        log.write(log_entry + "\n")
    print(log_entry)

def run_multiprocessing():
    day = 1

    while True:
        incomplete_sections = list(
            Section.objects.filter(current_height__lt=MAX_HEIGHT).values_list('id', flat=True)
        )

        if not incomplete_sections:
            print("🎉 All sections completed!")
            break

        team_assignments = [(section_id, (i % NUM_TEAMS) + 1, day) for i, section_id in enumerate(incomplete_sections)]

        with Pool(processes=NUM_TEAMS) as pool:
            pool.map(process_section_with_team, team_assignments)

        day += 1

if __name__ == '__main__':
    run_multiprocessing()

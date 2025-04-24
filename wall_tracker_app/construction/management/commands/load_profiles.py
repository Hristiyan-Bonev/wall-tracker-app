import subprocess
from django.core.management.base import BaseCommand
from construction.models import WallProfile, Section


class Command(BaseCommand):
    help = 'Load wall profiles and trigger section processing with multiprocessing'

    def handle(self, *args, **kwargs):
        file_path = 'input_profiles.txt'
        max_height = 30

        with open(file_path, 'r') as f:
            lines = f.readlines()

            for i, line in enumerate(lines):
                heights = list(map(int, line.strip().split()))
                profile = WallProfile.objects.create(name=f"Profile {i + 1}")
                for height in heights:
                    Section.objects.create(
                        profile=profile,
                        initial_height=height,
                        current_height=height,
                        cost=0.0,
                        completed_day=None
                    )

        self.stdout.write(self.style.SUCCESS("Profiles loaded."))

        # 👇 Launch external multiprocessing safely
        subprocess.run(["python", "scripts/process_sections.py"], check=True)

        self.stdout.write(self.style.SUCCESS("Section processing complete."))
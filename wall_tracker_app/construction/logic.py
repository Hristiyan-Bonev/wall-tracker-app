from .models import Section

ICE_PER_FOOT = 195
COST_PER_CUBIC_YARD = 1900
MAX_HEIGHT = 30

def calculate_day_ice(profile_id, day):
    total_ice = 0
    sections = Section.objects.filter(profile_id=profile_id)
    for section in sections:
        if section.initial_height + day >= MAX_HEIGHT:
            work_days = MAX_HEIGHT - section.initial_height
            if day <= work_days:
                total_ice += ICE_PER_FOOT
        elif section.initial_height + day < MAX_HEIGHT:
            total_ice += ICE_PER_FOOT
    return total_ice

def calculate_cost(profile_id=None, day=None):
    sections = Section.objects.all()
    if profile_id:
        sections = sections.filter(profile_id=profile_id)
    total_cost = 0
    for section in sections:
        max_days = MAX_HEIGHT - section.initial_height
        days_worked = min(day, max_days) if day is not None else max_days
        total_ice = days_worked * ICE_PER_FOOT
        total_cost += total_ice * COST_PER_CUBIC_YARD
    return total_cost

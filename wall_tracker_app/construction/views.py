from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from .logic import calculate_day_ice, calculate_cost
from .models import WallProfile
from datetime import date, timedelta


@api_view(['GET'])
def day_ice_usage(request, profile_id, day):
    return Response({"day": day, "ice_amount": calculate_day_ice(profile_id, int(day))})

@api_view(['GET'])
def profile_cost(request, profile_id, day):
    return Response({"day": day, "cost": calculate_cost(profile_id=int(profile_id), day=int(day))})

@api_view(['GET'])
def overall_cost(request, day=None):
    return Response({"day": day, "cost": calculate_cost(profile_id=None, day=int(day) if day else None)})

@api_view(['GET'])
def profile_overview(request, day):
    return Response({"day": day, "cost": calculate_cost(profile_id=None, day=int(day))})


def index(request):
    profiles = WallProfile.objects.all()
    profile_data = []

    today = date.today()

    for profile in profiles:
        sections = profile.sections.all()
        section_details = []

        for section in sections:
            days_to_build = max(0, 30 - section.initial_height)
            completion_date = today + timedelta(days=days_to_build)
            cost = days_to_build * 195 * 1900  # 195 cubic yards per foot, 1900 coins per cubic yard

            section_details.append({
                'initial_height': section.initial_height,
                'days_to_build': days_to_build,
                'completion_date': completion_date,
                'cost': cost,
            })

        profile_data.append({
            'profile': profile,
            'sections': section_details,
        })

    return render(request, 'construction/index.html', {'profile_data': profile_data})

from django.test import TestCase
from construction.models import WallProfile, Section

class ProfileModelTest(TestCase):
    def test_profile_creation(self):
        profile = WallProfile.objects.create(name="Test Profile")
        self.assertEqual(profile.name, "Test Profile")

class SectionModelTest(TestCase):
    def setUp(self):
        self.profile = WallProfile.objects.create(name="Test Profile")

    def test_section_creation(self):
        section = Section.objects.create(
            profile=self.profile,
            initial_height=10,
            cost=1000
        )
        self.assertEqual(section.profile, self.profile)
        self.assertEqual(section.initial_height, 10)
        self.assertEqual(section.cost, 1000)

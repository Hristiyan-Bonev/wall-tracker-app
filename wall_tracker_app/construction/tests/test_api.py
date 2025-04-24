from django.test import TestCase
from django.urls import reverse
from construction.models import WallProfile, Section
from datetime import date, timedelta

class ViewTests(TestCase):
    def setUp(self):
        # Create a WallProfile instance
        self.profile = WallProfile.objects.create(name="Test Profile")

        # Create Section instances associated with the Profile
        self.section1 = Section.objects.create(
            profile=self.profile,
            initial_height=10,
            cost=1000.00
        )
        self.section2 = Section.objects.create(
            profile=self.profile,
            initial_height=15,
            cost=1500.00
        )

    def test_index_view(self):
        """
        Test the index view returns a 200 status code and contains the profile name.
        """
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.profile.name)
        self.assertContains(response, self.section1.initial_height)
        self.assertContains(response, self.section2.initial_height)

    def test_day_ice_usage_view(self):
        """
        Test the day_ice_usage view returns a 200 status code and contains expected data.
        """
        day = 3
        url = reverse('day_ice_usage', kwargs={'profile_id': self.profile.id, 'day': day})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # Assuming the view returns JSON data with 'ice_usage' key
        self.assertIn('ice_usage', response.json())
        self.assertIsInstance(response.json()['ice_usage'], (int, float))

    def test_profile_cost_view(self):
        """
        Test the profile_cost view returns a 200 status code and contains expected data.
        """
        day = 3
        url = reverse('profile_cost', kwargs={'profile_id': self.profile.id, 'day': day})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # Assuming the view returns JSON data with 'total_cost' key
        self.assertIn('total_cost', response.json())
        self.assertIsInstance(response.json()['total_cost'], (int, float))

    def test_profile_overview_view(self):
        """
        Test the profile_overview view returns a 200 status code and contains expected data.
        """
        day = 3
        url = reverse('profile-overview', kwargs={'day': day})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # Assuming the view returns JSON data with a list of profiles
        self.assertIsInstance(response.json(), dict)
        for profile_data in response.json():
            self.assertIn('profile_name', profile_data)
            self.assertIn('cost', profile_data)

    def test_overall_cost_view(self):
        """
        Test the overall_cost view returns a 200 status code and contains expected data.
        """
        url = reverse('overall_cost')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # Assuming the view returns JSON data with 'total_cost' and 'total_ice' keys
        self.assertIn('total_cost', response.json())
        self.assertIn('total_ice', response.json())
        self.assertIsInstance(response.json()['total_cost'], (int, float))
        self.assertIsInstance(response.json()['total_ice'], (int, float))

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from .models import AstronomyShow, PlanetariumDome, ShowSession


class ShowSessionTests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="andre",
            password="test-password",
        )
        self.show = AstronomyShow.objects.create(
            title="Viagem pelo espaço",
            description="Um espetáculo de astronomia.",
        )
        self.dome = PlanetariumDome.objects.create(
            name="Cúpula principal",
            rows=10,
            seats_in_row=20,
            description="Cúpula de teste.",
        )
        self.url = reverse("showsession-list")
    def test_authenticated_user_can_create_session(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(
            self.url,
            {
                "astronomy_show": self.show.id,
                "planetarium_dome": self.dome.id,
                "show_time": "2026-12-01T18:00:00Z",
            },
            format="multipart",
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(ShowSession.objects.count(), 1)

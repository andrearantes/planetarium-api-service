from rest_framework.routers import DefaultRouter
from .views import (AstronomyShowViewSet,
    ShowThemeViewSet,
    PlanetariumDomeViewSet,
    ShowSessionViewSet,
    ReservationViewSet,
    TicketViewSet
                    )


router = DefaultRouter()
router.register("shows", AstronomyShowViewSet)
router.register("themes", ShowThemeViewSet)
router.register("domes", PlanetariumDomeViewSet)
router.register("sessions", ShowSessionViewSet)
router.register("reservations", ReservationViewSet)
router.register("tickets", TicketViewSet)
urlpatterns = router.urls

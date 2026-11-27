from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import (AstronomyShow,
                     ShowTheme,
                     PlanetariumDome,
                     ShowSession,
                     Reservation,
                     Ticket
                     )
from .serializers import (AstronomyShowSerializer,
                          ShowThemeSerializer,
                          PlanetariumDomeSerializer,
                          ShowSessionSerializer,
                          ReservationSerializer,
                          TicketSerializer
                          )


class AstronomyShowViewSet(ModelViewSet):
    queryset = AstronomyShow.objects.all()
    serializer_class = AstronomyShowSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.query_params.get("title")
        theme_id = self.request.query_params.get("theme")
        if title:
            queryset = queryset.filter(title__icontains=title)
        if theme_id:
            queryset = queryset.filter(themes__id=theme_id).distinct()
        return queryset


class ShowThemeViewSet(ModelViewSet):
    queryset = ShowTheme.objects.all()
    serializer_class = ShowThemeSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.query_params.get("name")
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class PlanetariumDomeViewSet(ModelViewSet):
    queryset = PlanetariumDome.objects.all()
    serializer_class = PlanetariumDomeSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.query_params.get("name")
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class ShowSessionViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = ShowSession.objects.all()
    serializer_class = ShowSessionSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        dome_id = self.request.query_params.get("planetarium_dome")
        show_id = self.request.query_params.get("astronomy_show")
        if dome_id:
            queryset = queryset.filter(planetarium_dome_id=dome_id)
        if show_id:
            queryset = queryset.filter(astronomy_show_id=show_id)
        return queryset


class ReservationViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TicketViewSet(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Ticket.objects.filter(
            reservation__user=self.request.user
        )

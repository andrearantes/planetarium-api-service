from rest_framework import serializers

from .models import (
    AstronomyShow,
    PlanetariumDome,
    ShowTheme,
    ShowSession,
    Reservation,
    Ticket
)


class ShowThemeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShowTheme
        fields = ("id",
                  "name"
                  )


class AstronomyShowSerializer(serializers.ModelSerializer):
    themes = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=ShowTheme.objects.all()
    )

    class Meta:
        model = AstronomyShow
        fields = ("id",
                  "title",
                  "description",
                  "themes"
                  )


class PlanetariumDomeSerializer(serializers.ModelSerializer):
    capacity = serializers.SerializerMethodField()

    class Meta:
        model = PlanetariumDome
        fields = ("id",
            "name",
            "rows",
            "seats_in_row",
            "description",
            "capacity",
        )

    def get_capacity(self, obj):
        return obj.rows * obj.seats_in_row


class ShowSessionSerializer(serializers.ModelSerializer):
    astronomy_show = serializers.PrimaryKeyRelatedField(
        queryset=AstronomyShow.objects.all()
    )
    planetarium_dome = serializers.PrimaryKeyRelatedField(
        queryset=PlanetariumDome.objects.all()
    )

    class Meta:
        model = ShowSession
        fields = "__all__"


class ReservationSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Reservation
        fields = "__all__"


class TicketSerializer(serializers.ModelSerializer):
    show_session = serializers.PrimaryKeyRelatedField(
        queryset=ShowSession.objects.all()
    )
    reservation = serializers.PrimaryKeyRelatedField(
        queryset=Reservation.objects.all()
    )

    class Meta:
        model = Ticket
        fields = "__all__"

    def validate_reservation(self, reservation):
        if reservation.user != self.context["request"].user:
            raise serializers.ValidationError(
                "You can only use your own reservation."
            )
        return reservation

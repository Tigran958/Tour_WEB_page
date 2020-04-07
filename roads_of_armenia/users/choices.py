from django.utils.translation import ugettext_lazy as _

USER_CHOICES = (
    (1, _("Driver")),
    (2, _("Client")),
    (3, _("Guide")),
    (4, _("TourAgents"))
)

CAR_CHOICES = (
    (1, _("BMW")),
    (2, _("Mercedes Benz"))
)

LANGUAGES_CHOICES = (
    (1, _("Armenian")),
    (2, _("English")),
    (3, _("France")),
    (4, _("Russian")),
)

TOUR_CHOICES = (
    (1, _("Extreme")),
)

GENDER_CHOICES = (
    (1, _("Male")),
    (2, _("Female"))
)

AGE_CHOICES = (
    (1, _("18-25")),
    (2, _("25-35")),
    (3, _("35+"))
)

REGION_CHOICES = (
    (1, _("Armavir")),
    (2, _("Yerevan")),
    (3, _("Kotayq"))
)


WEEK_DAY_CHOICES = (
    (1, _("Monday")),
    (2, _("Tuesday")),
    (3, _("Wednesday")),
    (4, _("Thursday")),
    (5, _("Frayday")),
    (6, _("Saturday")),
    (7, _("Sunday"))
    )

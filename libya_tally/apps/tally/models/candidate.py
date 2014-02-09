from django.db import models
from django.utils.translation import ugettext as _
from django_enumfield import enum

from libya_tally.apps.tally.models.ballot import Ballot
from libya_tally.libs.models.base_model import BaseModel
from libya_tally.libs.models.enums.race_type import RaceType


class Candidate(BaseModel):
    class Meta:
        app_label = 'tally'

    ballot = models.ForeignKey(Ballot, related_name='candidates')

    candidate_id = models.PositiveIntegerField()
    full_name = models.TextField()
    order = models.PositiveSmallIntegerField()
    race_type = enum.EnumField(RaceType)

    @property
    def race_type_name(self):
        return {
            0: _('General'),
            1: _('Women'),
            2: _('Component Amazigh'),
            3: _('Component Twarag'),
            4: _('Component Tebu')
        }[self.race_type]

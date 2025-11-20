from django.forms import ModelForm
from TombolaDisplay.models import Participant, Tombola  # Remplace Users par Participant

class ParticipantForm(ModelForm):  # Remplace UsersForm par ParticipantForm
    class Meta:
        model = Participant  # Remplace Users par Participant
        fields = ['name', 'firstname', 'email']  # Corrige aussi fristname ➔ firstname

# Pour ajouter un participant
form = ParticipantForm()

# Pour mettre à jour un participant
# pistache = Participant.objects.get(pk=1)
# form = ParticipantForm(instance=pistache)

class TombolaForm(ModelForm):
    class Meta:
        model = Tombola
        fields = ['name', 'created_at','finished_at','is_open']
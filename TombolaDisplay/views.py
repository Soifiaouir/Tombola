from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from .models import Participant, Ticket, Tombola
from .forms import ParticipantForm, TombolaForm


def user(request):
    if request.method == "POST":
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = ParticipantForm()  # GET : formulaire vide

    return render(request, "TombolaDisplay/user.html", {"form": form})

def index(request):
    participant = Participant.objects.get(pk=1)
    return render(request, 'TombolaDisplay/index.html', {'participant': participant})

def tombola_create(request, participant_id):
    participant = get_object_or_404(Participant, pk=participant_id)
    if request.method == "POST":
        form = TombolaForm(request.POST)
        if form.is_valid():
            tombola = form.save(commit=False)  # Ne sauvegarde pas encore
            tombola.owner = participant
            tombola.save()
            for i in range(50):
                Ticket.objects.create(
                    price=2.0,
                    date=date.today(),
                    owner=None,  # ou laisser vide si le ticket n'est pas attribué lors de la création
                    tombola=tombola
                )

            return redirect("index")
    else:
        form = TombolaForm()

    return render(request, 'TombolaDisplay/tombola.html', {'participant': participant, 'form': form})

def get_ticket(request, participant_id, tombola_id):
    participant = get_object_or_404(Participant, pk=participant_id)
    tombola = get_object_or_404(Tombola, pk=tombola_id)
    # Prendre un ticket non attribué pour cette tombola
    ticket = Ticket.objects.filter(owner=None, tombola=tombola).first()
    if ticket:
        ticket.owner = participant
        ticket.save()
    else:
        # Optionnel : gérer le cas où il n'y a plus de tickets disponibles !
        pass
    return redirect('index')





from django.core.signals import request_finished
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Message
from pydub import AudioSegment
from pydub.playback import play
from pydub.playback import _play_with_simpleaudio
import simpleaudio

@receiver(post_save, sender = Message)
def notification(sender, instance, created, **kwargs):

    if created == True:
        print(f"NEW MESSAGE FROM {instance.user.username}")
        song = AudioSegment.from_mp3("Main/song.mp3")
        _play_with_simpleaudio(song)
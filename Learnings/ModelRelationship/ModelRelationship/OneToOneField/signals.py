from .models import Page
from django.db.models.signals import post_delete
from django.dispatch import receiver

# when we delete a page it will generate a post delete signal
# on signal post delete send by page model
@receiver(post_delete, sender=Page)
def delete_related_user(sender, instance, **kwargs):
    print("Page Post deleted")
    instance.user.delete() # take the user instance and delete that user which generate that signal
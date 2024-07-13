import os
from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from .models import WebsiteInfo, CarouselImages, ProjectImage, Projects

# Função utilitária para deletar a imagem antiga se foi modificada
def delete_old_image(instance, field_name):
    try:
        old_image = getattr(instance, f'_old_{field_name}')
        current_image = getattr(instance, field_name)
        if old_image and old_image != current_image:
            old_image.delete(save=False)
    except AttributeError:
        pass

# Sinal pre_save para WebsiteInfo
@receiver(pre_save, sender=WebsiteInfo)
def auto_delete_old_about_picture_on_change(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_instance = WebsiteInfo.objects.get(pk=instance.pk)
            instance._old_about_picture = old_instance.about_picture
        except WebsiteInfo.DoesNotExist:
            pass

# Sinal pre_save para CarouselImages
@receiver(pre_save, sender=CarouselImages)
def auto_delete_old_image_on_change(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_instance = CarouselImages.objects.get(pk=instance.pk)
            instance._old_image = old_instance.image
        except CarouselImages.DoesNotExist:
            pass

# Sinal pre_save para ProjectImage
@receiver(pre_save, sender=ProjectImage)
def auto_delete_old_project_image_on_change(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_instance = ProjectImage.objects.get(pk=instance.pk)
            instance._old_image = old_instance.image
        except ProjectImage.DoesNotExist:
            pass

# Sinal post_delete para WebsiteInfo
@receiver(post_delete, sender=WebsiteInfo)
def auto_delete_about_picture_on_delete(sender, instance, **kwargs):
    instance.about_picture.delete(save=False)

# Sinal post_delete para CarouselImages
@receiver(post_delete, sender=CarouselImages)
def auto_delete_image_on_delete(sender, instance, **kwargs):
    instance.image.delete(save=False)

# Sinal post_delete para ProjectImage
@receiver(post_delete, sender=ProjectImage)
def auto_delete_project_image_on_delete(sender, instance, **kwargs):
    instance.image.delete(save=False)

# Sinal para ProjectImage, para deletar a imagem antiga se uma nova imagem for atribuída
@receiver(post_save, sender=ProjectImage)
def delete_old_image_on_change(sender, instance, **kwargs):
    delete_old_image(instance, 'image')

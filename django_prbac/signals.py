from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django_prbac.models import Grant
from django.core.cache import cache


@receiver(post_save, sender=Grant, dispatch_uid='clear-grant-cache')
def clear_grant_cache(sender, instance, created, **kwargs):
    if isinstance(instance, Grant):
        key = instance.from_role.get_privilege_cache_key(instance.to_role.slug, instance.assignment)
        cache.delete(key)


@receiver(pre_delete, sender=Grant, dispatch_uid='clear-grant-cache-delete')
def clear_grant_cache_delete(sender, instance, **kwargs):
    if isinstance(instance, Grant):
        key = instance.from_role.get_privilege_cache_key(instance.to_role.slug, instance.assignment)
        cache.delete(key)

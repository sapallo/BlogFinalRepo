from django.db.models.signals import post_save
from django.contrib.auth.models import Permission, Group 
from django.contrib.contenttypes.models import ContentType
from django.dispatch import receiver
from apps.user.models import User
from apps.post.models import Post, Comment


@receiver(post_save, sender=User)
def created_groups_and_permissions(sender, instance, created, **kwargs):
    if created and instance.is_superuser:
        try:
            post_content_type = ContentType.objects.get_for_model(Post)
            comment_content_type = ContentType.objects.get_for_model(Comment)

            # permiso post, aca los creo y luego los asigno
            view_post_permission = Permission.objects.get(
                codename="view_post", content_type=post_content_type)
            add_post_permission = Permission.objects.get(
                codename="add_post", content_type=post_content_type)
            change_post_permission = Permission.objects.get(
                codename="change_post", content_type=post_content_type)
            delate_post_permission = Permission.objects.get(
                codename="delate_post", content_type=post_content_type)
            
            # permisos de comentarios

            view_comment_permission = Permission.objects.get(
                codename="view_comment", content_type=post_content_type)
            add_comment_permission = Permission.objects.get(
                codename="add_comment", content_type=comment_content_type)
            change_comment_permission = Permission.objects.get(
                codename="change_comment", content_type=comment_content_type)
            delate_comment_permission = Permission.objects.get(
                codename="delate_comment", content_type=comment_content_type)
            
            #crear grupo de usuario registrado
            registered_group, created = Group.objects.get_or_created(
                name='Registered')
            registered_group.permissions.add(
                view_post_permission,
                add_post_permission,
                change_post_permission,
                delate_post_permission,
                view_comment_permission,
                add_comment_permission,
                delate_comment_permission,
            ) #dejar los permisis segun la consigna, ahora agrego todos

            registered_group, created = Group.objects.get_or_create(
                name='Collaborators')
            registered_group.permissions.add(
                view_post_permission,
                add_post_permission,
                change_post_permission,
                delate_post_permission,
                view_comment_permission,
                add_comment_permission,
                delate_comment_permission,
            )

            registered_group, created = Group.objects.get_or_created(
                name='Admins')
            registered_group.permissions.set(Permission.objects.all())
        except ContentType.DoesNotExist:
            print("Tipo de contenido no disponible")
        except Permission.DoesNotExist:
            print("Permisos no disponible")
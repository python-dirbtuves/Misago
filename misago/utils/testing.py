from django.core.management import call_command

from misago.models import Forum, ForumRole, Role


def fix_hardcoded_role(forums, forum_roles, role_name):
    role = Role.objects.get(name=role_name)
    perms = dict(role.permissions)
    perms['forums'] = {
        forums[forum_id]: forum_roles[forum_role_id]
        for forum_id, forum_role_id in perms['forums'].items()
    }
    role.permissions = perms
    role.save()


def fix_hardoced_fixtures():
    forums = {
        1: Forum.objects.get(slug='private').pk,
        2: Forum.objects.get(slug='reports').pk,
        3: Forum.objects.get(slug='root').pk,
        4: Forum.objects.get(slug='first-category').pk,
        5: Forum.objects.get(slug='first-forum').pk,
        6: Forum.objects.get(slug='project-homepage').pk,
    }

    forum_roles = {
        1: ForumRole.objects.get(name='Full Access').pk,
        2: ForumRole.objects.get(name='Standard Access and Upload').pk,
        3: ForumRole.objects.get(name='Standard Access').pk,
        4: ForumRole.objects.get(name='Read and Download').pk,
        5: ForumRole.objects.get(name='Threads list only').pk,
        6: ForumRole.objects.get(name='Read only').pk,
    }

    fix_hardcoded_role(forums, forum_roles, "Administrator")
    fix_hardcoded_role(forums, forum_roles, "Moderator")
    fix_hardcoded_role(forums, forum_roles, "Registered")
    fix_hardcoded_role(forums, forum_roles, "Guest")


def load_fixtures():
    call_command('syncfixtures', quiet=1)
    fix_hardoced_fixtures()

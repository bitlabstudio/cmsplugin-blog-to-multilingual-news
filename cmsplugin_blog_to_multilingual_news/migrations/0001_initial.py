# flake8: noqa
# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.db import models, connection


def get_models():
    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.globalpagepermission': {
            'Meta': {'object_name': 'GlobalPagePermission'},
            'can_add': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'can_change': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'can_change_advanced_settings': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'can_change_permissions': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'can_delete': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'can_move_page': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'can_publish': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'can_recover_page': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'can_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.Group']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['sites.Site']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'cms.page': {
            'Meta': {'ordering': "('tree_id', 'lft')", 'unique_together': "(('publisher_is_draft', 'application_namespace'),)", 'object_name': 'Page'},
            'application_namespace': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'application_urls': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'changed_by': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_navigation': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'is_home': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'languages': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'limit_visibility_in_menu': ('django.db.models.fields.SmallIntegerField', [], {'default': 'None', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'navigation_extenders': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['cms.Page']"}),
            'placeholders': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['cms.Placeholder']", 'symmetrical': 'False'}),
            'publication_date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'publication_end_date': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'publisher_is_draft': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'publisher_public': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'publisher_draft'", 'unique': 'True', 'null': 'True', 'to': "orm['cms.Page']"}),
            'reverse_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'revision_id': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'djangocms_pages'", 'to': u"orm['sites.Site']"}),
            'soft_root': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'template': ('django.db.models.fields.CharField', [], {'default': "'INHERIT'", 'max_length': '100'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.pagemoderatorstate': {
            'Meta': {'ordering': "('page', 'action', '-created')", 'object_name': 'PageModeratorState'},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '1000', 'blank': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Page']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'})
        },
        'cms.pagepermission': {
            'Meta': {'object_name': 'PagePermission'},
            'can_add': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'can_change': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'can_change_advanced_settings': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'can_change_permissions': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'can_delete': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'can_move_page': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'can_publish': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'can_view': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'grant_on': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.Group']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Page']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'cms.pageuser': {
            'Meta': {'object_name': 'PageUser', '_ormbases': [u'auth.User']},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'created_users'", 'to': u"orm['auth.User']"}),
            u'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        'cms.pageusergroup': {
            'Meta': {'object_name': 'PageUserGroup', '_ormbases': [u'auth.Group']},
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'created_usergroups'", 'to': u"orm['auth.User']"}),
            u'group_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.Group']", 'unique': 'True', 'primary_key': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'cms.placeholderreference': {
            'Meta': {'object_name': 'PlaceholderReference', 'db_table': "u'cmsplugin_placeholderreference'", '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'placeholder_ref': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'})
        },
        'cms.staticplaceholder': {
            'Meta': {'object_name': 'StaticPlaceholder'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'blank': 'True'}),
            'creation_method': ('django.db.models.fields.CharField', [], {'default': "'code'", 'max_length': '20', 'blank': 'True'}),
            'dirty': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'draft': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'static_draft'", 'null': 'True', 'to': "orm['cms.Placeholder']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'public': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'static_public'", 'null': 'True', 'to': "orm['cms.Placeholder']"})
        },
        'cms.title': {
            'Meta': {'unique_together': "(('language', 'page'),)", 'object_name': 'Title'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'has_url_overwrite': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'menu_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'meta_description': ('django.db.models.fields.TextField', [], {'max_length': '155', 'null': 'True', 'blank': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'title_set'", 'to': "orm['cms.Page']"}),
            'page_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'publisher_is_draft': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'publisher_public': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'publisher_draft'", 'unique': 'True', 'null': 'True', 'to': "orm['cms.Title']"}),
            'publisher_state': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'db_index': 'True'}),
            'redirect': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'cms.usersettings': {
            'Meta': {'object_name': 'UserSettings'},
            'clipboard': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'djangocms_usersettings'", 'to': u"orm['auth.User']"})
        },
        'cmsplugin_blog.entry': {
            'Meta': {'ordering': "('-pub_date',)", 'object_name': 'Entry'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'placeholders': ('djangocms_utils.fields.M2MPlaceholderField', [], {'to': "orm['cms.Placeholder']", 'symmetrical': 'False'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'tags': ('tagging.fields.TagField', [], {})
        },
        'cmsplugin_blog.entrytitle': {
            'Meta': {'unique_together': "(('language', 'slug'),)", 'object_name': 'EntryTitle'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'entry': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cmsplugin_blog.Entry']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'cmsplugin_blog.latestentriesplugin': {
            'Meta': {'object_name': 'LatestEntriesPlugin', 'db_table': "'cmsplugin_latestentriesplugin'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'current_language_only': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'limit': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'tagged': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'filer.clipboard': {
            'Meta': {'object_name': 'Clipboard'},
            'files': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'in_clipboards'", 'symmetrical': 'False', 'through': "orm['filer.ClipboardItem']", 'to': "orm['filer.File']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'filer_clipboards'", 'to': "orm['auth.User']"})
        },
        'filer.clipboarditem': {
            'Meta': {'object_name': 'ClipboardItem'},
            'clipboard': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['filer.Clipboard']"}),
            'file': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['filer.File']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'filer.file': {
            'Meta': {'object_name': 'File'},
            '_file_size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'folder': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'all_files'", 'null': 'True', 'to': "orm['filer.Folder']"}),
            'has_all_mandatory_data': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'original_filename': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'owned_files'", 'null': 'True', 'to': "orm['auth.User']"}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'polymorphic_filer.file_set'", 'null': 'True', 'to': "orm['contenttypes.ContentType']"}),
            'sha1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '40', 'blank': 'True'}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'filer.folder': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('parent', 'name'),)", 'object_name': 'Folder'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'filer_owned_folders'", 'null': 'True', 'to': "orm['auth.User']"}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['filer.Folder']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'filer.folderpermission': {
            'Meta': {'object_name': 'FolderPermission'},
            'can_add_children': ('django.db.models.fields.SmallIntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'can_edit': ('django.db.models.fields.SmallIntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'can_read': ('django.db.models.fields.SmallIntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'everybody': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'folder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['filer.Folder']", 'null': 'True', 'blank': 'True'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'filer_folder_permissions'", 'null': 'True', 'to': "orm['auth.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'filer_folder_permissions'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'filer.image': {
            'Meta': {'object_name': 'Image', '_ormbases': ['filer.File']},
            '_height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            '_width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'date_taken': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'default_alt_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'default_caption': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'file_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['filer.File']", 'unique': 'True', 'primary_key': 'True'}),
            'must_always_publish_author_credit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'must_always_publish_copyright': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subject_location': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '64', 'null': 'True', 'blank': 'True'})
        },
        u'multilingual_news.category': {
            'Meta': {'object_name': 'Category'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '512'})
        },
        u'multilingual_news.categoryplugin': {
            'Meta': {'object_name': 'CategoryPlugin', '_ormbases': ['cms.CMSPlugin']},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['multilingual_news.Category']", 'symmetrical': 'False'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'template_argument': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        },
        u'multilingual_news.categorytranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'CategoryTranslation', 'db_table': "u'multilingual_news_category_translation'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['multilingual_news.Category']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'multilingual_news.newsentry': {
            'Meta': {'ordering': "('-pub_date',)", 'object_name': 'NewsEntry'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'multilingual_news_contents'", 'null': 'True', 'to': "orm['cms.Placeholder']"}),
            'excerpt': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'multilingual_news_excerpts'", 'null': 'True', 'to': "orm['cms.Placeholder']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'newsentries'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['multilingual_news.Category']"}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['filer.Image']", 'null': 'True', 'blank': 'True'}),
            'image_float': ('django.db.models.fields.CharField', [], {'max_length': '8', 'blank': 'True'}),
            'image_height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'image_source_text': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'image_source_url': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True'}),
            'image_width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'multilingual_news.newsentrytranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'NewsEntryTranslation', 'db_table': "u'multilingual_news_newsentry_translation'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['multilingual_news.NewsEntry']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '512'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        u'multilingual_news.recentplugin': {
            'Meta': {'object_name': 'RecentPlugin', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'current_language_only': ('django.db.models.fields.BooleanField', [], {}),
            'limit': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'multilingual_tags.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '64'})
        },
        u'multilingual_tags.taggeditem': {
            'Meta': {'unique_together': "(('content_type', 'object_id', 'tag'),)", 'object_name': 'TaggedItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tagged_items'", 'to': u"orm['multilingual_tags.Tag']"})
        },
        u'multilingual_tags.tagtranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'TagTranslation', 'db_table': "u'multilingual_tags_tag_translation'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['multilingual_tags.Tag']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'tagging.tag': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        },
        'tagging.taggeditem': {
            'Meta': {'object_name': 'TaggedItem'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'taggeditem_set'", 'to': u"orm['tagging.Tag']"})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }

    }
    table_names = connection.introspection.table_names()
    if 'tagging_translated_tagtranslated' in table_names:
        models.update({
            'tagging_translated.tagtranslated': {
                'Meta': {'object_name': 'TagTranslated'},
                'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
                'tag': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'translated'", 'unique': 'True', 'to': "orm['tagging.Tag']"})
            },
            'tagging_translated.tagtranslatedtranslation': {
                'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'TagTranslatedTranslation', 'db_table': "'tagging_translated_tagtranslated_translation'"},
                'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
                'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
                'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['tagging_translated.TagTranslated']"}),
                'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
            }
        })
    if 'cmsplugin_blog_categories_category' in table_names:
        models.update({
            'cmsplugin_blog_categories.category': {
                'Meta': {'object_name': 'Category'},
                'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
                'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
                'slug': ('django.db.models.fields.SlugField', [], {'max_length': '512'})
            },
            'cmsplugin_blog_categories.categoryplugin': {
                'Meta': {'object_name': 'CategoryPlugin', 'db_table': "'cmsplugin_categoryplugin'", '_ormbases': ['cms.CMSPlugin']},
                'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['cmsplugin_blog_categories.Category']", 'symmetrical': 'False'}),
                'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
                'template_argument': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
            },
            'cmsplugin_blog_categories.categorytitle': {
                'Meta': {'object_name': 'CategoryTitle'},
                'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cmsplugin_blog_categories.Category']"}),
                'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
                'language': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
                'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
            },
            'cmsplugin_blog_categories.entrycategory': {
                'Meta': {'object_name': 'EntryCategory'},
                'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entry_categories'", 'to': "orm['cmsplugin_blog_categories.Category']"}),
                'entry': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'categories'", 'to': "orm['cmsplugin_blog.Entry']"}),
                'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
            },
        })
    if 'hero_slider_slideritem' in table_names:
        models.update({
            'hero_slider.slideritem': {
                'Meta': {'object_name': 'SliderItem'},
                'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hero_slider.SliderItemCategory']", 'null': 'True', 'blank': 'True'}),
                'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
                'external_url': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
                'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
                'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['filer.File']"}),
                'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
                'position': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
            },
            'hero_slider.slideritemcategory': {
                'Meta': {'object_name': 'SliderItemCategory'},
                'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
                'slug': ('django.db.models.fields.SlugField', [], {'max_length': '128'})
            },
            'hero_slider.slideritemcategorytranslation': {
                'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'SliderItemCategoryTranslation', 'db_table': "'hero_slider_slideritemcategory_translation'"},
                'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
                'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
                'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['hero_slider.SliderItemCategory']"}),
                'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
            },
            'hero_slider.slideritemtranslation': {
                'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'SliderItemTranslation', 'db_table': "'hero_slider_slideritem_translation'"},
                'description': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
                'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
                'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
                'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
                'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': "orm['hero_slider.SliderItem']"}),
                'title': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'})
            },
        })
    if 'cmsplugin_blog_seo_addons_seoaddon' in table_names:
        models.update({
            'cmsplugin_blog_seo_addons.entryseoaddon': {
                'Meta': {'object_name': 'EntrySEOAddon'},
                'entry': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cmsplugin_blog.Entry']"}),
                'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
                'seoaddon': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cmsplugin_blog_seo_addons.SEOAddon']", 'null': 'True', 'blank': 'True'})
            },
            'cmsplugin_blog_seo_addons.seoaddon': {
                'Meta': {'object_name': 'SEOAddon'},
                'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
            },
            'cmsplugin_blog_seo_addons.seoaddontranslation': {
                'Meta': {'object_name': 'SEOAddonTranslation'},
                'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
                'language': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
                'meta_description': ('django.db.models.fields.TextField', [], {'max_length': '512', 'blank': 'True'}),
                'seoaddon': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cmsplugin_blog_seo_addons.SEOAddon']"})
            },
        })

    return models


class Migration(SchemaMigration):

    depends_on = (
        ('multilingual_news', '0013_auto__add_field_newsentrytranslation_meta_title__add_field_newsentrytr'),
        ('cms', '0058_placeholderref_table_rename'),
    )

    def migrate_placeholder(self, orm, entry, news_entry, old_slot, new_slot, new_field):
        placeholder = None
        try:
            placeholder_m2m_object = entry.placeholders.through.objects.get(
                entry=entry, placeholder__slot=old_slot)
            placeholder = placeholder_m2m_object.placeholder
        except ObjectDoesNotExist:
            pass

        if placeholder:
            placeholder_cls = orm['cms.Placeholder']
            new_placeholder = placeholder_cls.objects.create(slot=new_slot)
            for plugin in placeholder.get_plugins():
                plugin.placeholder_id = new_placeholder.pk
                plugin.save()
            setattr(news_entry, new_field, new_placeholder)
            news_entry.save()
            try:
                placeholder_m2m_object.delete()
                placeholder.delete()
            except ObjectDoesNotExist:
                pass

    def forwards(self, orm):
        # replace former cmsplugin_blog apphooks with the apphook of multilingual_news
        for page in orm['cms.Page'].objects.all():
            if page.application_urls == 'BlogApphook':
                page.application_urls = 'MultilingualNewsApphook'
                page.save()

        table_names = connection.introspection.table_names()
        # if cmsplugin-blog-categories was installed
        if 'cmsplugin_blog_categories_category' in table_names:
            # copy over all categories and translations
            for category in orm['cmsplugin_blog_categories.Category'].objects.all():
                news_category = orm['multilingual_news.Category'].objects.create(
                    creation_date=category.creation_date,
                    slug=category.slug,
                )
                for title in orm['cmsplugin_blog_categories.CategoryTitle'].objects.filter(category=category):
                    orm['multilingual_news.CategoryTranslation'].objects.create(
                        title=title.title,
                        language_code=title.language,
                        master=news_category,
                    )

        # move every cmsplugin_blog.Entry to a multilingual_news.NewsEntry
        for entry in orm['cmsplugin_blog.Entry'].objects.all():
            author = None
            # since we can't determine some other way, we always try to
            # select the author found in the first translation or set it to
            # None if that fails.
            try:
                author = orm['cmsplugin_blog.EntryTitleTranslation'].objects.filter(entry=entry)[0]
            except:
                pass
            # create the new news_entry shared master object
            news_entry = orm['multilingual_news.NewsEntry'].objects.create(
                pub_date=entry.pub_date,
                author=author,
            )
            # migrate tagging to mutlilingual_tags and re-assign the new
            # news entries
            news_entry_ctype = orm['contenttypes.ContentType'].objects.get(app_label='multilingual_news', model='newsentry')
            entry_ctype = orm['contenttypes.ContentType'].objects.get(app_label='cmsplugin_blog', model='entry')
            for tagged_item in orm['tagging.TaggedItem'].objects.filter(content_type=entry_ctype, object_id=entry.id):
                try:
                    multilingual_tag = orm['multilingual_tags.Tag'].objects.get(
                        slug=tagged_item.tag.name.lower())
                except ObjectDoesNotExist:
                    multilingual_tag = orm['multilingual_tags.Tag'].objects.create(
                        slug=tagged_item.tag.name.lower())
                    # optionally taking the translated tags into account
                    if 'tagging_translated_tagtranslated' in table_names:
                        for tagtranslated in orm['tagging_translated.TagTranslatedTranslation'].objects.filter(
                                tagtranslated__tag=tagged_item.tag):
                            orm['multilingual_tags.TagTranslation'].objects.get_or_create(
                                language_code=tagtranslated.language_code,
                                master=multilingual_tag,
                                name=tagtranslated.name)
                    else:
                        orm['multilingual_tags.TagTranslation'].objects.get_or_create(
                            language_code=settings.LANGUAGE_CODE,
                            master=multilingual_tag,
                            name=tagged_item.tag.name)
                orm['multilingual_tags.TaggedItem'].objects.get_or_create(
                    content_type=news_entry_ctype, object_id=news_entry.id,
                    tag=multilingual_tag)

            for title in orm['cmsplugin_blog.EntryTitle'].objects.filter(entry=entry):
                # if cmsplugin_blog_seo_addons is present, we migrate the data over from
                # there
                meta_description = ''
                if 'cmsplugin_blog_seo_addons_seoaddon' in table_names:
                    try:
                        addon = orm['cmsplugin_blog_seo_addons.EntrySEOAddon'].objects.get(entry=entry)
                        addon_trans = orm['cmsplugin_blog_seo_addons.SEOAddonTranslation'].objects.get(seoaddon=addon)
                    except ObjectDoesNotExist:
                        pass
                    else:
                        meta_description = addon_trans.meta_description
                # if cmsplugin-blog-language-publish has been added and
                # used, we have a table for it, so we look into the data,
                # that we find there and apply it if necessary. Otherwise
                # the fallback is the entry.is_published value
                is_published = entry.is_published
                if 'cmsplugin_blog_language_publish' in table_names:
                    try:
                        is_published = orm['cmsplugin_blog_language_publish.EntryLanguagePublish'].objects.get(
                            entry_title=title).is_published
                    except ObjectDoesNotExist:
                        pass
                # create the translation objects for the news entry
                # belonging to the recently created master
                creation_kwargs = {
                    'title': title.title,
                    'slug': title.slug,
                    'is_published': is_published,
                    'master': news_entry,
                    'language_code': title.language,
                    'meta_description': meta_description,
                }
                orm['multilingual_news.NewsEntryTranslation'].objects.create(
                    title=title.title,
                    slug=title.slug,
                    is_published=is_published,
                    master=news_entry,
                    language_code=title.language,
                )

            # if hero_slider is present, we change the content_object
            if 'hero_slider_slideritem' in table_names:
                try:
                    ctype = orm['contenttypes.ContentType'].objects.get(app_label='cmsplugin_blog', name='entry')
                    slideritem = orm['hero_slider.Slideritem'].objects.get(content_type=ctype, object_id=entry.id)
                except ObjectDoesNotExist:
                    pass
                else:
                    newsctype = orm['contenttypes.ContentType'].objects.get(app_label='multilingual_news', name='news entry')
                    slideritem.content_type = newsctype
                    slideritem.object_id = news_entry.id
                    slideritem.save()

            # if cmsplugin_blog_categories was installed
            if 'cmsplugin_blog_categories_category' in table_names:
                # get all the entrycategory instances for this entry
                entrycategories = orm['cmsplugin_blog_categories.EntryCategory'].objects.filter(entry=entry)
                # ... and for each of its instances
                for entrycategory in entrycategories:
                    # ... try to get the new category, we've recently
                    # created
                    try:
                        news_category = orm['multilingual_news.Category'].objects.get(slug=entrycategory.category.slug)
                    except ObjectDoesNotExist:
                        pass
                    else:
                        # ... and add it to the entry's categories
                        news_entry.categories.add(news_category)


            # copy the placeholders from the cmsplugin_blog.Entry to the two
            # new fields on the multilingual_news.NewsEntry
            self.migrate_placeholder(
                orm, entry, news_entry, 'content', 'multilingual_news_content', 'content')
            self.migrate_placeholder(
                orm, entry, news_entry, 'excerpt', 'multilingual_news_excerpt', 'excerpt')

            # change the page apphooks from BlogCategoriesApphook to
            # MultilingualNewsApphook
            if 'cmsplugin_blog_categories_category' in table_names:
                for page in orm['cms.Page'].objects.all():
                    if page.application_urls == 'BlogCategoriesApphook':
                        page.application_urls = 'MultilingualNewsApphook'
                        page.save()

    def backwards(self, orm):
        pass

    models = get_models()

    complete_apps = ['cmsplugin_blog_to_multilingual_news']
    symmetrical = True

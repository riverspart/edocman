# -*- coding: utf-8 -*-

from odoo.addons.mail.tests.common import TestMail


class TestThmdocumentBase(TestMail):

    @classmethod
    def setUpClass(cls):
        super(TestThmdocumentBase, cls).setUpClass()

        user_group_employee = cls.env.ref('base.group_user')
        user_group_thmdocument_user = cls.env.ref('thmdocument.group_thmdocument_user')
        user_group_thmdocument_manager = cls.env.ref('thmdocument.group_thmdocument_manager')

        # Test users to use through the various tests
        Users = cls.env['res.users'].with_context({'no_reset_password': True})
        cls.user_thmdocumentuser = Users.create({
            'name': 'Armande ThmdocumentUser',
            'login': 'Armande',
            'email': 'armande.thmdocumentuser@example.com',
            'groups_id': [(6, 0, [user_group_employee.id, user_group_thmdocument_user.id])]
        })
        cls.user_thmdocumentmanager = Users.create({
            'name': 'Bastien ThmdocumentManager',
            'login': 'bastien',
            'email': 'bastien.thmdocumentmanager@example.com',
            'groups_id': [(6, 0, [user_group_employee.id, user_group_thmdocument_manager.id])]})

        # Test 'Pigs' thmdocument
        cls.thmdocument_pigs = cls.env['thmdocument.thmdocument'].with_context({'mail_create_nolog': True}).create({
            'name': 'Pigs',
            'privacy_visibility': 'employees',
            'alias_name': 'thmdocument+pigs',
            'partner_id': cls.partner_1.id})
        # Already-existing tasks in Pigs
        cls.task_1 = cls.env['thmdocument.task'].with_context({'mail_create_nolog': True}).create({
            'name': 'Pigs UserTask',
            'user_id': cls.user_thmdocumentuser.id,
            'thmdocument_id': cls.thmdocument_pigs.id})
        cls.task_2 = cls.env['thmdocument.task'].with_context({'mail_create_nolog': True}).create({
            'name': 'Pigs ManagerTask',
            'user_id': cls.user_thmdocumentmanager.id,
            'thmdocument_id': cls.thmdocument_pigs.id})

        # Test 'Goats' thmdocument, same as 'Pigs', but with 2 stages
        cls.thmdocument_goats = cls.env['thmdocument.thmdocument'].with_context({'mail_create_nolog': True}).create({
            'name': 'Goats',
            'privacy_visibility': 'followers',
            'alias_name': 'thmdocument+goats',
            'partner_id': cls.partner_1.id,
            'type_ids': [
                (0, 0, {
                    'name': 'New',
                    'sequence': 1,
                }),
                (0, 0, {
                    'name': 'Won',
                    'sequence': 10,
                })]
            })

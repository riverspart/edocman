# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.addons.thmdocument.tests.test_thmdocument_base import TestThmdocumentBase
from odoo.exceptions import AccessError
from odoo.tools import mute_logger


class TestPortalThmdocumentBase(TestThmdocumentBase):

    def setUp(self):
        super(TestPortalThmdocumentBase, self).setUp()
        self.user_noone = self.env['res.users'].with_context({'no_reset_password': True, 'mail_create_nosubscribe': True}).create({
            'name': 'Noemie NoOne',
            'login': 'noemie',
            'email': 'n.n@example.com',
            'signature': '--\nNoemie',
            'notify_email': 'always',
            'groups_id': [(6, 0, [])]})

        self.task_3 = self.env['thmdocument.task'].with_context({'mail_create_nolog': True}).create({
            'name': 'Test3', 'user_id': self.user_portal.id, 'thmdocument_id': self.thmdocument_pigs.id})
        self.task_4 = self.env['thmdocument.task'].with_context({'mail_create_nolog': True}).create({
            'name': 'Test4', 'user_id': self.user_public.id, 'thmdocument_id': self.thmdocument_pigs.id})
        self.task_5 = self.env['thmdocument.task'].with_context({'mail_create_nolog': True}).create({
            'name': 'Test5', 'user_id': False, 'thmdocument_id': self.thmdocument_pigs.id})
        self.task_6 = self.env['thmdocument.task'].with_context({'mail_create_nolog': True}).create({
            'name': 'Test5', 'user_id': False, 'thmdocument_id': self.thmdocument_pigs.id})


class TestPortalThmdocument(TestPortalThmdocumentBase):

    @mute_logger('odoo.addons.base.ir.ir_model')
    def test_employee_thmdocument_access_rights(self):
        pigs = self.thmdocument_pigs

        pigs.write({'privacy_visibility': 'employees'})
        # Do: Alfred reads thmdocument -> ok (employee ok employee)
        pigs.sudo(self.user_thmdocumentuser).read(['user_id'])
        # Test: all thmdocument tasks visible
        tasks = self.env['thmdocument.task'].sudo(self.user_thmdocumentuser).search([('thmdocument_id', '=', pigs.id)])
        test_task_ids = set([self.task_1.id, self.task_2.id, self.task_3.id, self.task_4.id, self.task_5.id, self.task_6.id])
        self.assertEqual(set(tasks.ids), test_task_ids,
                        'access rights: thmdocument user cannot see all tasks of an employees thmdocument')
        # Do: Bert reads thmdocument -> crash, no group
        self.assertRaises(AccessError, pigs.sudo(self.user_noone).read, ['user_id'])
        # Do: Donovan reads thmdocument -> ko (public ko employee)
        self.assertRaises(AccessError, pigs.sudo(self.user_public).read, ['user_id'])
        # Do: thmdocument user is employee and can create a task
        tmp_task = self.env['thmdocument.task'].sudo(self.user_thmdocumentuser).with_context({'mail_create_nolog': True}).create({
            'name': 'Pigs task',
            'thmdocument_id': pigs.id})
        tmp_task.sudo(self.user_thmdocumentuser).unlink()

    @mute_logger('odoo.addons.base.ir.ir_model')
    def test_followers_thmdocument_access_rights(self):
        pigs = self.thmdocument_pigs
        pigs.write({'privacy_visibility': 'followers'})

        # Do: Alfred reads thmdocument -> ko (employee ko followers)
        self.assertRaises(AccessError, pigs.sudo(self.user_thmdocumentuser).read, ['user_id'])
        # Test: no thmdocument task visible
        tasks = self.env['thmdocument.task'].sudo(self.user_thmdocumentuser).search([('thmdocument_id', '=', pigs.id)])
        self.assertEqual(tasks, self.task_1,
                         'access rights: employee user should not see tasks of a not-followed followers thmdocument, only assigned')

        # Do: Bert reads thmdocument -> crash, no group
        self.assertRaises(AccessError, pigs.sudo(self.user_noone).read, ['user_id'])

        # Do: Donovan reads thmdocument -> ko (public ko employee)
        self.assertRaises(AccessError, pigs.sudo(self.user_public).read, ['user_id'])

        pigs.message_subscribe_users(user_ids=[self.user_thmdocumentuser.id])

        # Do: Alfred reads thmdocument -> ok (follower ok followers)
        prout = pigs.sudo(self.user_thmdocumentuser)
        prout.invalidate_cache()
        prout.read(['user_id'])

        # Do: Donovan reads thmdocument -> ko (public ko follower even if follower)
        self.assertRaises(AccessError, pigs.sudo(self.user_public).read, ['user_id'])
        # Do: thmdocument user is follower of the thmdocument and can create a task
        self.env['thmdocument.task'].sudo(self.user_thmdocumentuser.id).with_context({'mail_create_nolog': True}).create({
            'name': 'Pigs task', 'thmdocument_id': pigs.id
        })
        # not follower user should not be able to create a task
        pigs.sudo(self.user_thmdocumentuser).message_unsubscribe_users(user_ids=[self.user_thmdocumentuser.id])
        self.assertRaises(AccessError, self.env['thmdocument.task'].sudo(self.user_thmdocumentuser).with_context({
            'mail_create_nolog': True}).create, {'name': 'Pigs task', 'thmdocument_id': pigs.id})

        # Do: thmdocument user can create a task without thmdocument
        self.assertRaises(AccessError, self.env['thmdocument.task'].sudo(self.user_thmdocumentuser).with_context({
            'mail_create_nolog': True}).create, {'name': 'Pigs task', 'thmdocument_id': pigs.id})

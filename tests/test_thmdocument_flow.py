# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from .test_thmdocument_base import TestThmdocumentBase
from odoo.tools import mute_logger


EMAIL_TPL = """Return-Path: <whatever-2a840@postmaster.twitter.com>
X-Original-To: {to}
Delivered-To: {to}
To: {to}
cc: {cc}
Received: by mail1.odoo.com (Postfix, from userid 10002)
    id 5DF9ABFB2A; Fri, 10 Aug 2012 16:16:39 +0200 (CEST)
Message-ID: {msg_id}
Date: Tue, 29 Nov 2011 12:43:21 +0530
From: {email_from}
MIME-Version: 1.0
Subject: {subject}
Content-Type: text/plain; charset=ISO-8859-1; format=flowed

Hello,

This email should create a new entry in your module. Please check that it
effectively works.

Thanks,

--
Raoul Boitempoils
Integrator at Agrolait"""


class TestThmdocumentFlow(TestThmdocumentBase):

    def test_thmdocument_process_thmdocument_manager_duplicate(self):
        pigs = self.thmdocument_pigs.sudo(self.user_thmdocumentmanager)
        dogs = pigs.copy()
        self.assertEqual(len(dogs.tasks), 2, 'thmdocument: duplicating a thmdocument must duplicate its tasks')

    @mute_logger('odoo.addons.mail.mail_thread')
    def test_task_process_without_stage(self):
        # Do: incoming mail from an unknown partner on an alias creates a new task 'Frogs'
        task = self.format_and_process(
            EMAIL_TPL, to='thmdocument+pigs@mydomain.com, valid.lelitre@agrolait.com', cc='valid.other@gmail.com',
            email_from='%s' % self.user_thmdocumentuser.email,
            subject='Frogs', msg_id='<1198923581.41972151344608186760.JavaMail@agrolait.com>',
            target_model='thmdocument.task')

        # Test: one task created by mailgateway administrator
        self.assertEqual(len(task), 1, 'thmdocument: message_process: a new thmdocument.task should have been created')
        # Test: check partner in message followers
        self.assertIn(self.partner_2, task.message_partner_ids, "Partner in message cc is not added as a task followers.")
        # Test: messages
        self.assertEqual(len(task.message_ids), 2,
                         'thmdocument: message_process: newly created task should have 2 messages: creation and email')
        self.assertEqual(task.message_ids[1].subtype_id.name, 'Task Opened',
                         'thmdocument: message_process: first message of new task should have Task Created subtype')
        self.assertEqual(task.message_ids[0].author_id, self.user_thmdocumentuser.partner_id,
                         'thmdocument: message_process: second message should be the one from Agrolait (partner failed)')
        self.assertEqual(task.message_ids[0].subject, 'Frogs',
                         'thmdocument: message_process: second message should be the one from Agrolait (subject failed)')
        # Test: task content
        self.assertEqual(task.name, 'Frogs', 'thmdocument_task: name should be the email subject')
        self.assertEqual(task.thmdocument_id.id, self.thmdocument_pigs.id, 'thmdocument_task: incorrect thmdocument')
        self.assertEqual(task.stage_id.sequence, False, "thmdocument_task: shouldn't have a stage, i.e. sequence=False")

    @mute_logger('odoo.addons.mail.mail_thread')
    def test_task_process_with_stages(self):
        # Do: incoming mail from an unknown partner on an alias creates a new task 'Cats'
        task = self.format_and_process(
            EMAIL_TPL, to='thmdocument+goats@mydomain.com, valid.lelitre@agrolait.com', cc='valid.other@gmail.com',
            email_from='%s' % self.user_thmdocumentuser.email,
            subject='Cats', msg_id='<1198923581.41972151344608186760.JavaMail@agrolait.com>',
            target_model='thmdocument.task')

        # Test: one task created by mailgateway administrator
        self.assertEqual(len(task), 1, 'thmdocument: message_process: a new thmdocument.task should have been created')
        # Test: check partner in message followers
        self.assertIn(self.partner_2, task.message_partner_ids, "Partner in message cc is not added as a task followers.")
        # Test: messages
        self.assertEqual(len(task.message_ids), 2,
                         'thmdocument: message_process: newly created task should have 2 messages: creation and email')
        self.assertEqual(task.message_ids[1].subtype_id.name, 'Task Opened',
                         'thmdocument: message_process: first message of new task should have Task Created subtype')
        self.assertEqual(task.message_ids[0].author_id, self.user_thmdocumentuser.partner_id,
                         'thmdocument: message_process: second message should be the one from Agrolait (partner failed)')
        self.assertEqual(task.message_ids[0].subject, 'Cats',
                         'thmdocument: message_process: second message should be the one from Agrolait (subject failed)')
        # Test: task content
        self.assertEqual(task.name, 'Cats', 'thmdocument_task: name should be the email subject')
        self.assertEqual(task.thmdocument_id.id, self.thmdocument_goats.id, 'thmdocument_task: incorrect thmdocument')
        self.assertEqual(task.stage_id.sequence, 1, "thmdocument_task: should have a stage with sequence=1")

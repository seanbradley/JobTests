# -*- coding: utf-8 -*-
"""
    test_users
    ~~~~~~~~~~~~~~

    Creation and Deltion of Test Users

    :copyright: (c) 2012 by Sunrider International
    :license: LICENSE_NAME, see LICENSE_FILE for more details.
"""

import unittest, os, csv
from pages.control import create_app, db
from pages.app.users.models import User

FIXTURES = os.path.abspath(os.path.join(os.path.dirname(__file__), 'fixtures'))
USER_TEST_DATA = os.path.abspath(os.path.join(FIXTURES, 'user_test_data.csv'))


class UsersTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app(init_admin=False)
        self.app.test_request_context().push()

        db.drop_all()
        db.create_all()

        #: Loading Users
        with open(USER_TEST_DATA) as f:
            csv_reader = csv.reader(f, delimiter='|')
            for row in csv_reader:
                db.session.add(User(username=row[0], email=row[2], password=row[1]))
        db.session.commit()

    def tearDown(self):
        db.drop_all()

    def test_create_user(self):
        u = User(username='adminex', email='adminex@me.com', password='adminex')
        u.admin = True
        u.save()
        assert u in db.session

    def test_get_user(self):
        j = User.query.filter_by(username='jonathan').first()
        u = User.query.filter_by(username='Jonathan').first()

        assert u is None
        self.assertEqual(j.username, 'jonathan')

    def test_update_user(self):
        j = User.query.filter_by(username='jonathan').first()
        j.admin = True
        j.save()
        u = User.query.filter_by(username='jonathan').first()
        self.assertEqual(u.admin, True)

    def test_delete_user(self):
        j = User.query.filter_by(username='jonathan').first()
        db.session.delete(j)
        db.session.commit()
        u = User.query.filter_by(username='jonathan').first()
        self.assertEqual(u, None)


if __name__ == '__main__':
    unittest.main()



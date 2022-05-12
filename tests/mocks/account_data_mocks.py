"""
Contains the test fixtures for mocking get_account and post_account.
"""
from dataclasses import dataclass
import pickledb

db = pickledb.load("./tests/mock_db.db", True)

@dataclass
class dummy_response:
    status_code : int

    def json(self):
        return "mock_json"

class account_methods_mock():

    @staticmethod
    def get_account(email_address: str = None, account_id: str = None):
        """get_account
        Returns a entry in the mock store for testing,
        entries created by usage by mock_post_account
        """
        if account_id:
            if db.exists(account_id):
                return dummy_response(status_code=200)
            else:
                return dummy_response(status_code = 404)
        if email_address:
            if db.exists(email_address):
                return dummy_response(status_code=200)
            else:
                return dummy_response(status_code=404)

    @staticmethod
    def post_account(email_address : str):
        """post_account
        Creates a entry in the mock store for use
        by get_account.
        """
        db.set(email_address, "dummy")
        db.dump()
        return dummy_response(status_code=201)

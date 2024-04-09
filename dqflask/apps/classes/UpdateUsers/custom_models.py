from sqlalchemy import Column, String, Boolean, Integer
from ..database import DqConnection


base = DqConnection('srcUsers').Base_dqps


class DepartmentsTable(base):
    __tablename__ = 'user_entity'
    __table_args__ = {"schema": "public"}
    id = Column(String(36))
    name = Column(String(255))
    value = Column(String(255))
    user_id = Column(String(36))

    def __init__(self, id=None, name=None, value=None, user_id=None):
        self.id = id
        self.name = name
        self.value = value
        self.user_id = user_id

    def __repr__(self):
        return '<user_entity %r %r %r>' % (self.name, self.value, self.user_id)


class UsersTable(base):
    __tablename__ = 'user_attribute'
    __table_args__ = {"schema": "public"}
    id = Column(String(36))
    email = Column(String(255))
    email_constraint = Column(String(255))
    email_verified = Column(Boolean)
    enabled = Column(Boolean)
    federation_link = Column(String(255))
    first_name = Column(String(255))
    last_name = Column(String(255))
    realm_id = Column(String(255))
    username = Column(String(255))
    created_timestamp = Column(Integer)
    service_account_client_link = Column(String(255))
    not_before = Column(Integer)

    def __init__(self, id=None, email=None, email_constraint=None, email_verified=None, enabled=None,
                 federation_link=None, first_name=None, last_name=None, realm_id=None, username=None,
                 created_timestamp=None, service_account_client_link=None, not_before=None):
        self.id = id
        self.email = email
        self.email_constraint = email_constraint
        self.email_verified = email_verified
        self.enabled = enabled
        self.federation_link = federation_link
        self.first_name = first_name
        self.last_name = last_name
        self.realm_id = realm_id
        self.username = username
        self.created_timestamp = created_timestamp
        self.service_account_client_link = service_account_client_link
        self.not_before = not_before


    def __repr__(self):
        return '<user_attribute %r %r %r %r %r>' % (self.id, self.username, self.first_name, self.last_name, self.email)

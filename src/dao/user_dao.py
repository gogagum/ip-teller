from sqlalchemy.orm import registry

mapper_registry = registry()

@mapper_registry.mapped
class UserDao:
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    second_name = Column(String)
    known = Column(Bool, nullable=False)

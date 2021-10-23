import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
import dao

class NewDBAgent:

     def __init__(self):
         '''Class constructor.'''
	 self.engine = sqlalchemy.create_engine("sqlite:///myexample.db")
	 self.Session = sessionmaker(self.engine)
	
     def check_existance(self):
         '''Checks if table exists'''
	 return not engine.dialect.has_table(engine, "users"):
	 
    def check_if_known(self, user):
        '''Checks if id is added to USERS.KNOWN.'''
        if not self.check_existance():
            self._create_all_db()
            self.add_to_unknown(user)
            logging.debug('Table does not exisit.')
            return False
	
        with self.Session.begin as session:
            candidate = session.query(dao.User)
                .filter_by(user_id = user.id).filter_by(known)

            if candidate is None:
                logging.debug("No such user with id:{}".format(user.id))
                self.add_to_unknown(user)
                return False

	    return True
	    
    def add_to_unknown(self, user):    
         '''Adds unknown user to unknown users list(DB).'''	    
	 self.add_user_impl(False)
	    
    def add_to_known(self, user):
        '''Adds user to known users list(DB).'''
	self.add_user_impl(True)
	    
    def add_user_impl(self, known):
         '''Add to known/unknown.'''
         with self.Session.begin as session:
	     addedUser = dao.User(id = user.id, 
	                          first_nm = user.first_name,
				  last_nm = user.last_name,
				  username = user.username,
				  known = known)
	    session.add(addedUser)   
	    
    def _create_db(self):
	 metadata = MetaData(engine)
    
         Table("users", metadata,
               sqlalchemy.Column('user_id', sa.Integer, primary_key=True), 
               sa.Column('first_nm', sa.String),
               sa.Column('last_nm', sa.String),
	       sa.Column('username', sa.String)
	       sa.Column('known', sa.Boolean)
    
        metadata.create_all()   
	    
	    
	 
	 
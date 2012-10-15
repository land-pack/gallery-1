from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref, eagerload
from sqlalchemy import (Column, Integer, Unicode, ForeignKey, and_, or_, Date,
                                DateTime, String, Text, Boolean, desc, asc)
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.schema import Table
import sqlalchemy
import datetime
import json

Base = declarative_base()

engine = create_engine('sqlite:////home/ngon2/images.db')
session = scoped_session(sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine))

ticket_tag = Table("image_tag", Base.metadata,
    Column('image_id', Integer, ForeignKey('images.id')),
    Column('tag_id', Integer, ForeignKey('tags.id')),
)

class Images(Base):
    __tablename__ = 'images'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(255), nullable=False)
    url = Column(Unicode(512), nullable=False)
    date = Column(DateTime, nullable = False)
    tags = relationship('Tags', secondary=ticket_tag, backref='images_backref')
    viewcount = Column(Integer, default = 0)
    width = Column(Integer, default = 0)
    height = Column(Integer, default = 0)
    size = Column(Integer, default = 0)
    
    def __repr__(self):
        return self.name

    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.date = datetime.datetime.now()

    def add_tag(self, tagid):
        self.tags.append(tagid)

    def remove_tag(self, tagid):
        try:
            self.tags.remove(tagid)
        except Exception as ex:
            raise ex

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'url': self.url,
            'tags': [tag.id for tag in self.tags],
            'date': self.date,
            'viewcount': self.viewcount,
            'width': self.width,
            'height': self.height,
            'size': self.size,
        }

    @classmethod
    def by_id(cls, img_id): 
        return session.query(Images).filter(Images.id == img_id).first()

    @classmethod
    def by_ids(cls, img_ids):
        return session.query(Images).filter(Images.id.in_(img_ids)).all()

    @classmethod
    def by_tag_id(cls, tag_id):
        return session.query(Images).options(eagerload('tags')).\
                                filter(Images.tags.any(Tags.id == tag_id))

    @classmethod
    def by_tag_ids(cls, tag_ids):
        return session.query(Images).options(eagerload('tags')).\
                                filter(Images.tags.any(Tags.id.in_(tag_ids)))

    @classmethod
    def by_month(cls, month):
        return session.query(Images).filter(sqlalchemy.extract('month',\
                                Images.date) == month)
    @classmethod
    def get_all(cls):
        return session.query(Images).all()

    @classmethod
    def inc_view(cls, img_id):
        img = Images.by_id(img_id)
        img.viewcount += 1
        session.add(img)
        session.commit()
    
    @classmethod
    def create(cls, img_dict):
        img = Images(img_dict['name'], img_dict['url'])
        
        if 'tags' in img_dict:
            for t in img_dict['tags']:
                img.add_tag(Tags.by_id(t))

        if 'date' in img_dict:
            img.date = img_dict['date']

        if 'width' in img_dict:
            img.width = img_dict['width']

        if 'height' in img_dict:
            img.height = img_dict['height']

        if 'size' in img_dict:
            img.size = img_dict['size']
        return img

class Tags(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(255), nullable=False)
    images = relationship("Images", secondary=ticket_tag,
                            backref="tags_backref")

    def __repr__(self):
        return self.name

    def __init__(self, name):
        self.name = name 

    def add_images(self, image):
        self.images.add(image)

    @classmethod
    def by_image_id(self, image_id):
        return session.query(Tags).options(eagerload('images')).\
            filter(Tags.images.any(Images.id == image_id))

    @classmethod
    def by_id(self, tag_id):
        return session.query(Tags).filter(Tags.id == tag_id).first()

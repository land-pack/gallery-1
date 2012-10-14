import sys
import os
import unittest
import logging

from models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

class TestImage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base.metadata.create_all(bind=engine)
        imgs = [Images("img1", "http://1"), Images("img2", "http://2"), 
                    Images("img3", "http://3"),  Images("img4", "http://4"), 
                    Images("img5", "http://5"), ]
        for img in imgs:
            session.add(img)

        tags = [Tags("wallpaper"), Tags("desktop"), Tags("mobile"),]
        for tag in tags:
            session.add(tag)

        imgs[2].add_tag(tags[1])
        imgs[4].add_tag(tags[1])
        imgs[1].add_tag(tags[0])
        imgs[0].add_tag(tags[0])
        imgs[0].add_tag(tags[1])

        session.commit()

    @classmethod
    def tearDownClass(cls):
        session.rollback()
        Base.metadata.drop_all(bind=engine)
        session.close()

    def test_by_id(self):
        img = Images.by_id(1).to_dict()
        self.assertEqual(img['id'], 1)
     
    def test_by_ids(self):
        imgs = [img.to_dict() for img in Images.by_ids([1, 3, 2])]

        img = imgs[0]
        self.assertEqual(img['id'], 1)
        self.assertEqual(img['name'], 'img1')

        img = imgs[1]
        self.assertEqual(img['id'], 2)
        self.assertEqual(img['name'], 'img2')

        img = imgs[2]
        self.assertEqual(img['id'], 3)
        self.assertEqual(img['name'], 'img3')

    def test_tag_by_id(self):
        imgs = [img.to_dict() for img in Images.by_tag_id(2)]
        id_list = [t['id'] for t in imgs]
        self.assertEqual(id_list, [1, 3, 5])
        
        imgs = [img.to_dict() for img in Images.by_tag_id(1)]
        id_list = [t['id'] for t in imgs]
        self.assertEqual(id_list, [1, 2,])

    def test_tag_by_ids(self):
        imgs = [img.to_dict() for img in Images.by_tag_ids([1, 2])]
        id_list = [t['id'] for t in imgs]
        self.assertEqual(id_list, [1, 2, 3, 5])

    def test_by_month(self):
        imgs = [img.to_dict() for img in Images.by_month(10)]
        id_list = [t['id'] for t in imgs]
        self.assertEqual(id_list, [1, 2, 3, 4, 5])

    def test_create(self):
        img_dict = {
            'name': 'testimg',
            'url': 'http://abc',
            'width': 800,
            'height': 600,
            'tags': [1, 2],
        }
        img = Images.create(img_dict)
        
        self.assertEqual(img.width, 800)
        self.assertEqual(img.height, 600)

if __name__ == "__main__":
    unittest.main()

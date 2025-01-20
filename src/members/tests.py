from django.test import TestCase,Client
from django.contrib.auth.models import User
import datetime
from . import api_views, models


def get_token():
    admin=User.objects.create_user(username="testerAdmin",password="admin", is_superuser=True)
    c=Client()
    response=c.post("/api/auth/token/login/",{"username":"testerAdmin","password":"admin"})
    return response.json()["auth_token"]

class AuthTestCase(TestCase):
    def test_account_token(self):
        admin=User.objects.create_user(username="testerAdmin",password="admin", is_superuser=True)
        c=Client()
        response=c.post("/api/auth/token/login/",{"username":"testerAdmin","password":"admin"})
        print("token:",response.json()["auth_token"])
        self.assertEqual(response.status_code,200)
        

class MemberTagTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        for i in range(0,30):
            models.MemberTag.objects.create(title="test"+str(i+1))
        return super(MemberTagTestCase, cls).setUpClass()
        
    def test_tag_queryset(self):
        tags=api_views.MemberTagViewset().get_queryset()
        if len(tags)!=30:
            self.fail("incorrect number of tags created, needed "+str(30)+"created "+str(len(tags)))
        self.assertEqual(tags[0].title,"test1")
        self.assertEqual(tags[1].title,"test2")
    
    def test_tag_pagination(self):
        token=get_token()
        c=Client(HTTP_AUTHORIZATION="Token "+token)
        response=c.get("/api/v1/tags/", headers={"Accept": "*/*"},query_params={"page":1})
        self.assertEqual(response.status_code,200)
        self.assertEqual(int(response.json()["count"]),20)
        response=c.get("/api/v1/tags/", headers={"Accept": "*/*"},query_params={"page":2})
        self.assertEqual(response.status_code,200)
        self.assertEqual(int(response.json()["count"]),10)


class MemberTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        for i in range(0,30):
            models.Member.objects.create(name="test"+str(i+1), lastname="test"+str(i+1), date_of_birth=datetime.date.today())
        return super(MemberTestCase, cls).setUpClass()
        
    def test_member_queryset(self):
        members=api_views.MemberViewset().get_queryset()
        if len(members)!=30:
            self.fail("incorrect number of members created, needed "+str(30)+"created "+str(len(members)))
        self.assertEqual(members[0].name,"test1")
        self.assertEqual(members[1].name,"test2")
    
    def test_member_pagination(self):
        token=get_token()
        c=Client(HTTP_AUTHORIZATION="Token "+token)
        response=c.get("/api/v1/members/", headers={"Accept": "*/*"},query_params={"page":1})
        self.assertEqual(response.status_code,200)
        self.assertEqual(int(response.json()["count"]),20)
        response=c.get("/api/v1/members/", headers={"Accept": "*/*"},query_params={"page":2})
        self.assertEqual(response.status_code,200)
        self.assertEqual(int(response.json()["count"]),10)

# Create your tests here.

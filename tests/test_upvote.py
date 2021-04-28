import unittest
from app.models import Pitch, Upvote,User


class UpvoteModelTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the class
    """

    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.user_Vee = User(username='zeluuhyne', password='banana', email='zeluuhyne@ms.com')  
        self.pitch_vee = Pitch(title='love', pitch='This is the ghetto', category='Event', user=self.user_Vee)
        self.upvote_vee = Upvote(upvote='2',pitch=self.pitch_vee,user=self.user_Vee) 
    def tearDown(self):
        Upvote.query.delete()
        Pitch.query.delete()
        User.query.delete()
    def test_instance(self):
        self.assertTrue(isinstance(self.upvote_vee, Upvote))

    def test_check_instance_variables(self):
        self.assertEquals(self.upvote_vee.upvote, '2')
        self.assertEquals(self.upvote_vee.user, self.user_Vee)
        self.assertEquals(self.upvote_vee.pitch, self.pitch_vee)

    def test_save_upvote(self):
        self.upvote_vee.save()
        self.assertTrue(len(Upvote.query.all()) > 0)

       

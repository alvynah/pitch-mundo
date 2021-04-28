import unittest
from app.models import Pitch, Downvote,User


class DownvoteModelTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the class
    """

    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.user_Vee = User(username='zeluuhyne', password='banana', email='zeluuhyne@ms.com')  
        self.pitch_vee = Pitch(title='love', pitch='This is the ghetto', category='Event', user=self.user_Vee)
        self.downvote_vee = Downvote(downvote='8',pitch=self.pitch_vee,user=self.user_Vee) 
    def tearDown(self):
        Downvote.query.delete()
        Pitch.query.delete()
        User.query.delete()
    def test_instance(self):
        self.assertTrue(isinstance(self.downvote_vee, Downvote))

    def test_check_instance_variables(self):
        self.assertEquals(self.downvote_vee.downvote, '8')
        self.assertEquals(self.downvote_vee.user, self.user_Vee)
        self.assertEquals(self.downvote_vee.pitch, self.pitch_vee)

    def test_save_upvote(self):
        self.downvote_vee.save()
        self.assertTrue(len(Downvote.query.all()) > 0)

       

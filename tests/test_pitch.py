import unittest
from app.models import Pitch,User


class PitchModelTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the class
    """

    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.user_Vee = User(username='reinyheny', password='banana', email='reinyheny@ms.com')
        self.pitch = Pitch(title='Monday', pitch='This is the ghetto', category='Event',user=self.user_Vee)

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.pitch, Pitch))

    def test_check_instance_variables(self):
        self.assertEquals(self.pitch.title, 'Monday')
        self.assertEquals(self.pitch.pitch, 'This is the ghetto')
        self.assertEquals(self.pitch.category, 'Event')
        self.assertEquals(self.pitch.user, self.user_Vee)

    def test_save_pitch(self):
        self.pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all()) > 0)

    # def test_get_pitch_by_title(self):
    
    #     got_pitches = Pitch.get_pitches('Monday')
    #     self.assertTrue(len(got_pitches) == 1)

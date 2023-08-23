from unittest import *
from Business.Repositories.EloRatingRepository import EloRatingRepository

class EloRepositoryTest(TestCase):
    def setUp(self):
        self.elo_repository = EloRatingRepository()

    def tearDown(self):
        self.elo_repository = None

    def test_get_adjusted_elo_ratings(self):

        w = 1700
        l = 2000
        t = 4/5

        normal_w,normal_l  = self.elo_repository.get_elo_ratings(w,l)
        print(normal_w,normal_l)


        new_w,new_l = self.elo_repository.adjust_elo_rating_for_functions(w,l,t)
        print(new_w,new_l)
import requests
from getpass import getpass

from exercises_utils.exercise import Exercise

class User:
    """
    Class for representing a user.
    """
    
    logged_in = False
    
    def __init__ (self) -> None:
        """
        Constructor.
        
        :param id: a unique identifier for the user - used in the db to keep track of each user's score
        """
        
        self.email = input("Email: ")
        self.password = getpass("Password: ")
        
        resp = requests.get(
            "https://api.ai-world-school.com/api/grader/check-user",
            # "http://localhost:8080/api/grader/check-user",
            params = {
                "email": self.email,
                "password": self.password
            }
        )
        
        data = resp.json()
        
        if not data['isValid']:
            raise Exception(data['error']['message'])
        
        self.logged_in = True
        print('Successfully logged in!')
        
    def submit(self, exercise: Exercise, _locals: dict) -> None:
        """
        Submits an exercise.
        
        :param exercise: the exercise to be submitted
        :param _locals: all variables set inside the jupyter notebook
        """
        
        if not self.logged_in:
            raise Exception('User must be logged in to submit an exercise.')
        
        # check the exercise
        score = exercise._check(_locals)
        
        # update the user's score
        self._update_score(exercise, score)
        
    def _update_score(self, exercise: Exercise, score: int) -> None:
        """
        Updates the user's score on db.
        
        :param exercise: the exercise that was submitted
        :param points: the score to be added to the user's score
        """
        
        if not self.logged_in:
            raise Exception('User must be logged in to submit an exercise.')
        
        print('id: ', exercise.id)
        
        resp = requests.get(
            "https://api.ai-world-school.com/api/grader/update-score",
            params = {
                "email": self.email,
                "password": self.password,
                "exercise_id": exercise.id,
                "exercise_total_score": exercise.total_score,
                "score": score
            }
        )
        
        data = resp.json()
        
        if data['error']:
            raise Exception(data['error']['message'])
        
        print('Successfully updated score!')
    
    
# debug
# if __name__ == "__main__":
#     user = User()
#     exercise = Exercise("1", 10)
#     user.submit(exercise)
#     print(user.score)
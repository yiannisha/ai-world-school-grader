from abc import ABCMeta, abstractmethod

class Exercise (ABCMeta):
    """
    Class for representing an exercise.
    """
    
    @property
    @abstractmethod
    def id(self) -> str:
        """
        Exercise's id.
        """
        pass
    
    @property
    @abstractmethod
    def total_score(self) -> int:
        """
        Exercise's total score.
        """
        pass
    
    @abstractmethod
    def _get_exercises(self, _locals: dict) -> list[bool]:
        """
        Returns the exercises.
        """
        pass
    
    @classmethod
    def _check(self) -> int:
        """
        Checks the exercise.
        Returns the score.
        """
        score = 0
        results = {}
        
        # get local variables
        _locals = globals()
        print('globals: ', _locals)
        
        for index, exercise in enumerate(self._get_exercises(self, _locals)):
            try:
                results[index + 1] = eval(exercise)
            except KeyError as e:
                print('error: ', e)
                results[index + 1] = False
                
            if results[index + 1]:
                score += 1
        
        if score == self.total_score:
            print('All exercises passed!')
        else:
            for exercise, result in results.items():
                if not result:
                    print(f'Exercise {exercise} failed. Try again and resubmit.')
    
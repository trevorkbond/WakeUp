from abc import ABC, abstractmethod

class ChallengeGetter(ABC):
    @abstractmethod
    def get_challenge(self) -> str:
        pass
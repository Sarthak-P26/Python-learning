class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)
            
    def next_question(self):
        # Safety check to avoid IndexError
        if self.question_number >= len(self.question_list):
            return

        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_input = input(f"Q.{self.question_number} {current_question.text} (True/False): ")
        self.check_answer(user_input, current_question.answer)
    
    def check_answer(self, user_input, correct_answer):
        if user_input.lower() == correct_answer.lower():  # Fixed .lower()
            self.score += 1
            print("You guessed the correct answer.")
        else:
            print("This's wrong")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
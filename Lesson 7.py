class CourtCase:
    def __init__(self, case_number: str):
        # номер дела передается в качестве аргумента при создании экземпляра и сохраняется в атрибут self.case_number
        self.case_number = case_number

        # список участников дела по умолчанию пустой и сохраняется в атрибут self.case_participants
        self.case_participants = []

        # список дат судебных заседаний по умолчанию пустой и сохраняется в атрибут self.listening_datetimes
        self.listening_datetimes = []

        # статус дела по умолчанию False, означает, что дело еще не завершено, сохраняется в атрибут self.is_finished
        self.is_finished = False

        # вердикт по умолчанию пустой строкой и сохраняется в атрибут self.verdict
        self.verdict = ""

    def set_a_listening_datetime(self, listening_datetime: str) -> None:
        # добавляем переданный параметр в конец списка self.listening_datetimes
        self.listening_datetimes.append(listening_datetime)

    def add_participant(self, participant: str) -> None:
        # добавляем переданный параметр в конец списка self.case_participants
        self.case_participants.append(participant)

    def remove_participant(self, participant: str) -> None:
        # проверяем, что передаваемый параметр содержится в списке участников
        if participant in self.case_participants:
            # если содержится, то удаляем его из self.case_participants
            self.case_participants.remove(participant)

    def make_a_decision(self, verdict: str) -> None:
        # присваиваем переданный параметр атрибуту self.verdict
        self.verdict = verdict
        # устанавливаем атрибут self.is_finished в значение True
        self.is_finished = True
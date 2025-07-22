import datetime
from typing import List, Dict, Set

class LegalCase:
    def __init__(self, case_id: str, client_name: str, case_type: str, priority: int, deadline: int):
        self.case_id = case_id
        self.client_name = client_name
        self.case_type = case_type
        self.priority = priority
        self.deadline = datetime.datetime.strptime(deadline, "%d-%m-%Y")
        self.documents = set[str] = set()

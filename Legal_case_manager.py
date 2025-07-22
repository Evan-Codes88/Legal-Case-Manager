# Legal Case Management System
# A Python project to demonstrate data structures, problem-solving, and legal tech application

import datetime
from typing import List, Dict, Set

class LegalCase:
    def __init__(self, case_id: str, client_name: str, case_type: str, priority: int, deadline: str):
        self.case_id = case_id
        self.client_name = client_name
        self.case_type = case_type
        self.priority = priority  # 1 (high) to 3 (low)
        self.deadline = datetime.datetime.strptime(deadline, "%Y-%m-%d")
        self.documents: Set[str] = set()  # Set to store unique document IDs

    def add_document(self, doc_id: str) -> None:
        """Add a document to the case, ensuring no duplicates."""
        self.documents.add(doc_id)
        print(f"Document {doc_id} added to case {self.case_id}")

    def __str__(self) -> str:
        return f"Case {self.case_id}: {self.client_name} ({self.case_type}), Priority: {self.priority}, Deadline: {self.deadline.date()}"

class CaseManager:
    def __init__(self):
        self.cases: Dict[str, LegalCase] = {}  # Dictionary to store cases by case_id
        self.case_types: Set[str] = set()  # Set to track unique case types

    def add_case(self, case: LegalCase) -> None:
        """Add a new case to the manager."""
        if case.case_id in self.cases:
            print(f"Case {case.case_id} already exists!")
            return
        self.cases[case.case_id] = case
        self.case_types.add(case.case_type)
        print(f"Case {case.case_id} added successfully.")

    def get_cases_by_priority(self, priority: int) -> List[LegalCase]:
        """Return cases filtered by priority, sorted by deadline."""
        filtered_cases = [case for case in self.cases.values() if case.priority == priority]
        return sorted(filtered_cases, key=lambda x: x.deadline)

    def get_overdue_cases(self) -> List[LegalCase]:
        """Return cases past their deadline."""
        today = datetime.datetime.now()
        return [case for case in self.cases.values() if case.deadline < today]

    def get_case_summary(self) -> Dict[str, int]:
        """Generate a summary of cases by type."""
        summary = {}
        for case in self.cases.values():
            summary[case.case_type] = summary.get(case.case_type, 0) + 1
        return summary

    def search_case_by_client(self, client_name: str) -> List[LegalCase]:
        """Search cases by client name (case-insensitive partial match)."""
        return [case for case in self.cases.values() if client_name.lower() in case.client_name.lower()]

def main():
    # Initialize the case manager
    manager = CaseManager()

    # Sample data to demonstrate functionality
    sample_cases = [
        LegalCase("CASE001", "John Doe", "Contract Dispute", 1, "2025-08-01"),
        LegalCase("CASE002", "Jane Smith", "IP Litigation", 2, "2025-07-15"),
        LegalCase("CASE003", "Acme Corp", "Contract Dispute", 3, "2025-09-01"),
        LegalCase("CASE004", "John Adams", "Compliance", 1, "2025-07-10"),
    ]

    # Add sample cases
    for case in sample_cases:
        manager.add_case(case)

    # Add documents to a case
    sample_cases[0].add_document("DOC001")
    sample_cases[0].add_document("DOC002")

    # Demonstrate functionality
    print("\nHigh Priority Cases (Priority 1):")
    for case in manager.get_cases_by_priority(1):
        print(case)

    print("\nOverdue Cases:")
    for case in manager.get_overdue_cases():
        print(case)

    print("\nCase Summary by Type:")
    summary = manager.get_case_summary()
    for case_type, count in summary.items():
        print(f"{case_type}: {count} case(s)")

    print("\nSearch for cases with client 'John':")
    for case in manager.search_case_by_client("John"):
        print(case)

if __name__ == "__main__":
    main()
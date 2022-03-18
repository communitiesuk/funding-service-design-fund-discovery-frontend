from dataclasses import dataclass
from datetime import datetime


@dataclass
class Rounds:
    """_summary_  rounds class for rounds data
    alteration

    Returns:
        Altered simplified rounds data
    """

    fund_id: str
    round_title: str
    round_id: str
    eligibility_criteria: dict
    opens: datetime
    deadline: datetime
    application_url: str

    @staticmethod
    def fund_rounds(fund_round):
        """Function is used for data alteration
        from class Rounds

        Args:
            fund_round is used as for loop attribute.

        Returns:
            Function return rounds data
        """
        return Rounds(
            fund_id=fund_round.get("fund_id"),
            round_title=fund_round.get("round_title"),
            round_id=fund_round.get("round_id"),
            eligibility_criteria=fund_round.get("eligibility_criteria"),
            opens=fund_round.get("opens"),
            deadline=fund_round.get("deadline"),
            application_url=fund_round.get("application_url"),
        )

    @property
    def opens_formatted(self):
        """
        GIVEN function is to alter the datetime string object
        for self.opens for human readability.
        """
        return datetime.strptime(self.opens, "%Y-%m-%dT%H:%M:%S").strftime(
            "%Y-%m-%d"
        )

    @property
    def deadline_formatted(self):
        """
        GIVEN function is to alter the datetime string object
        for self.deadline for human readability.
        """
        return datetime.strptime(self.deadline, "%Y-%m-%dT%H:%M:%S").strftime(
            "%Y-%m-%d"
        )

    @property
    def eligibility_criteria_formatted(self):
        """_summary_ Function formats numbers(cost) with comma separated integer

        Returns:
            Comma separated integers
        """
        return "{:,}".format(self.eligibility_criteria["max_project_cost"])

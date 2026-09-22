from services.ai_service import AIService


class TravelPlanner:

    def __init__(self):
        self.ai = AIService()

    def create_plan(self, destination, days, budget):

        prompt = f"""Create a travel plan.

        Destination:
        {destination}

        Days:
        {days}

        Budget:
        {budget}

        Include:

        1. Day wise itinerary

        2. Top attractions

        3. Food recommendations

        4. Packing checklist

        5. Budget saving tips

        Format nicely.
        """

        return self.ai.ask(prompt)

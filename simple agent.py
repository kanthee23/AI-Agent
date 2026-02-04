class SimpleAgent:
    def __init__(self):
        self.memory = []


    def perceive(self, user_input):
        """Process input"""
        return user_input.lower()
    

    def reason(self, processed_input):
        """Make decision based rule"""
        responses = {
            "hellow": "Hi there, How can i help you",
            "how are you": "I'm cool, because i am just code",
            "what is your name": "I am Simple Agent",
            "bye": "Goodbye! Have a grate day"
        }

        for key in responses:
            if key in processed_input:
                return responses[key]
            
        return "I don't understand, Data not enough!"
    
    def act(self, response):
        """Generate output"""
        print(f"Agent:{response}")
        return response
    
    def run(self):
        """Main loop"""
        print("Simple agent activated, Type quit to stop.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == "quit":
                break

            processed = self.perceive(user_input)
            decision = self.reason(processed)
            self.act(decision)
            self.memory.append((user_input, decision))


if __name__ == "__main__":
    agent = SimpleAgent()
    agent.run()

    



        
    
    

    
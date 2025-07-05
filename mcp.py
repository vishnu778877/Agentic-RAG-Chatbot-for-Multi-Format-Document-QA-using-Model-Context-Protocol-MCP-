class MCPMessage:
    def __init__(self, sender, receiver, msg_type, trace_id, payload):
        self.sender = sender
        self.receiver = receiver
        self.type = msg_type
        self.trace_id = trace_id
        self.payload = payload

class MCPBus:
    def __init__(self):
        self.handlers = {}

    def register(self, agent_name, handler):
        self.handlers[agent_name] = handler

    def send(self, message: MCPMessage):
        if message.receiver in self.handlers:
            self.handlers[message.receiver](message)

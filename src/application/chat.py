
class ChatUseCase:
    def __init__(self, llm_client, executor):
        self.llm = llm_client
        self.executor = executor


    def execute(self, message: str):
        raw = self.llm.generate(message)

        if isinstance(raw, dict):
           return raw
        try:
            import json
            clean = raw.replace("```json", "").replace("```", "").strip()
            return json.loads(clean)
        except:
            return {"text": raw}
import requests

class ActionExecutor:
    def __init__(self, base_url):
        self.base_url = base_url

    def execute_action(self, actions:list):
        for action in actions:
            tool = action.get("tools")
            args = action.get("args", {})

            if tool == "movement":
                url = self.base_url + args.get("endpoint", "")
                requests.request(method=args.get("method", "POST"), url=url, json=args.get("body", {}))

        
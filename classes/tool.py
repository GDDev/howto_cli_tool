from data.db_tool import ToolDatabase

class Tool:

    db_tool = ToolDatabase()

    def __init__(self, name, title, usage, category, description):
        self.id
        self.name = name
        self.title = title
        self.usage = usage
        self.category = category
        self.description = description
        self.flag_list

    def __init__(self, name, usage):
        self.name = name
        self.usage = usage
        self.flag_list

    def find_tool(name, title, usage, category, description, flag_list):
        tool = Tool(name, title, usage, category, description, flag_list)
        return tool

    def get_tool_usage(self):
        return self.usage
    
    def get_tool_description(self):
        return self.description
    
    def get_tool(self):
        return self

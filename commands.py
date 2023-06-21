import json

# Tool's functions
def get_tool(data):
    return f"Example syntax: {data['usage']}"

def describe_tool(data):
    return f""

def get_all(data):
    all_info = f"What is {data['name']}?\n{data['description']}\n\n***{data['title']}***\nUse the syntax as follows:\n`{data['usage']}`\n\nWhich are the available flags?\n"
    for flag in data["flags"]:
        all_info += f"  {flag['flag']}: {flag['description']}\n"
    all_info += f"\n{data['name']} is under the category of {data['category']}"
    return all_info

# Techniques functions
def get_tech_tool(data, tool):
    return f"{data['tools']['name' == tool]['usage']}"


def get_tool_info(tool_str, data):
    for tool in data.get("tools", []):
        if tool["name"].lower() == tool_str.lower():
            output_dict = {"usage": tool["usage"]}
            if "description" in tool:
                output_dict["description"] = tool["description"]
            return output_dict
    return {}


def get_tags_info(data, tool_str=None):
    flags = data.get("flags", [])
    if tool_str:
        flags = [t for t in flags if t["name"].lower() == tool_str.lower()]
    output_list = []
    for flag in flags:
        output_dict = {"flag": flag["name"]}
        if "description" in flag:
            output_dict["description"] = flag["description"]
        output_list.append(output_dict)
    return output_list
    
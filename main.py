import sys
import os.path
import json
from commands import *

        
def main():
    # Get input from user
    if len(sys.argv) < 2:
        print("Usage: python main.py <tool or technique> [-t <tool>] [-d or -a]")
        sys.exit(1)
    howto = sys.argv[1].lower()
    if len(sys.argv) > 2:
        if (not sys.argv[2].startswith('-')):
            howto += f"-{sys.argv[2]}"

    # Check for flags
    flags = {}
    for i in range(2, len(sys.argv)):
        if sys.argv[i] in ["-a", "--all"]:
            flags["all"] = True
        elif sys.argv[i] in ["-d", "--describe"]:
            flags["describe"] = True
        if sys.argv[i] in ["-t", "--tool"]:
            flags["tool"] = sys.argv[i+1]
        
    # Check if input is a tool or a technique
    tool_or_technique(howto, flags)
    

def tool_or_technique(howto, flags):
    tool_path = f"data/tools/{howto}.json"
    technique_path = f"data/techniques/{howto}.json"
    if os.path.isfile(tool_path):
        with open(tool_path) as tool_file:
            tool_data = json.load(tool_file)
            if flags:
                if "all" in flags:
                    print(get_all(tool_data))
                elif "describe" in flags:
                    print(describe_tool(tool_data))
                else:
                    print(f"Sorry, it seems like you have typed a invalid flag")
            else:
                print(get_tool(tool_data))
    elif os.path.isfile(technique_path):
        with open(technique_path) as technique_file:
            technique_data = json.load(technique_file)
            if flags:
                if "tool" in flags:
                    print(get_tech_tool(technique_data, flags["tool"]))
                else:
                    print(f"Sorry, it seems like you have typed a invalid flag")
            else:
                print(technique_data["tools"][0]["usage"])
    else:
        print(f"Sorry, I couldn't find any information on {howto}")
        sys.exit(1)


if __name__ == "__main__":
    main()


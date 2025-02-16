import json
with open("sample-data.json", "r") as f:
    data = json.load(f)
print("Interface status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<15} {'Speed':<10} {'MTU':<10}")
print("-" * 80)
for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]  
    description = attributes.get("description", "inherit")  
    speed = attributes.get("speed", "N/A")  
    mtu = attributes.get("mtu", "N/A")  

    print(f"{dn:<50} {description:<15} {speed:<10} {mtu:<10}")
import  random

def generate_random_ip():
    """Function para makapag generate ng random ip address."""
    return f"192.168.1.{random.randint(0, 20)}"

def check_firewall_rules(ip, rules):
    """Function if yung ip is match dun sa firewall rules natin."""
    for rule_ip, action in rules.items():
        if ip == rule_ip:
            return action
    return "allow"  # Default action if walang mag mamatch

def main():
    # Malicious firewall rules (key: IP address, value: action)
    firewall_rules = {
        "192.168.1.1": "block",
        "192.168.1.4": "block",
        "192.168.1.9": "block",
        "192.168.1.13": "block",
        "192.168.1.16": "block",
        "192.168.1.19": "block"
    }

      # for network test ito!
    for _ in range(20):
     ip_address = generate_random_ip()
     action = check_firewall_rules(ip_address, firewall_rules)
     random_number = random.randint(0, 9999)
     print(f"IP: {ip_address}, Action: {action}, Random: {random_number}")

if __name__ == "__main__":
    main()
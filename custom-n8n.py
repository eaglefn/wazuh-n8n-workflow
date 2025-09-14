#!/var/ossec/framework/python/bin/python3
# /var/ossec/integrations/custom-n8n.py

import sys, json, requests

def get_path(obj, path):
    """Einfacher Dot-Pfad-Getter: 'rule.mitre.id' -> obj['rule']['mitre']['id']"""
    cur = obj
    for part in path.split('.'):
        if isinstance(cur, dict) and part in cur:
            cur = cur[part]
        else:
            return None
    return cur

def to_scalar(v):
    # n8n-freundlich: Listen zu Komma-Strings
    if isinstance(v, list):
        return ",".join(str(x) for x in v)
    return v

# Args vom Integrator: [1]=alert_file, [2]=user:pass (optional), [3]=hook_url
alert_file = sys.argv[1]
hook_url   = sys.argv[3]

with open(alert_file, "r", encoding="utf-8") as f:
    alert = json.loads(f.read())

# Wunschfelder (du kannst die Liste beliebig erweitern)
wanted_paths = [
    # Quelle/Agent
    "agent.name", "agent.id", "agent.ip",
    # IP/Quelle (je nach Decoder kann srcip unterschiedlich heißen)
    "data.srcip", "data.src_ip", "srcip", "source.ip",
    # Regel & Beschreibung
    "rule.id", "rule.description",
    # MITRE
    "rule.mitre.id", "rule.mitre.technique", "rule.mitre.tactic",
]

fields = {}
for p in wanted_paths:
    v = get_path(alert, p)
    if v is not None:
        fields[p.replace(".", "_")] = to_scalar(v)

payload = {
    "alert": alert,   # vollständiges Original-Alert für spätere Analysen in n8n
    "fields": fields  # flache, gut weiterverarbeitbare Teilmenge
}

resp = requests.post(hook_url, json=payload, timeout=10)
resp.raise_for_status()

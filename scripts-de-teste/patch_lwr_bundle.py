# Python port of sf-skills service-digital-engagement-messaging-site-integrate/scripts/patch_lwr_bundle.sh
# Usage: python -I patch_lwr_bundle.py <site-dir> <deploymentName> <scrtUrl> <siteEndpoint>
import json, sys, uuid
from pathlib import Path

site_dir, deployment, scrt, endpoint = sys.argv[1:5]
MSG = "experience_messaging:embeddedMessaging"
ATTRS = {"deploymentName": deployment, "scrtUrl": scrt, "siteEndpoint": endpoint,
         "isExpSiteAuthMode": False, "hideChatButtonOnLoad": "Default", "clientVersion": "WebV2"}

def has_messaging(n):
    if isinstance(n, list):
        return any(has_messaging(x) for x in n)
    if isinstance(n, dict):
        return n.get("definition") == MSG or has_messaging(n.get("children") or [])
    return False

def update_messaging(n):
    if isinstance(n, list):
        for x in n:
            update_messaging(x)
    elif isinstance(n, dict):
        if n.get("definition") == MSG:
            n["attributes"] = dict(ATTRS)
        elif isinstance(n.get("children"), list):
            update_messaging(n["children"])

def patch_footer(footer):
    children = footer.setdefault("children", [])
    if has_messaging(children):
        update_messaging(children)
        return
    node = {"id": str(uuid.uuid4()), "type": "component", "definition": MSG, "attributes": dict(ATTRS)}
    section = next((c for c in children if c.get("type") == "component" and c.get("definition") == "community_layout:section"), None)
    if section is None:
        children.append(node)
        return
    region = next((c for c in section.get("children") or [] if c.get("type") == "region"), None)
    if region is None:
        section.setdefault("children", []).append(node)
    else:
        region.setdefault("children", []).append(node)

patched = 0
for f in sorted(Path(site_dir, "sfdc_cms__themeLayout").glob("*/content.json")):
    data = json.loads(f.read_text(encoding="utf-8"))
    for child in data.get("contentBody", {}).get("component", {}).get("children") or []:
        if child.get("type") == "region" and child.get("name") == "footer":
            patch_footer(child)
    f.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    footers = [c for c in data["contentBody"]["component"].get("children") or [] if c.get("name") == "footer"]
    count = sum(json.dumps(c).count(MSG) for c in footers)
    print(f"{f.parent.name}: messaging components in footer = {count}")
    patched += count > 0
print("patched layouts:", patched)
sys.exit(0 if patched else 1)

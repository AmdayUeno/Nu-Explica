# Applies the approved Nu Explica design to the LWR site bundle (idempotent).
import json, sys, uuid
from pathlib import Path

site = Path(sys.argv[1])

def load(rel):
    return json.loads((site / rel).read_text(encoding="utf-8"))

def save(rel, data):
    (site / rel).write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# 0. Public access (Experience Builder: "Public can access the site")
s = load("sfdc_cms__site/Nu_Explica1/content.json")
s["contentBody"]["authenticationType"] = "AUTHENTICATED_WITH_PUBLIC_ACCESS_ENABLED"
save("sfdc_cms__site/Nu_Explica1/content.json", s)

# 1a. Head markup: page title + DM Sans from Google Fonts
FONT_TAGS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
    '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&display=swap">\n'
)
a = load("sfdc_cms__appPage/mainAppPage/content.json")
head = a["contentBody"]["headMarkup"].replace("<title>Welcome to LWC Communities!</title>", "<title>Nu Explica</title>")
if "fonts.googleapis.com" not in head:
    head = head.replace("<title>Nu Explica</title>", "<title>Nu Explica</title>\n" + FONT_TAGS, 1)
a["contentBody"]["headMarkup"] = head
save("sfdc_cms__appPage/mainAppPage/content.json", a)

# 1b. Branding set (theme panel)
FONT = "DM Sans"
b = load("sfdc_cms__brandingSet/Build_Your_Own_LWR/content.json")
v = b["contentBody"]["values"]
v.update({
    "PrimaryAccentColor": "#820AD1", "PrimaryAccentForegroundColor": "#FFFFFF",
    "_PrimaryAccentColor1": "#6A08AB", "_PrimaryAccentColor2": "#520685", "_PrimaryAccentColor3": "#3A045E",
    "TextColor": "#1F0A2E", "_TextColor1": "#1F0A2E", "_TextColor2": "#1F0A2E", "_TextColor3": "#1F0A2E",
    "BackgroundColor": "#FFFFFF", "_BackgroundColor1": "#F7F0FD", "_BackgroundColor2": "#E4D4F2", "_BackgroundColor3": "#4A3858",
    "_NeutralColor": "#E4D4F2", "_NeutralColor1": "#E4D4F2", "_NeutralColor2": "#C9B3DD", "_NeutralColor3": "#4A3858",
    "BaseFont": FONT, "BodyFont": FONT, "BodySmallFont": FONT, "ButtonFont": FONT,
    "BodySmallTextColor": "#4A3858",
    "ButtonBorderRadius": "999px", "ButtonSmallBorderRadius": "999px", "ButtonLargeBorderRadius": "999px",
    "ButtonFontWeight": "500",
})
for key in list(v):
    if key.startswith("Heading") and key.endswith("Font"):
        v[key] = FONT
    if key.startswith("Heading") and key.endswith("FontWeight"):
        v[key] = "700"
save("sfdc_cms__brandingSet/Build_Your_Own_LWR/content.json", b)

# 2. Home view: replace the "Start Building Your Page" placeholder with the custom page component
h = load("sfdc_cms__view/home/content.json")
root = h["contentBody"]["component"]
content = next(r for r in root["children"] if r.get("name") == "content")
if not any(c.get("definition") == "c:nuExplicaHome" for c in content["children"]):
    content["children"] = [{
        "attributes": {},
        "definition": "c:nuExplicaHome",
        "id": str(uuid.uuid4()),
        "type": "component",
    }]
hidden = next(r for r in root["children"] if r.get("name") == "sfdcHiddenRegion")
for c in hidden["children"]:
    if c.get("definition") == "community_builder:seoAssistant":
        c["attributes"]["pageTitle"] = "Nu Explica"
        c["attributes"]["description"] = "Investimentos explicados do zero, sem jargão. Protótipo educativo com IA."
save("sfdc_cms__view/home/content.json", h)
print("site design applied")

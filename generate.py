import os
import gifos

# Authenticate the API call
os.environ["GITHUB_TOKEN"] = os.getenv("GITHUB_TOKEN", "")

# 1. Initialize a large terminal window for the full dashboard
t = gifos.Terminal(width=850, height=450, xpad=15, ypad=15)

# 2. Boot Sequence Header (\x1b[32m applies the Nostromo green)
t.gen_text(text="\x1b[32mSYSTEM LOGIN: ESTEBAN TATO-BARCIA\x1b[0m", row_num=1)
t.gen_text(text="\x1b[32m=================================================\x1b[0m", row_num=2)

# 3. Safely bypass the library's internal division bug to fetch repos
try:
    stats = gifos.utils.fetch_github_stats(user_name="TatoNomic")
    repos = stats.public_repos
except Exception:
    repos = "SECURE_NODE"

# 4. Construct the custom ASCII Neofetch layout
neofetch_layout = [
    f"\x1b[32m      ___       ROLE    : Deputy Research Coordinator (GLAD-MHG)\x1b[0m",
    f"\x1b[32m    _/___\_     NODE    : King's College London (Part-Time PhD)\x1b[0m",
    f"\x1b[32m   /'_ `_ `_\   DOMAIN  : Genomics, Speech AI, ML Pipelines\x1b[0m",
    f"\x1b[32m  | | | | | | | STACK   : Python / R / Bash\x1b[0m",
    f"\x1b[32m  \_|_|_|_|_|_/ SAMPLES : EDTA Plasma & DNA Processing\x1b[0m",
    f"\x1b[32m     \_|_|_/    REPOS   : {repos}\x1b[0m",
    f"\x1b[32m      `\"\"\"`     STATUS  : OPTIMAL\x1b[0m"
]

for i, line in enumerate(neofetch_layout, start=4):
    t.gen_text(text=line, row_num=i)

# 5. Add the blinking terminal cursor at the bottom
t.gen_text(text="\x1b[32m> \x1b[0m", row_num=13, contin=True)

# 6. Generate the final output.gif file locally
t.gen_gif()

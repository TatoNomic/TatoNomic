import gifos
import sys

try:
    # Initialize terminal with dimensions suited for a neofetch block
    t = gifos.Terminal(width=850, height=600, xpad=15, ypad=15)

    # 1. Simulate the Nostromo boot sequence
    t.gen_text(text="\x1b[32m> WEYLAND-YUTANI CORP: MU-TH-UR 6000\x1b[0m", row_num=1)
    t.gen_text(text="\x1b[32m> SYSTEM MOUNTED. STATUS: OPTIMAL\x1b[0m", row_num=2)
    t.gen_text(text="\x1b[32m> run neofetch --profile tato_esteban\x1b[0m", row_num=4)

    # 2. Securely fetch your live GitHub stats
    try:
        github_stats = gifos.utils.fetch_github_stats(user_name="TatoNomic")
        repos = github_stats.public_repos
        commits = github_stats.total_contributions
    except Exception:
        repos = "SECURE"
        commits = "ENCRYPTED"

    # 3. Build the custom glowing green ASCII Neofetch
    neofetch_lines = [
        "\x1b[32m        ___       ESTEBAN TATO-BARCIA @ TatoNomic\x1b[0m",
        "\x1b[32m      __\_/__     -------------------------------\x1b[0m",
        "\x1b[32m    /'_ `_ `_`\   Role    : Deputy Research Coordinator (GLAD-MHG)\x1b[0m",
        "\x1b[32m   | | | | | | |  Domain  : Genomics, Speech AI, ML Pipelines\x1b[0m",
        "\x1b[32m   \_|_|_|_|_|_/  Node    : King's College London (Part-Time PhD)\x1b[0m",
        "\x1b[32m      \_|_|_/     Samples : EDTA Plasma & DNA Processing\x1b[0m",
        f"\x1b[32m       `\"\"\"`      Repos   : {repos}\x1b[0m",
        f"\x1b[32m                  Commits : {commits}\x1b[0m",
        "\x1b[32m                  System  : MU-TH-UR 6000\x1b[0m"
    ]

    for i, line in enumerate(neofetch_lines, start=6):
        t.gen_text(text=line, row_num=i)

    t.gen_text(text="\x1b[32m> \x1b[0m", row_num=17, contin=True)
    
    # 4. Export the final animation
    t.gen_gif()

except Exception as e:
    print(f"Error generating GIF: {e}")
    sys.exit(1)

import gifos
import os

# Initialize a CRT-style terminal frame
t = gifos.Terminal(width=800, height=500, xpad=15, ypad=15)

# Use ANSI escape \x1b[32m for Nostromo Glowing Green text
t.gen_text(text="\x1b[32mWEYLAND-YUTANI CORP: MU-TH-UR 6000 SYSTEM INTERFACE\x1b[0m", row_num=1)
t.gen_text(text="\x1b[32m===================================================\x1b[0m", row_num=2)

# Simulate system boot typing
t.gen_text(text="\x1b[32m> INITIATING PROTOCOL: TATO_ESTEBAN.SYS ...\x1b[0m", row_num=4)
t.gen_text(text="\x1b[32m> LOADING DOMAINS : Speech AI | Machine Learning | Genomics\x1b[0m", row_num=5)
t.gen_text(text="\x1b[32m> MOUNTING STACK  : Python | PyTorch | R | Bash\x1b[0m", row_num=6)

# Dynamically fetch your real GitHub stats
github_stats = gifos.utils.fetch_github_stats(user_name="TatoNomic")

t.gen_text(text="", row_num=7)
t.gen_text(text=f"\x1b[32m> TOTAL CONTRIBUTIONS : {github_stats.total_contributions}\x1b[0m", row_num=8)
t.gen_text(text=f"\x1b[32m> PUBLIC REPOSITORIES : {github_stats.public_repos}\x1b[0m", row_num=9)
t.gen_text(text=f"\x1b[32m> SYSTEM STATUS       : OPTIMAL\x1b[0m", row_num=10)

# Generate and save the animation as a GIF
t.gen_gif()

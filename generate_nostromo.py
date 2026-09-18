import gifos
import sys

try:
    # Initialize terminal with Nostromo dimensions
    t = gifos.Terminal(width=800, height=450, xpad=20, ypad=20)
    
    # \x1b[32m makes the text green. \x1b[0m resets it.
    t.gen_text(text="\x1b[32mWEYLAND-YUTANI CORP: MU-TH-UR 6000 SYSTEM INTERFACE\x1b[0m", row_num=1)
    t.gen_text(text="\x1b[32m===================================================\x1b[0m", row_num=2)
    
    t.gen_text(text="\x1b[32m> INITIATING PROTOCOL: TATO_ESTEBAN.SYS ...\x1b[0m", row_num=4)
    t.gen_text(text="\x1b[32m> KCL_GENOMICS_TERMINAL CONNECTED\x1b[0m", row_num=5)
    
    t.gen_text(text="\x1b[32m> LOADING MODULES : Speech AI | Genomics | Pipelines\x1b[0m", row_num=7)
    t.gen_text(text="\x1b[32m> MOUNTING STACK  : Python | PyTorch | R | Bash\x1b[0m", row_num=8)
    
    # Securely fetch GitHub account name as per the official docs
    try:
        github_stats = gifos.utils.fetch_github_stats(user_name="TatoNomic")
        t.gen_text(text=f"\x1b[32m> ACCOUNT DETECTED: {github_stats.account_name}\x1b[0m", row_num=10)
    except Exception:
        t.gen_text(text="\x1b[32m> ACCOUNT DETECTED: TatoNomic\x1b[0m", row_num=10)

    t.gen_text(text="\x1b[32m> SYSTEM STATUS   : OPTIMAL\x1b[0m", row_num=12)
    
    # Generate the looping GIF
    t.gen_gif()

except Exception as e:
    print(f"Failed to generate GIF: {e}")
    sys.exit(1)

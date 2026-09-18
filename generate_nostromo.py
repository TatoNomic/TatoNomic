import gifos
import sys
import traceback

try:
    # Initialize a CRT-style terminal frame
    t = gifos.Terminal(width=800, height=500, xpad=15, ypad=15)

    # ANSI escape \x1b[32m for Nostromo Glowing Green text
    t.gen_text(text="\x1b[32mWEYLAND-YUTANI CORP: MU-TH-UR 6000 SYSTEM INTERFACE\x1b[0m", row_num=1)
    t.gen_text(text="\x1b[32m===================================================\x1b[0m", row_num=2)

    # Simulate system boot typing
    t.gen_text(text="\x1b[32m> INITIATING PROTOCOL: TATO_ESTEBAN.SYS ...\x1b[0m", row_num=4)
    t.gen_text(text="\x1b[32m> LOADING DOMAINS : Speech AI | Machine Learning | Genomics\x1b[0m", row_num=5)
    t.gen_text(text="\x1b[32m> MOUNTING STACK  : Python | PyTorch | R | Bash\x1b[0m", row_num=6)
    
    t.gen_text(text="\x1b[32m> ACCOUNT DETECTED: TatoNomic\x1b[0m", row_num=8)
    t.gen_text(text="\x1b[32m> SYSTEM STATUS   : OPTIMAL\x1b[0m", row_num=9)

    # Generate and save the animation as a GIF
    t.gen_gif()

except Exception as e:
    print("\n--- ERROR LOG ---")
    traceback.print_exc()
    print("-----------------\n")
    sys.exit(1)

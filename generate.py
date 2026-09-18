import gifos
import os

# Set the GitHub token for the fetch_github_stats function
os.environ["GITHUB_TOKEN"] = os.getenv("GITHUB_TOKEN", "")

t = gifos.Terminal(width=320, height=240, xpad=5, ypad=5)
t.gen_text(text="Hello World!", row_num=1)
t.gen_text(text="With \x1b[32mANSI\x1b[0m escape sequence support!", row_num=2)

try:
    # This is where the library crashes due to the division by zero bug
    github_stats = gifos.utils.fetch_github_stats(
        user_name="TatoNomic"
    )
    account_name = github_stats.account_name
except ZeroDivisionError:
    # Bypass the developer's broken math and force the username
    account_name = "TatoNomic"
except Exception as e:
    account_name = "TatoNomic"

t.delete_row(row_num=1)
t.gen_text(text=f"GitHub Name: {account_name}", row_num=1, contin=True)

t.gen_gif()

import gifos
import os

# Set the GitHub token for the fetch_github_stats function
os.environ["GITHUB_TOKEN"] = os.getenv("GITHUB_TOKEN", "")

t = gifos.Terminal(width=320, height=240, xpad=5, ypad=5)
t.gen_text(text="Hello World!", row_num=1)
t.gen_text(text="With \x1b[32mANSI\x1b[0m escape sequence support!", row_num=2)

github_stats = gifos.utils.fetch_github_stats(
    user_name="TatoNomic"
)  # needs GITHUB_TOKEN in .env or as environment variable

t.delete_row(row_num=1)
t.gen_text(text=f"GitHub Name: {github_stats.account_name}", row_num=1, contin=True)

t.gen_gif()

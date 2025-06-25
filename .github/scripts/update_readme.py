from github import Github
import os
import re

g = Github(os.environ['GITHUB_TOKEN'])
user = g.get_user("Alok77it")

repos = {
    "K8S_COMMIT": "Full-Stack-Kubernetes-App-with-CI-CD-on-Local-Kind-Cluster",
    "PYTHON_COMMIT": "Python_practice_mini_project",
    "NGINX_COMMIT": "Nginx-Reverse-Proxy-Docker",
}

def get_last_commit_date(repo_name):
    repo = user.get_repo(repo_name)
    commit = next(repo.get_commits())
    # Format as YYYY-MM-DD HH:MM
    return commit.commit.author.date.strftime("%Y-%m-%d %H:%M")

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

for placeholder, repo_name in repos.items():
    date = get_last_commit_date(repo_name)
    # Replace the placeholder with the date, keeping the comment tag
    readme = re.sub(
        f"<!--{placeholder}-->.*?(?=</b></sub>|<\\/b><\\/sub>|<\\/b>)",
        f"<!--{placeholder}-->{date}",
        readme,
        flags=re.DOTALL
    )
    # If simpler placeholder, fallback replacement
    readme = readme.replace(f"<!--{placeholder}-->", date)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)

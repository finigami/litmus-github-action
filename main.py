# import logging
# import sys

# class GitHubActionsFormatter(logging.Formatter):
#     def format(self, record):
#         level = record.levelname.lower()
#         if level in ["warning", "error", "info", "debug"]:
#             return f"::{level}::{record.getMessage()}"
#         return record.getMessage()

# handler = logging.StreamHandler(sys.stdout)
# handler.setFormatter(GitHubActionsFormatter())

# logger = logging.getLogger("github-actions")
# logger.setLevel(logging.INFO)
# logger.addHandler(handler)

# logger.info("Deployment started")
# logger.warning("Disk usage is high")
# logger.error("Deployment failed")

print("Hello, Github Action World!")

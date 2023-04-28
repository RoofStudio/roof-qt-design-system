import os
import re
import subprocess
from invoke import task


def update_version(version_files, fix_type):
    for version_file in version_files:
        with open(version_file, "r") as f:
            content = f.read()

        if "version=" in content:
            version = re.search(r"version=['\"](\d+\.\d+\.\d+)['\"]", content).group(1)
        elif "__version__" in content:
            version = re.search(
                r"__version__ = ['\"](\d+\.\d+\.\d+)['\"]", content
            ).group(1)

        major, minor, patch = map(int, version.split("."))

        if fix_type == "bug":
            patch += 1
        elif fix_type == "low":
            minor += 1
            patch = 0
        elif fix_type == "high":
            major += 1
            minor = 0
            patch = 0

        new_version = f"{major}.{minor}.{patch}"

        if "version=" in content:
            content = re.sub(
                r"version=['\"]\d+\.\d+\.\d+['\"]", f"version='{new_version}'", content
            )
        elif "__version__" in content:
            content = re.sub(
                r"__version__ = ['\"]\d+\.\d+\.\d+['\"]",
                f"__version__ = '{new_version}'",
                content,
            )

        with open(version_file, "w") as f:
            f.write(content)


@task
def release(c, fix_type):
    version_files = [
        "setup.py",
    ]

    # Update the version in the version files
    update_version(version_files, fix_type)

    # Commit the changes
    c.run(f"git add {' '.join(version_files)}")
    c.run(f'git commit -m "Release {fix_type.capitalize()} Fix"')

    # Create a new tag
    c.run("git tag v{new_version}")

    # Push the changes and the new tag to GitHub
    c.run("git push")
    c.run("git push --tags")


@task
def lock(c):
    c.run("pipenv run pip freeze > requirements.txt")


@task
def start(c):
    c.run("invoke lint && python main.py")


@task
def test(c):
    c.run("invoke lint && python -m unittest")


@task
def clean(c):
    c.run("find . -name '*.pyc' -delete")


@task
def lint(c):
    c.run("pipenv run black .")

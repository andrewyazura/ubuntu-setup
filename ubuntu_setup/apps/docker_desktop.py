import click

from ..utils import run_command, run_commands

DOCKER_REPO_SETUP = [
    "sudo apt install -y ca-certificates curl gnupg",
    "sudo install -m 0755 -d /etc/apt/keyrings",
    (
        "curl -fsSL https://download.docker.com/linux/ubuntu/gpg"
        "| sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg"
    ),
    "sudo chmod a+r /etc/apt/keyrings/docker.gpg",
    (
        'echo "deb [arch="$(dpkg --print-architecture)"'
        " signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu"
        ' "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable"'
        " | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null"
    ),
    "sudo apt update",
]


def install_docker_desktop(deb_file_path: str) -> None:
    run_commands(DOCKER_REPO_SETUP)

    run_command(f"sudo apt install -y {deb_file_path}")
    click.secho("docker desktop install completed!", bg="green")

import subprocess


def setup_remote():
    cp = subprocess.run(
        ["flatpak", "remotes", "--columns=name"],
        capture_output=True,
    )

    remotes = cp.stdout.decode().splitlines()

    if "flathub" not in remotes:
        subprocess.run(
            [
                "flatpak",
                "remote-add",
                "flathub",
                "https://dl.flathub.org/repo/flathub.flatpakrepo",
            ],
            capture_output=True,
        )

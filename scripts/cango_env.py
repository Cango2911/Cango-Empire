# -*- coding: utf-8 -*-
"""Zentrale .env-Ladung für CanGo-Empire-Skripte — keine Passwörter im Quelltext."""

from __future__ import annotations

import os
from pathlib import Path

_REPO_ROOT: Path | None = None


def repo_root() -> Path:
    global _REPO_ROOT
    if _REPO_ROOT is None:
        _REPO_ROOT = Path(__file__).resolve().parent.parent
    return _REPO_ROOT


def load_env() -> None:
    """Lädt KEY=value aus .env im Repo-Root (setzt nur Keys, die noch fehlen)."""
    env_file = repo_root() / ".env"
    if not env_file.is_file():
        return
    for line in env_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            continue
        key, _, val = line.partition("=")
        key = key.strip()
        val = val.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = val


def ftp_credentials(*, require_password: bool = True) -> tuple[str, str, str]:
    """FTP-Host, -User und -Passwort aus Umgebung (.env oder export)."""
    load_env()
    host = os.environ.get("FTP_HOST", "145.223.115.121")
    user = os.environ.get("FTP_USER", "u447057499.automation-cango-app-empire.com")
    pw = os.environ.get("FTP_PASS", "")
    if require_password and not pw:
        raise RuntimeError(
            "FTP_PASS fehlt: Legen Sie eine .env im Repo-Root an (siehe .env.example) "
            "oder setzen Sie die Umgebungsvariable FTP_PASS."
        )
    return host, user, pw

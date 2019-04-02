"""Write your plugin in here!

This module comes with two example implementations of a hook, one wrapped in
a class and one as a standalone hook function.

.. module:: gofmt
    :synopsis: Plugin for RepoBee that runs gofmt on .go files

.. moduleauthor:: Simon Lasén
"""
import pathlib
import sys
import os
import subprocess
from typing import Union

# this import you'll need
import repobee_plug as plug

PLUGIN_NAME = "gofmt"


def _run_gofmt(files):
    ok = []
    need_formatting = []
    for file in files:
        proc = subprocess.run(
            ["gofmt", "-d", str(file.absolute())],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=False,
        )
        if proc.stdout:  # if there is a diff, bad formatting!
            need_formatting.append(file)
        else:
            ok.append(file)
    return ok, need_formatting


@plug.repobee_hook
def act_on_cloned_repo(path: Union[str, pathlib.Path], api) -> plug.HookResult:
    """Return an error hookresult with a garbage message.
    
    Args:
        path: Path to the student repo.
            api: An instance of :py:class:`repobee.github_api.GitHubAPI`.
    Returns:
        a plug.HookResult specifying the outcome.
    """
    path = pathlib.Path(path)
    gofiles = [
        p for p in path.resolve().rglob("*.go") if ".git" not in str(p).split(os.sep)
    ]
    if not gofiles:
        return plug.HookResult(
            hook=PLUGIN_NAME, status=plug.Status.WARNING, msg="Found no .go-files"
        )

    ok, need_formatting = _run_gofmt(gofiles)

    msg = "\n".join(
        ["not formatted: " + str(file) for file in need_formatting]
        + ["looks ok: " + str(file) for file in ok]
    )

    return plug.HookResult(
        hook=PLUGIN_NAME,
        status=plug.Status.SUCCESS if not need_formatting else plug.Status.ERROR,
        msg=msg,
    )

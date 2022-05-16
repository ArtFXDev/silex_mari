# pylint: skip-file
name = "silex_mari"
version = "0.0.5"

authors = ["ArtFx TD gang"]

description = """
    Set of python module and mari config to integrate mari in the silex pipeline
    Part of the Silex ecosystem
    """

vcs = "git"

build_command = "python {root}/script/build.py {install}"


def commands():
    """
    Set the environment variables for silex_mari
    """
    env.SILEX_ACTION_CONFIG.prepend("{root}/silex_mari/config")
    env.PYTHONPATH.append("{root}")
    env.MARI_PATH.append("{root}/startup")
    env.MARI_SCRIPT_PATH.append("{root}/script")

    #parser_module = ".".join(["silex_mari", "cli", "parser"])
    #alias("silex", f"hython -m {parser_module}")


@late()
def requires():
    major = str(this.version.major)
    silex_requirement = ["silex_client"]
    if major in ["dev", "beta", "prod"]:
        silex_requirement = [f"silex_client-{major}"]

    return ["mari", "python-3.7"] + silex_requirement
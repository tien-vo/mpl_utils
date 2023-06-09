import matplotlib.pyplot as plt
import matplotlib as mpl
import tempfile
import atexit
import shutil
import os

__all__ = ["init"]


def _checkdep_usetex(s):
    return s and shutil.which("tex")


def init(tex=False, cache=False, **kw):
    plt.style.use("mpl_utils")
    plt.rc("text", usetex=_checkdep_usetex(tex))
    if cache:
        # Quick fix for matplotlib's tex cache in multiprocessing
        mpldir = tempfile.mkdtemp()
        atexit.register(shutil.rmtree, mpldir)
        umask = os.umask(0)
        os.umask(umask)
        os.chmod(mpldir, 0o777 & ~umask)
        os.environ["HOME"] = mpldir
        os.environ["MPLCONFIGDIR"] = mpldir

        class TexManager(mpl.texmanager.TexManager):
            texcache = os.path.join(mpldir, "tex.cache")

        mpl.texmanager.TexManager = TexManager

### allnodes['lamb1'] is a tuple of 5 elements: OS, Arch, Platform, pkgType,
### encoding. Each element must be a string.
### 'pkgType' is the native package type for the node (must be one of "source",
### "win.binary", "win64.binary", "mac.binary", "mac.binary.leopard",
### or "mac.binary.mavericks").
### 'encoding' must be an encoding accepted by Python function
### codecs.getdecoder() (test it from python with e.g.
### codecs.getdecoder('utf_8') or codecs.getdecoder('iso8859'))

# FIXME - parameterize this as much as possible
# OS version, etc. can be obtained programmatically

allnodes = {
    'malbec1':    ("Linux (Ubuntu 16.04.1 LTS)",
                   "x86_64",
                   "x86_64-linux-gnu",
                   "source",
                   "utf_8"),
    'malbec2':    ("Linux (Ubuntu 16.04.1 LTS)",
                   "x86_64",
                   "x86_64-linux-gnu",
                   "source",
                   "utf_8"),
    'lamb1':      ("Linux (openSUSE 12.1)",
                   "x86_64",
                   "x86_64-suse-linux",
                   "source",
                   "utf_8"),
    'lamb2':      ("Linux (openSUSE 11.4)",
                   "x86_64",
                   "x86_64-suse-linux",
                   "source",
                   "utf_8"),
    'george2':    ("Linux (Ubuntu 12.04.1 LTS)",
                   "x86_64",
                   "x86_64-linux-gnu",
                   "source",
                  "utf_8"),
    'zin1':    ("Linux (Ubuntu 16.04 LTS)",
                   "x86_64",
                   "x86_64-linux-gnu",
                   "source",
                   "utf_8"),
    'zin2':    ("Linux (Ubuntu 14.04.2 LTS)",
                   "x86_64",
                   "x86_64-linux-gnu",
                   "source",
                   "utf_8"),
    'linux1.bioconductor.org':    ("Linux (Ubuntu 14.04.2 LTS)",
                   "x86_64",
                   "x86_64-linux-gnu",
                   "source",
                   "utf_8"),
    'linux2.bioconductor.org':    ("Linux (Ubuntu 14.04.2 LTS)",
                   "x86_64",
                   "x86_64-linux-gnu",
                   "source",
                   "utf_8"),
    'dockernode':("Linux (Ubuntu 14.04.1 LTS)",
                   "x86_64",
                   "x86_64-linux-gnu",
                   "source",
                   "utf_8"),
    'wilson1':    ("Linux (openSUSE 11.1)",
                   "x86_64",
                   "x86_64-suse-linux",
                   "source",
                   "utf_8"),
    'wilson2':    ("Linux (openSUSE 11.4)",
                   "x86_64",
                   "x86_64-suse-linux",
                   "source",
                   "utf_8"),
    'puck5':      ("Linux (Ubuntu 12.04)",
                   "x86_64",
                   "x86_64-linux-gnu",
                   "source",
                   "utf_8"),
    'wellington': ("Linux (openSUSE 10.3)",
                   "i686",
                   "i586-suse-linux",
                   "source",
                   "utf_8"),
    'churchill':  ("Solaris 2.9",
                   "sparc",
                   "sparc-sun-solaris2.9",
                   "source",
                   "utf_8"),
    'gladstone':  ("Linux (SUSE 10.0)",
                   "x86_64",
                   "x86_64-suse-linux",
                   "source",
                   "utf_8"),
    'lemming':    ("Windows Server 2003 (32-bit)",
                   "x64",
                   "mingw32",
                   "win.binary",
                   "iso8859"),
    'liverpool':  ("Windows Server 2003 R2 (32-bit)",
                   "x64",
                   "mingw32",
                   "win.binary",
                   "iso8859"),
    'cyclonus':  ("Windows Server 2003 R2 (32-bit)",
                   "x64",
                   "mingw32",
                   "win.binary",
                   "iso8859"),
    'gewurz':     ("Windows Server 2008 R2 Enterprise SP1 (64-bit)",
                   "x64",
                   "x86_64-w64-mingw32",
                   "win64.binary",
                   "iso8859"),
    'moscato1':   ("Windows Server 2008 R2 Standard (64-bit)",
                   "x64",
                   "mingw32 / x86_64-w64-mingw32",
                   "win.binary",
                   "iso8859"),
    'windows1.bioconductor.org':   ("Windows Server 2012 R2 Enterprise SP1 (64-bit)",
                   "x64",
                   "mingw32 / x86_64-w64-mingw32",
                   "win.binary",
                   "iso8859"),
    'windows2.bioconductor.org':   ("Windows Server 2012 R2 Enterprise SP1 (64-bit)",
                   "x64",
                   "mingw32 / x86_64-w64-mingw32",
                   "win.binary",
                   "iso8859"),
    'moscato2':   ("Windows Server 2008 R2 Enterprise SP1 (64-bit)",
                   "x64",
                   "mingw32 / x86_64-w64-mingw32",
                   "win.binary",
                   "iso8859"),
    'tokay1':     ("Windows Server 2012 R2 Standard",
                   "x64",
                   "mingw32 / x86_64-w64-mingw32",
                   "win.binary",
                   "iso8859"),
    'tokay2':     ("Windows Server 2012 R2 Standard",
                   "x64",
                   "mingw32 / x86_64-w64-mingw32",
                   "win.binary",
                   "iso8859"),
    'walpole':    ("Windows XP",
                   "i686",
                   "mingw32",
                   "win.binary",
                   "iso8859"),
    'matrix1':    ("Windows XP",
                   "i686",
                   "mingw32",
                   "win.binary",
                   "iso8859"),
    'matrix2':    ("Windows XP",
                   "i686",
                   "mingw32",
                   "win.binary",
                   "iso8859"),
    'pitt':       ("Mac OS X Leopard (10.5.8)",
                   "i386",
                   "i686-apple-darwin8",
                   "mac.binary.leopard",
                   "utf_8"),
    'morelia':    ("Mac OS X Mavericks (10.9.5)",
                   "x86_64",
                   "x86_64-apple-darwin13.4.0",
                   "mac.binary.mavericks",
                   "utf-8"),
    'oaxaca':     ("Mac OS X Mavericks (10.9.5)",
                   "x86_64",
                   "x86_64-apple-darwin13.4.0",
                   "mac.binary.mavericks",
                   "utf-8"),
    'montagu':    ("Mac OS X Leopard (10.5.8)",
                   "i386",
                   "i686-apple-darwin8",
                   "mac.binary.leopard",
                   "utf_8"),
    'pelham':     ("Mac OS X Snow Leopard (10.6.8)",
                   "x86_64",
                   "i686-apple-darwin10",
                   "mac.binary",
                   "utf_8"),
    'petty':      ("Mac OS X Snow Leopard (10.6.8)",
                   "x86_64",
                   "i686-apple-darwin10",
                   "mac.binary",
                   "utf_8"),
    'perceval':   ("Mac OS X Snow Leopard (10.6.8)",
                   "x86_64",
                   "i686-apple-darwin10",
                   "mac.binary",
                   "utf_8"),
    'lionbook':   ("Mac OS X Lion (10.7.1)",
                   "i386",
                   "i686-apple-darwin11",
                   "mac.binary.leopard",
                   "utf_8"),
    'derby':      ("Mac OS X (10.4.11)",
                   "i386",
                   "i686-apple-darwin8",
                   "mac.binary",
                   "utf_8"),
    'compton':    ("Mac OS X (10.4.11)",
                   "i386",
                   "i686-apple-darwin8",
                   "mac.binary",
                   "utf_8")
}

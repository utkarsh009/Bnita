from anita import *

class Bnita(Anita):
    """Bnita is an extension for Anita that adds support for additional virtual machine systems like GXemul,
    You could treat it as the Beta version of Anita adding extra functionality
    or, as a step up from the previous version, hence, A -> B
    Also, Bnita (pronounced Bee-neeta) is my mom's name :)"""
    def __init__(self, already_installed = 0, **kwargs):
        Anita.__init__(self, **kwargs)
        self.already_installed = already_installed
    def gxemul_cdrom_args(self):
        return self.dist.iso_path()
    def gxemul_disk_args(self, path):
        return ["-d", path]
    vmm_args = []
    if self.already_installed is 0:
        vmm_args += ["-d", gxemul_cdrom_args()]
    if dist.arch() == 'pmax':
        vmm_args += ["-E 3max"]
        cd_device = 'cd0a'
    def start_gxemul(self, vmm_args, already_installed = 0):
        child = self.pexpect_spawn(gxemul, ["-M", str(self.memory_size()), "-d", os.path.abspath(self.wd0_path), os.path.abspath(os.path.join(self.dist.download_local_arch_dir(), "binary", "kernel", ("netbsd-INSTALL.gz", "netbsd-GENERIC.gz")[already_installed]))] + vmm_args + self.extra_vmm_args)
        self.configure_child(child)
        return child
    if self.vmm == 'gxemul':
        scratch_disk_args = self.gxemul_disk_args(os.path.abspath(scratch_disk_path))
        child = self.start_gxemul(vmm_args, already_installed)
    def start_boot(self, vmm_args = None):
        if vmm_args is None:
            vmm_args = []
        if not self.no_install:
            self.install()
        if self.vmm = 'gxemul':
            child = self.start_gxemul(vmm_args)
        else:
            raise RuntimeError('unknown vmm %s' % vmm)
        self.child = child
        return child

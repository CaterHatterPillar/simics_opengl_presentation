import os
import sys
import operator
import fileinput

if __name__ == "__main__":

terms = [('\dvttermapi', 'API'),
         ('\dvttermabi', 'ABI'),
         ('\dvttermandroid', 'Android'),
         ('\dvttermandroidsdk', 'Android SDK'),
         ('\dvttermandroidemulator', 'Android emulator'),
         ('\dvttermacm', 'ACM'),
         ('\dvttermarm', 'ARM'),
         ('\dvttermcheckpoint', 'checkpoint'),
         ('\dvttermcheckpointing', 'checkpointing'),
         ('\dvttermcpu', 'CPU'),
         ('\dvttermcheckpointrestart', 'Checkpoint / Restart'),
         ('\dvttermcuda', 'CUDA'),
         ('\dvttermc', '\texttt{C}'),
         ('\dvttermcplusplus', '\texttt{C++}'),
         ('\dvttermcisco', 'Cisco Systems, Inc.'),
         ('\dvttermdirectvirtualization', 'Hardware-assisted Virtualization'),
         ('\dvttermdirectx', 'DirectX'),
         ('\dvttermdeterministicexecution', 'Deterministic Execution'),
         ('\dvttermdeterministicalgorithm', 'Deterministic Algorithm'),
         ('\dvttermericsson', 'Ericsson'),
         ('\dvttermegl', 'EGL'),
         ('\dvttermfedora', 'Fedora 19'),
         ('\dvttermfullsystemsimulation', 'Full-system Simulation'),
         ('\dvttermfreescalesemiconductor', 'Freescale Semiconductor, Inc.'),
         ('\dvttermfps', 'frames per second'),
         ('\dvttermflops', 'floating-point operations per second'), # use acronym insetad?
         ('\dvttermgpu', 'GPU'),
         ('\dvttermgpgpu', 'GPGPU'),
         ('\dvttermgoogle', 'Google'),
         ('\dvttermgeavionics', 'GE Aviation'),
         ('\dvttermgui', 'GUI'),
         ('\dvttermhost', 'host'),
         ('\dvttermhewlettpackard', 'Hewlett-Packard Company'),
         ('\dvttermhoneywell', 'Honeywell International, Inc.'),
         ('\dvttermhypersimulation', 'hypersimulation'),
         ('\dvttermhostvirtualizationextensions', 'Host Virtualization Extensions'),
         ('\dvttermhaxm', 'Intel\circledR\ HAXM'),
         ('\dvtterminterpretation', 'interpretation'),
         ('\dvttermintel', 'Intel\circledR'),
         ('\dvttermintelcoreiseven', 'Intel\circledR\ Core\texttrademark\ i7'),
         ('\dvttermibm', 'IBM'),
         ('\dvttermisa', 'ISA'),
         ('\dvttermieee', 'IEEE'),
         ('\dvttermieeefp', 'IEEE 754'),
         ('\dvttermios', 'iOS'),
         ('\dvttermjit', 'just-in-time'),
         ('\dvttermjni', 'Java Native Interface'),
         ('\dvttermkhronos', 'Khronos'),
         ('\dvttermkvm', 'KVM'), # Kernel-based Virtual Machine
         ('\dvttermlinux', 'Linux'),
         ('\dvttermlockheedmartin', 'Lockheed Martin'),
         ('\dvttermmipssecond', 'MIPS'), # Million Instructions Per Second
         ('\dvttermmicrosoft', 'Microsoft'),
         ('\dvttermmagicinstruction', 'magic instruction'),
         ('\dvttermmmu', 'MMU'),
         ('\dvttermnasa', 'NASA'),
         ('\dvttermnortel', 'Nortel Networks Corporation'),
         ('\dvttermnorthropgrumman', 'Northrop Grumman Corporation'),
         ('\dvttermopengl', 'OpenGL'),
         ('\dvttermopengles', 'OpenGL~ES'),
         ('\dvttermopenglestwopointo', 'OpenGL~ES~$2.0$'),
         ('\dvttermos', 'OS'),
         ('\dvttermpci', 'PCI'),
         ('\dvttermpcipassthrough', 'PCI~passthrough'),
         ('\dvttermparavirtualization', 'Paravirtualization'),
         ('\dvttermpython', '\texttt{Python}'),
         ('\dvttermqemu', 'QEMU'),
         ('\dvttermreverseexecution', 'reverse execution'),
         ('\dvttermsoftwarerendering', 'software rendering'),
         ('\dvttermsimics', 'Simics'),
         ('\dvttermsics', 'Swedish Institute of Computer Science'),
         ('\dvttermsunmicrosystems', 'Sun Microsystems, Inc.'),
         ('\dvttermsimd', 'SIMD'),
         ('\dvttermttm', 'time-to-market'),
         ('\dvttermtiming', 'timing'),
         ('\dvttermtarget', 'target'),
         ('\dvttermuart', 'UART'),
         ('\dvttermvirtutech', 'Virtutech'),
         ('\dvttermvmware', 'VMware, Inc.'),
         ('\dvttermvalve', 'Valve Corporation'),
         ('\dvttermwarp', 'Microsoft~WARP'),
         ('\dvttermwindriver', 'Wind River Systems, Inc.'),
         ('\dvttermwindows', 'Windows'),
         ('\dvttermxeleven', 'X11'),
         ('\dvttermxeightysix', 'x86')]

terms.sort(key=operator.itemgetter(0), reverse=True)

def replace_all(line, replace_with):
    for cmd, word in replace_with:
        line = line.replace(cmd + ' s', word + 's') # Plurals
        line = line.replace(cmd + '\\', word) # Escaped commands
        line = line.replace(cmd, word) # Regular commands
    return line

if __name__ == "__main__":
    for f in os.listdir("src"):
        if f.endswith(".tex"):
            for line in fileinput.input('src/%s' % f, inplace=True):
                print replace_all(line, terms),

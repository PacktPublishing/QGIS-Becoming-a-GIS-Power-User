# Enable backtrace
echo 0 > /proc/sys/kernel/yama/ptrace_scope

# Reload sysctl if you edited /etc/sysctl.d/10-ptrace.conf 
sysctl -p

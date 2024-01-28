### CPU load
stress-ng --cpu 4 --cpu-method matrixprod --metrics --timeout 60

### IO load
stress-ng --sequential 0 --class io --timeout 60s --metrics-brief

### Memory load
stress-ng --sequential 0 --class memory --timeout 60s --metrics-brief

### CPU+memory+IO load
stress-ng --cpu 4 --io 4 --vm 1 --vm-bytes 1G --timeout 60s --metrics-brief
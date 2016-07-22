try:
    with open('/proc/sys/crypto/fips_enabled') as f:
        fips_mode = int(f.read())
except:
    fips_mode = 0
